"""Render a .pptx (or .pdf) into one PNG grid of numbered slide thumbnails.

Usage: python3 scripts/contact_sheet.py deck.pptx out.png [--cols 4] [--first N --last M]
Needs: soffice (for .pptx), pdftoppm, Pillow.
"""
import argparse, glob, os, subprocess, tempfile
from PIL import Image, ImageDraw


def tile(paths, cols, numbers, thumb_w=480, pad=16, label_h=28):
    first = Image.open(paths[0])
    thumb_h = round(first.height * thumb_w / first.width)
    rows = -(-len(paths) // cols)
    sheet = Image.new("RGB", (pad + cols * (thumb_w + pad), pad + rows * (thumb_h + label_h + pad)), "#e9e9e9")
    draw = ImageDraw.Draw(sheet)
    for i, (p, n) in enumerate(zip(paths, numbers)):
        x = pad + (i % cols) * (thumb_w + pad)
        y = pad + (i // cols) * (thumb_h + label_h + pad)
        sheet.paste(Image.open(p).convert("RGB").resize((thumb_w, thumb_h)), (x, y + label_h))
        draw.text((x, y + 6), f"Slide {n}", fill="#222")
    return sheet


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("deck"); ap.add_argument("out")
    ap.add_argument("--cols", type=int, default=4)
    ap.add_argument("--first", type=int, default=1); ap.add_argument("--last", type=int)
    a = ap.parse_args()
    with tempfile.TemporaryDirectory() as tmp:
        pdf = a.deck
        if a.deck.lower().endswith(".pptx"):
            subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", tmp, a.deck],
                           check=True, capture_output=True)
            pdf = os.path.join(tmp, os.path.splitext(os.path.basename(a.deck))[0] + ".pdf")
        cmd = ["pdftoppm", "-png", "-r", "60", "-f", str(a.first)] + (["-l", str(a.last)] if a.last else [])
        subprocess.run(cmd + [pdf, os.path.join(tmp, "s")], check=True)
        pages = sorted(glob.glob(os.path.join(tmp, "s-*.png")), key=lambda p: int(p.rsplit("-", 1)[1][:-4]))
        numbers = [int(p.rsplit("-", 1)[1][:-4]) for p in pages]
        tile(pages, a.cols, numbers).save(a.out)
    print(f"{a.out}: {len(pages)} slides")


if __name__ == "__main__":
    main()
