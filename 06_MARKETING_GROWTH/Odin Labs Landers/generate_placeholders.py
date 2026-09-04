#!/usr/bin/env python3
"""
Generate placeholder hero images for Odin Lab Calgary therapy landing pages.
1200x800px, dark green background (#1a3a1a), lime green (#c4ff49) labels.
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
import math
import random

OUTPUT_DIR = "/Users/alexandertretjakov/Downloads/odin lab landers/img"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Colors
BG_DARK = (26, 58, 26)          # #1a3a1a
LIME = (196, 255, 73)            # #c4ff49
LIME_DIM = (120, 180, 40)        # dimmer lime for accents
WHITE = (255, 255, 255)
DARK_OVERLAY = (10, 25, 10)      # near-black
MID_GREEN = (40, 90, 40)         # mid green for gradients

W, H = 1200, 800

images = [
    # Hydrogen Therapy
    {
        "filename": "hydrogen-hero-bw.jpg",
        "label": "Hydrogen Therapy",
        "sublabel": "Hero — B&W",
        "accent": "bw",
        "icon": "H₂",
        "desc": "Clinical Wellness"
    },
    {
        "filename": "hydrogen-hero-color.jpg",
        "label": "Hydrogen Therapy",
        "sublabel": "Hero — Color",
        "accent": "color",
        "icon": "H₂",
        "desc": "Clinical Wellness"
    },
    {
        "filename": "hydrogen-section.jpg",
        "label": "Hydrogen Therapy",
        "sublabel": "Section Image",
        "accent": "color",
        "icon": "◉",
        "desc": "Molecular Hydrogen"
    },
    # Functional Health & Medicine
    {
        "filename": "functional-health-hero-bw.jpg",
        "label": "Functional Health",
        "sublabel": "Hero — B&W",
        "accent": "bw",
        "icon": "⚕",
        "desc": "& Medicine"
    },
    {
        "filename": "functional-health-hero-color.jpg",
        "label": "Functional Health",
        "sublabel": "Hero — Color",
        "accent": "color",
        "icon": "⚕",
        "desc": "& Medicine"
    },
    {
        "filename": "functional-health-section.jpg",
        "label": "Functional Health",
        "sublabel": "Section Image",
        "accent": "color",
        "icon": "◈",
        "desc": "Systems Medicine"
    },
    # Functional Health Coaching
    {
        "filename": "functional-coaching-hero-bw.jpg",
        "label": "Health Coaching",
        "sublabel": "Hero — B&W",
        "accent": "bw",
        "icon": "✦",
        "desc": "Functional Coaching"
    },
    {
        "filename": "functional-coaching-hero-color.jpg",
        "label": "Health Coaching",
        "sublabel": "Hero — Color",
        "accent": "color",
        "icon": "✦",
        "desc": "Functional Coaching"
    },
    {
        "filename": "functional-coaching-section.jpg",
        "label": "Health Coaching",
        "sublabel": "Section Image",
        "accent": "color",
        "icon": "◐",
        "desc": "Transformation"
    },
    # Nutritional Supplementation & Herbology
    {
        "filename": "nutritional-hero-bw.jpg",
        "label": "Nutrition & Herbology",
        "sublabel": "Hero — B&W",
        "accent": "bw",
        "icon": "✿",
        "desc": "Supplementation"
    },
    {
        "filename": "nutritional-hero-color.jpg",
        "label": "Nutrition & Herbology",
        "sublabel": "Hero — Color",
        "accent": "color",
        "icon": "✿",
        "desc": "Supplementation"
    },
    {
        "filename": "nutritional-section.jpg",
        "label": "Nutrition & Herbology",
        "sublabel": "Section Image",
        "accent": "color",
        "icon": "❧",
        "desc": "Botanical Medicine"
    },
    # Marma Therapy
    {
        "filename": "marma-hero-bw.jpg",
        "label": "Marma Therapy",
        "sublabel": "Hero — B&W",
        "accent": "bw",
        "icon": "◯",
        "desc": "Sound & Vibration"
    },
    {
        "filename": "marma-hero-color.jpg",
        "label": "Marma Therapy",
        "sublabel": "Hero — Color",
        "accent": "color",
        "icon": "◯",
        "desc": "Sound & Vibration"
    },
    {
        "filename": "marma-section.jpg",
        "label": "Marma Therapy",
        "sublabel": "Section Image",
        "accent": "color",
        "icon": "⟁",
        "desc": "Frequency Healing"
    },
    # Ayurveda
    {
        "filename": "ayurveda-hero-bw.jpg",
        "label": "Ayurveda",
        "sublabel": "Hero — B&W",
        "accent": "bw",
        "icon": "⊕",
        "desc": "Ancient Wisdom"
    },
    {
        "filename": "ayurveda-hero-color.jpg",
        "label": "Ayurveda",
        "sublabel": "Hero — Color",
        "accent": "color",
        "icon": "⊕",
        "desc": "Ancient Wisdom"
    },
    {
        "filename": "ayurveda-section.jpg",
        "label": "Ayurveda",
        "sublabel": "Section Image",
        "accent": "color",
        "icon": "◭",
        "desc": "Elemental Balance"
    },
]


def draw_grid_lines(draw, color, alpha_factor=0.3):
    """Draw subtle grid lines."""
    line_color = tuple(int(c * alpha_factor) for c in color)
    # Horizontal lines
    for y in range(0, H, 80):
        draw.line([(0, y), (W, y)], fill=line_color, width=1)
    # Vertical lines
    for x in range(0, W, 80):
        draw.line([(x, 0), (x, H)], fill=line_color, width=1)


def draw_radial_glow(img, cx, cy, radius, color, intensity=0.4):
    """Draw a radial glow effect."""
    overlay = Image.new('RGB', (W, H), (0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    steps = 20
    for i in range(steps, 0, -1):
        r = int(radius * i / steps)
        alpha = int(255 * intensity * (1 - i / steps) * 0.5)
        glow_color = tuple(min(255, int(c * alpha / 255)) for c in color)
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=glow_color)
    blurred = overlay.filter(ImageFilter.GaussianBlur(radius=60))
    result = Image.blend(img, blurred, 0.5)
    return result


def draw_diagonal_lines(draw, color, spacing=120):
    """Draw diagonal accent lines."""
    line_color = tuple(int(c * 0.15) for c in color)
    for offset in range(-H, W + H, spacing):
        x1 = offset
        y1 = 0
        x2 = offset + H
        y2 = H
        draw.line([(x1, y1), (x2, y2)], fill=line_color, width=1)


def draw_circles(draw, cx, cy, color):
    """Draw concentric circle accents."""
    for r in [60, 120, 200, 300]:
        alpha = max(20, 60 - r // 6)
        c = tuple(int(ch * alpha / 255) for ch in color)
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=c, width=1)


def draw_corner_marks(draw, color):
    """Draw corner bracket marks."""
    size = 40
    thickness = 2
    c = tuple(int(ch * 0.6) for ch in color)
    # Top-left
    draw.line([(30, 30), (30 + size, 30)], fill=c, width=thickness)
    draw.line([(30, 30), (30, 30 + size)], fill=c, width=thickness)
    # Top-right
    draw.line([(W - 30, 30), (W - 30 - size, 30)], fill=c, width=thickness)
    draw.line([(W - 30, 30), (W - 30, 30 + size)], fill=c, width=thickness)
    # Bottom-left
    draw.line([(30, H - 30), (30 + size, H - 30)], fill=c, width=thickness)
    draw.line([(30, H - 30), (30, H - 30 - size)], fill=c, width=thickness)
    # Bottom-right
    draw.line([(W - 30, H - 30), (W - 30 - size, H - 30)], fill=c, width=thickness)
    draw.line([(W - 30, H - 30), (W - 30, H - 30 - size)], fill=c, width=thickness)


def draw_scan_lines(draw):
    """Draw subtle horizontal scan lines for depth."""
    for y in range(0, H, 4):
        alpha = 8
        draw.line([(0, y), (W, y)], fill=(0, 0, 0, alpha), width=1)


def draw_bottom_bar(draw, color):
    """Draw a bottom info bar."""
    bar_h = 60
    draw.rectangle([(0, H - bar_h), (W, H)], fill=tuple(int(c * 0.3) for c in color))
    draw.line([(0, H - bar_h), (W, H - bar_h)], fill=tuple(int(c * 0.8) for c in color), width=1)


def get_font(size):
    """Try to get a system font, fall back to default."""
    font_paths = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/HelveticaNeue.ttc",
        "/System/Library/Fonts/Arial.ttf",
        "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/SFNSDisplay.ttf",
        "/System/Library/Fonts/SFNS.ttf",
    ]
    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue
    return ImageFont.load_default()


def create_image(cfg):
    is_bw = cfg["accent"] == "bw"

    # Base background
    img = Image.new('RGB', (W, H), BG_DARK)
    draw = ImageDraw.Draw(img)

    # Draw subtle gradient — darker at edges, slightly lighter center
    for y in range(H):
        factor = 1.0 - 0.3 * abs(y - H/2) / (H/2)
        for x in range(0, W, 4):
            edge_factor = 1.0 - 0.2 * abs(x - W/2) / (W/2)
            combined = factor * edge_factor
            r = int(BG_DARK[0] * combined)
            g = int(BG_DARK[1] * combined)
            b = int(BG_DARK[2] * combined)
            draw.line([(x, y), (x+3, y)], fill=(r, g, b))

    # Grid lines
    if is_bw:
        draw_grid_lines(draw, (200, 200, 200), alpha_factor=0.08)
    else:
        draw_grid_lines(draw, LIME, alpha_factor=0.06)

    # Diagonal lines
    if is_bw:
        draw_diagonal_lines(draw, (200, 200, 200), spacing=150)
    else:
        draw_diagonal_lines(draw, LIME, spacing=150)

    # Central glow
    glow_color = (150, 150, 150) if is_bw else LIME
    cx, cy = W // 2, H // 2

    # Draw glow manually (simple radial)
    glow = Image.new('RGB', (W, H), (0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    for radius in range(350, 0, -10):
        alpha_factor = (350 - radius) / 350 * 0.3
        if is_bw:
            gc = tuple(int(180 * alpha_factor) for _ in range(3))
        else:
            gc = tuple(int(c * alpha_factor) for c in LIME_DIM)
        glow_draw.ellipse(
            [cx - radius, cy - radius, cx + radius, cy + radius],
            fill=gc
        )
    glow_blurred = glow.filter(ImageFilter.GaussianBlur(radius=80))
    img = Image.blend(img, glow_blurred, 0.6)
    draw = ImageDraw.Draw(img)

    # Concentric circles
    draw_circles(draw, cx, cy, glow_color)

    # Corner marks
    draw_corner_marks(draw, glow_color)

    # Horizontal rule lines
    for y_pos in [H // 3, 2 * H // 3]:
        line_c = tuple(int(c * 0.2) for c in glow_color)
        draw.line([(80, y_pos), (W - 80, y_pos)], fill=line_c, width=1)

    # Bottom bar
    bar_y = H - 70
    bar_bg = tuple(int(c * 0.15) for c in glow_color)
    draw.rectangle([(0, bar_y), (W, H)], fill=bar_bg)
    bar_line_c = tuple(int(c * 0.5) for c in glow_color)
    draw.line([(0, bar_y), (W, bar_y)], fill=bar_line_c, width=1)

    # Side accent lines
    for x_offset in [60, 62]:
        draw.line([(x_offset, 80), (x_offset, H - 80)], fill=bar_line_c, width=1)
    for x_offset in [W - 60, W - 62]:
        draw.line([(x_offset, 80), (x_offset, H - 80)], fill=bar_line_c, width=1)

    # === TEXT ===
    # Odin Lab mark (top-left)
    font_small = get_font(14)
    font_med = get_font(18)
    font_large = get_font(52)
    font_xlarge = get_font(80)
    font_icon = get_font(100)
    font_sub = get_font(22)

    label_c = glow_color
    dim_c = tuple(int(c * 0.5) for c in glow_color)

    # Top-left: ODIN LAB CALGARY
    draw.text((80, 38), "ODIN LAB CALGARY", font=font_small, fill=dim_c)
    draw.text((80, 56), "Functional Health & Wellness", font=font_small, fill=tuple(int(c * 0.3) for c in glow_color))

    # Top-right: filename
    filename = cfg["filename"]
    draw.text((W - 80, 38), filename, font=font_small, fill=dim_c, anchor="ra")
    draw.text((W - 80, 56), "1200 × 800  ·  PLACEHOLDER", font=font_small, fill=tuple(int(c * 0.3) for c in glow_color), anchor="ra")

    # Center icon
    icon_text = cfg["icon"]
    icon_bbox = draw.textbbox((0, 0), icon_text, font=font_icon)
    icon_w = icon_bbox[2] - icon_bbox[0]
    icon_h = icon_bbox[3] - icon_bbox[1]
    icon_x = cx - icon_w // 2
    icon_y = cy - 120 - icon_h // 2
    icon_dim = tuple(int(c * 0.25) for c in glow_color)
    draw.text((icon_x, icon_y), icon_text, font=font_icon, fill=icon_dim)

    # Main label (large)
    label_bbox = draw.textbbox((0, 0), cfg["label"].upper(), font=font_xlarge)
    label_w = label_bbox[2] - label_bbox[0]
    label_x = cx - label_w // 2
    label_y = cy - 20
    draw.text((label_x + 2, label_y + 2), cfg["label"].upper(), font=font_xlarge, fill=(0, 0, 0))
    draw.text((label_x, label_y), cfg["label"].upper(), font=font_xlarge, fill=label_c)

    # Desc line
    desc_bbox = draw.textbbox((0, 0), cfg["desc"].upper(), font=font_sub)
    desc_w = desc_bbox[2] - desc_bbox[0]
    desc_x = cx - desc_w // 2
    desc_y = label_y + 90
    desc_c = tuple(int(c * 0.6) for c in glow_color)
    draw.text((desc_x, desc_y), cfg["desc"].upper(), font=font_sub, fill=desc_c)

    # Sublabel (small, below desc)
    sub_bbox = draw.textbbox((0, 0), cfg["sublabel"], font=font_med)
    sub_w = sub_bbox[2] - sub_bbox[0]
    sub_x = cx - sub_w // 2
    sub_y = desc_y + 36
    sub_c = tuple(int(c * 0.4) for c in glow_color)
    draw.text((sub_x, sub_y), cfg["sublabel"], font=font_med, fill=sub_c)

    # Bottom bar text
    bottom_c = tuple(int(c * 0.7) for c in glow_color)
    draw.text((80, bar_y + 22), "ODIN LAB CALGARY  ·  odincalgary.com", font=font_small, fill=bottom_c)
    draw.text((W - 80, bar_y + 22), "PLACEHOLDER IMAGE  ·  REPLACE WITH GENERATED", font=font_small, fill=tuple(int(c * 0.4) for c in glow_color), anchor="ra")

    # Dot separator in bottom bar center
    draw.text((cx, bar_y + 22), "✦ ODIN LAB ✦", font=font_small, fill=tuple(int(c * 0.5) for c in glow_color), anchor="ma")

    # If BW, desaturate the image
    if is_bw:
        img = img.convert('L').convert('RGB')

    return img


# Generate all images
print(f"Generating {len(images)} placeholder images...")
for cfg in images:
    out_path = os.path.join(OUTPUT_DIR, cfg["filename"])
    try:
        img = create_image(cfg)
        img.save(out_path, "JPEG", quality=92)
        print(f"  ✓ {cfg['filename']}")
    except Exception as e:
        print(f"  ✗ {cfg['filename']}: {e}")

print(f"\nDone. Images saved to: {OUTPUT_DIR}")
