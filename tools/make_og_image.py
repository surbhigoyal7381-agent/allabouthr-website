# -*- coding: utf-8 -*-
"""Generate the 1200x630 Open Graph share card at assets/og-cover.png.

    python tools/make_og_image.py

Why this exists: without an og:image, every link to this site shared on
WhatsApp, LinkedIn or Slack renders as a bare grey box. WhatsApp is the
business's main inbound channel, so that is a real cost.

1200x630 is the size LinkedIn, Facebook and WhatsApp all crop cleanly from.
The gradient is the same plum -> teal used by the .qband on the site.
"""

import io
import os

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W, H = 1200, 630

PLUM_D = (110, 37, 100)
TEAL_D = (1, 83, 111)
WHITE = (255, 255, 255)

FONT_DIR = r"C:\Windows\Fonts"
BOLD = os.path.join(FONT_DIR, "segoeuib.ttf")
REG = os.path.join(FONT_DIR, "segoeui.ttf")


def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()


def gradient(w, h, c1, c2):
    """Diagonal plum -> teal, matching the .qband on the site.

    Computed small and scaled up: exact, smooth, and fast. Computing it at full
    size pixel by pixel in Python is slow, and stepping columns leaves banding.
    """
    sw, sh = 160, 84
    small = Image.new("RGB", (sw, sh))
    px = small.load()
    for y in range(sh):
        for x in range(sw):
            # normalise so the full 0..1 range is actually used corner to corner
            t = (x / (sw - 1)) * 0.75 + (y / (sh - 1)) * 0.25
            px[x, y] = tuple(int(round(c1[i] + (c2[i] - c1[i]) * t)) for i in range(3))
    return small.resize((w, h), Image.BICUBIC)


def main():
    img = gradient(W, H, PLUM_D, TEAL_D)
    d = ImageDraw.Draw(img, "RGBA")

    # soft brand orbs, echoing the hero
    d.ellipse([W - 300, -190, W + 190, 300], fill=(255, 255, 255, 18))
    d.ellipse([-170, H - 250, 260, H + 180], fill=(255, 255, 255, 14))

    # logo, on the white plate the brand uses in dark contexts
    logo_path = os.path.join(ROOT, "assets", "logo.webp")
    if os.path.isfile(logo_path):
        logo = Image.open(logo_path).convert("RGBA")
        lw = 440
        logo = logo.resize((lw, int(logo.height * lw / logo.width)), Image.LANCZOS)
        pad = 26
        plate = Image.new("RGBA", (logo.width + pad * 2, logo.height + pad * 2), (255, 255, 255, 255))
        plate.alpha_composite(logo, (pad, pad))
        img.paste(plate, (80, 74), plate)

    MAXW = W - 160                      # 80px gutter each side
    HEADLINE = ["Every business runs on two engines",
                "— its people and its systems."]

    # shrink until the longest line fits; never let text run off the card
    size = 64
    while size > 34:
        f_h1 = font(BOLD, size)
        if max(d.textlength(l, font=f_h1) for l in HEADLINE) <= MAXW:
            break
        size -= 2
    f_h1 = font(BOLD, size)
    f_sub = font(REG, 31)
    f_small = font(REG, 25)

    y = 244
    for line in HEADLINE:
        d.text((80, y), line, font=f_h1, fill=WHITE)
        y += int(size * 1.18)

    d.text((80, y + 22),
           "HR consulting, HR software and business systems",
           font=f_sub, fill=(255, 255, 255, 235))
    d.text((80, y + 64),
           "for Indian companies from 10 to 2,500 people.",
           font=f_sub, fill=(255, 255, 255, 235))

    # footer strip
    d.line([(80, H - 96), (W - 80, H - 96)], fill=(255, 255, 255, 70), width=2)
    d.text((80, H - 72), "allabouthr.co", font=font(BOLD, 27), fill=WHITE)
    d.text((W - 80 - d.textlength("Mohali, Punjab · Since 2023", font=f_small), H - 70),
           "Mohali, Punjab · Since 2023", font=f_small, fill=(255, 255, 255, 215))

    out = os.path.join(ROOT, "assets", "og-cover.png")
    img.convert("RGB").save(out, "PNG", optimize=True)
    size = os.path.getsize(out)
    print("wrote %s  (%dx%d, %.0f KB)" % (
        os.path.relpath(out, ROOT).replace("\\", "/"), W, H, size / 1024.0))
    if size > 300 * 1024:
        print("  note: >300KB — some scrapers skip large images")


if __name__ == "__main__":
    main()
