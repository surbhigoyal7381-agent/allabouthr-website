# -*- coding: utf-8 -*-
"""Local dev server that behaves like Netlify, so you can test this site properly.

    python tools/serve.py [port]        # default 8777

Plain `python -m http.server` is not enough here: it ignores `_redirects` and
serves its own bare 404 page, which are exactly the two things this release
changed. This server:

  * serves static files, with directory index.html lookup;
  * applies the rules in `_redirects`, including `/prefix/*` wildcards;
  * serves `404.html` with a real 404 status for anything unknown;
  * logs every request with its status, so you can watch the redirects fire.

It is a development tool only. Nothing here ships to the host.
"""

import io
import os
import posixpath
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import unquote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GREY, GREEN, YELLOW, RED, RESET = "\033[90m", "\033[32m", "\033[33m", "\033[31m", "\033[0m"


def load_redirects():
    """Parse _redirects into (from, to, status) plus (prefix, to, status) wildcards."""
    exact, wildcard = {}, []
    path = os.path.join(ROOT, "_redirects")
    if not os.path.isfile(path):
        return exact, wildcard
    for line in io.open(path, encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) < 2:
            continue
        src, dst = parts[0], parts[1]
        status = int(parts[2]) if len(parts) > 2 and parts[2].isdigit() else 301
        if src.endswith("/*"):
            wildcard.append((src[:-1], dst, status))   # keep the trailing slash
        else:
            exact[src.rstrip("/") or "/"] = (dst, status)
    return exact, wildcard


# Re-read per request: this is a dev server, and caching the table at startup means a
# rebuild silently serves stale rules until you remember to restart.
EXACT, WILDCARD = load_redirects()


TEXTUAL = (".html", ".css", ".js", ".json", ".xml", ".txt", ".svg", ".webmanifest")


class Handler(SimpleHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def guess_type(self, path):
        """Netlify serves text as UTF-8; say so, or non-ASCII renders as mojibake."""
        ctype = SimpleHTTPRequestHandler.guess_type(self, path)
        if path.lower().endswith(TEXTUAL) and "charset=" not in ctype:
            ctype += "; charset=utf-8"
        return ctype

    def translate_path(self, path):
        path = posixpath.normpath(unquote(path.split("?", 1)[0].split("#", 1)[0]))
        full = os.path.join(ROOT, *[p for p in path.split("/") if p not in ("", ".", "..")])
        return full

    def match_redirect(self):
        exact, wildcard = load_redirects()
        key = self.path.split("?", 1)[0].split("#", 1)[0]
        lookup = key.rstrip("/") or "/"
        if lookup in exact:
            return exact[lookup]
        for prefix, dst, status in wildcard:
            if key.startswith(prefix):
                return dst, status
        return None

    def send_404(self):
        page = os.path.join(ROOT, "404.html")
        if os.path.isfile(page):
            data = io.open(page, "rb").read()
            self.send_response(404)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            if self.command != "HEAD":
                self.wfile.write(data)
        else:
            self.send_error(404, "Not Found")

    def do_GET(self):
        self.handle_request()

    def do_HEAD(self):
        self.handle_request()

    def handle_request(self):
        # 1 — a static file or directory index wins, as it does on Netlify
        target = self.translate_path(self.path)
        if os.path.isdir(target):
            if not self.path.split("?")[0].endswith("/"):
                self.send_response(301)
                self.send_header("Location", self.path.split("?")[0] + "/")
                self.send_header("Content-Length", "0")
                self.end_headers()
                return
            if os.path.isfile(os.path.join(target, "index.html")):
                return SimpleHTTPRequestHandler.do_GET(self) if self.command == "GET" \
                    else SimpleHTTPRequestHandler.do_HEAD(self)
        elif os.path.isfile(target):
            return SimpleHTTPRequestHandler.do_GET(self) if self.command == "GET" \
                else SimpleHTTPRequestHandler.do_HEAD(self)

        # 2 — then the redirect table
        hit = self.match_redirect()
        if hit:
            dst, status = hit
            if status == 404:
                return self.send_404()
            self.send_response(status)
            self.send_header("Location", dst)
            self.send_header("Content-Length", "0")
            self.end_headers()
            return

        # 3 — otherwise the branded 404
        self.send_404()

    def log_message(self, fmt, *args):
        msg = fmt % args
        code = ""
        for part in msg.split():
            if part.isdigit() and len(part) == 3:
                code = part
                break
        colour = GREEN if code.startswith("2") else YELLOW if code.startswith("3") \
            else RED if code else GREY
        sys.stderr.write("%s%s%s\n" % (colour, msg, RESET))


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8777
    srv = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print("AllAboutHR dev server  —  http://localhost:%d/" % port)
    print("  root        %s" % ROOT)
    print("  redirects   %d exact, %d wildcard (from _redirects)"
          % (len(EXACT), len(WILDCARD)))
    print("  404 page    %s"
          % ("404.html" if os.path.isfile(os.path.join(ROOT, "404.html")) else "MISSING"))
    print("\nCtrl+C to stop.\n")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nstopped.")


if __name__ == "__main__":
    main()
