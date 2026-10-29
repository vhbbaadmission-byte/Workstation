#!/usr/bin/env python3
"""
extract_palette.py — pull REAL colors from a reference image (a slide, a UI, a
design you like) so the deck's tokens are sampled pixels, never hallucinated hex.

Usage:
    python extract_palette.py <image_path> [--colors 8] [--json]

Prints a human summary by default; add --json for machine-readable output.
Only dependency is Pillow. Every hex it prints is a color that is actually in the
image (quantized), with the share of the image it covers. Vision fills in the
*roles* (which one is the accent, etc.); this script fills in the *values*.
"""
import sys, json, colorsys, argparse
from collections import Counter

try:
    from PIL import Image
except ImportError:
    sys.exit("Pillow is required: pip install Pillow")


def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)


def luminance(rgb):
    # relative luminance, 0 (black) .. 1 (white)
    r, g, b = [c / 255 for c in rgb]
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def saturation(rgb):
    r, g, b = [c / 255 for c in rgb]
    _, _, s = colorsys.rgb_to_hls(r, g, b)  # HLS: s is saturation
    return s


def is_neutral(rgb, sat_threshold=0.12):
    return saturation(rgb) < sat_threshold


def extract(path, n_colors=8):
    img = Image.open(path).convert("RGB")
    w, h = img.size
    # cap work for large images; area ratios are unchanged by downscale
    if max(w, h) > 800:
        img.thumbnail((800, 800))
    small = img
    pal = small.quantize(colors=max(n_colors * 3, 16), method=Image.Quantize.FASTOCTREE)
    try:
        counts = Counter(pal.get_flattened_data())
    except AttributeError:
        counts = Counter(pal.getdata())
    palette = pal.getpalette()
    total = sum(counts.values())

    swatches = []
    for idx, cnt in counts.most_common():
        rgb = tuple(palette[idx * 3: idx * 3 + 3])
        swatches.append({
            "hex": rgb_to_hex(rgb),
            "rgb": list(rgb),
            "pct": round(100 * cnt / total, 1),
            "lum": round(luminance(rgb), 3),
            "sat": round(saturation(rgb), 3),
        })

    # merge near-duplicate hexes, keep the top n_colors by area
    seen, merged = {}, []
    for s in swatches:
        key = tuple(round(c / 12) for c in s["rgb"])  # ~12-level bucket
        if key in seen:
            merged[seen[key]]["pct"] = round(merged[seen[key]]["pct"] + s["pct"], 1)
        else:
            seen[key] = len(merged)
            merged.append(s)
    merged.sort(key=lambda s: s["pct"], reverse=True)
    merged = merged[:n_colors]

    avg_lum = sum(s["lum"] * s["pct"] for s in merged) / max(sum(s["pct"] for s in merged), 1)
    theme = "dark" if avg_lum < 0.4 else ("light" if avg_lum > 0.7 else "mid")

    # role guesses — vision should confirm/override these
    neutrals = [s for s in merged if is_neutral(s["rgb"])]
    chromatics = [s for s in merged if not is_neutral(s["rgb"])]
    bg = merged[0]["hex"] if merged else None
    fg = max(merged, key=lambda s: abs(s["lum"] - merged[0]["lum"]))["hex"] if merged else None
    accent = max(chromatics, key=lambda s: s["sat"])["hex"] if chromatics else None

    return {
        "image": path,
        "size": [w, h],
        "aspect": round(w / h, 3) if h else None,
        "looks_like_slide_16x9": bool(h and abs(w / h - 16 / 9) < 0.06),
        "theme": theme,
        "avg_luminance": round(avg_lum, 3),
        "swatches": merged,
        "role_guess": {"background": bg, "foreground": fg, "accent": accent,
                       "neutrals": [s["hex"] for s in neutrals],
                       "chromatics": [s["hex"] for s in chromatics]},
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("image")
    ap.add_argument("--colors", type=int, default=8)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    data = extract(a.image, a.colors)
    if a.json:
        print(json.dumps(data, indent=2))
        return
    print(f"image      : {data['image']}  ({data['size'][0]}x{data['size'][1]}, "
          f"aspect {data['aspect']}, 16:9 slide? {data['looks_like_slide_16x9']})")
    print(f"theme      : {data['theme']}  (avg luminance {data['avg_luminance']})")
    print("palette    : (hex - % of image - luminance - saturation)")
    for s in data["swatches"]:
        print(f"   {s['hex']}   {s['pct']:>5}%   lum {s['lum']:.2f}   sat {s['sat']:.2f}")
    rg = data["role_guess"]
    print("role guess : (confirm/override with your eyes)")
    print(f"   background {rg['background']} | foreground {rg['foreground']} | accent {rg['accent']}")


if __name__ == "__main__":
    main()
