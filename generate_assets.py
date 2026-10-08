#!/usr/bin/env python3
"""
Asset Generator for Xiaomi Smart Band QuickApp (Band 9 & 10)
-------------------------------------------------------------
Generates:
1. Inverted dark QR codes (184x184 px) with pure black background (#000000)
2. Crisp 96x96 px icons from SVG/PNG files
3. 128x128 px App launcher icon
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path
from PIL import Image

BASE_DIR = Path(__file__).resolve().parent
QR_DIR = BASE_DIR / "src" / "common" / "qrcodes"
ICON_DIR = BASE_DIR / "src" / "common" / "icons"
SVG_SRC_DIR = BASE_DIR / "icon"
APP_LOGO_PATH = BASE_DIR / "icon2.png"

# =====================================================================
# CONFIGURE YOUR CUSTOM QR CODE DATA HERE:
# =====================================================================
QR_ITEMS = {
    # WhatsApp direct message link: https://wa.me/<country_code><number>
    "whatsapp": "https://wa.me/351912345678",

    # Telegram profile link: https://t.me/<username>
    "telegram": "https://t.me/yourusername",

    # Instagram profile link: https://instagram.com/<username>
    "instagram": "https://instagram.com/yourusername",

    # Revolut payment link: https://revolut.me/<revtag>
    "revolut": "https://revolut.me/yourusername",

    # GitHub profile link: https://github.com/<username>
    "github": "https://github.com/mastermaiolo",

    # Bank IBAN (plain text without spaces for best bank scanner compatibility)
    "iban": "PT50000000000000000000000",

    # Phone direct dialer: tel:+<country_code><number>
    "phone": "tel:+351912345678",

    # Wi-Fi network: WIFI:S:<SSID>;T:<WPA|WEP|nopass>;P:<Password>;;
    "wifi": "WIFI:S:MyHomeWiFi;T:WPA;P:MySuperSecretPassword;;",
}


def ensure_dirs():
    QR_DIR.mkdir(parents=True, exist_ok=True)
    ICON_DIR.mkdir(parents=True, exist_ok=True)


def generate_dark_qr(payload: str, output_path: Path):
    """
    Generates a dark-mode QR code for AMOLED screens:
    - Pure black background (#000000)
    - Pure white foreground (#FFFFFF)
    - Quiet zone border = 1 module
    - Final size = 184x184 px (resampled with NEAREST for sharp pixels)
    """
    tmp_path = Path("/tmp/temp_qr.png")

    # Strategy A: Use system 'qrencode' CLI if available
    if shutil.which("qrencode"):
        cmd = [
            "qrencode",
            "-o", str(tmp_path),
            "-l", "M",
            "-m", "1",
            "-s", "8",
            "--foreground=FFFFFF",
            "--background=000000",
            payload,
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        img = Image.open(tmp_path).convert("RGB")
    else:
        # Strategy B: Fallback to python 'qrcode' library
        try:
            import qrcode
            qr = qrcode.QRCode(
                version=None,
                error_correction=qrcode.constants.ERROR_CORRECT_M,
                box_size=8,
                border=1,
            )
            qr.add_data(payload)
            qr.make(fit=True)
            img = qr.make_image(fill_color="white", back_color="black").convert("RGB")
        except ImportError:
            print("❌ ERROR: Neither 'qrencode' CLI nor 'qrcode' python package found.")
            print("   Install via: sudo pacman -S qrencode  OR  pip install qrcode[pil]")
            sys.exit(1)

    # Scale to exactly 184x184 px for Xiaomi Smart Band screen
    img_184 = img.resize((184, 184), Image.Resampling.NEAREST)
    img_184.save(output_path)
    print(f"  ✓ QR Code: {output_path.name} (184x184 px)")


def convert_icons():
    """Converts SVG files from icon/ directory to 96x96 px PNGs."""
    if not SVG_SRC_DIR.exists():
        print(f"⚠️  No 'icon/' folder found at {SVG_SRC_DIR}. Skipping SVG conversion.")
        return

    svg_files = list(SVG_SRC_DIR.glob("*.svg"))
    if not svg_files:
        print("ℹ️  No SVGs found in 'icon/' folder.")
        return

    print(f"\n🎨 Converting {len(svg_files)} SVGs to 96x96 PNG...")
    has_rsvg = shutil.which("rsvg-convert") is not None

    for svg in svg_files:
        target_png = ICON_DIR / f"{svg.stem}.png"
        if has_rsvg:
            cmd = ["rsvg-convert", "-w", "96", "-h", "96", str(svg), "-o", str(target_png)]
            subprocess.run(cmd, check=True)
            print(f"  ✓ Icon: {target_png.name} (96x96 px)")
        else:
            print(f"⚠️  rsvg-convert not found. Please install librsvg (e.g., sudo pacman -S librsvg).")
            break


def convert_app_logo():
    """Converts icon2.png into src/common/logo.png (128x128 px)."""
    target = BASE_DIR / "src" / "common" / "logo.png"
    if APP_LOGO_PATH.exists():
        im = Image.open(APP_LOGO_PATH)
        im_128 = im.resize((128, 128), Image.Resampling.LANCZOS)
        im_128.save(target)
        print(f"\n📱 App Launcher Logo updated: {target.name} (128x128 px)")


def main():
    print("=" * 60)
    print("🚀 Xiaomi Smart Band QR Code Asset Generator")
    print("=" * 60)
    ensure_dirs()

    print("\n📦 Generating QR Codes (184x184 px, inverted dark mode)...")
    for key, payload in QR_ITEMS.items():
        out_file = QR_DIR / f"{key}_dark.png"
        generate_dark_qr(payload, out_file)

    convert_icons()
    convert_app_logo()

    print("\n✅ All assets generated successfully!")
    print("👉 Now run: npm run release\n")


if __name__ == "__main__":
    main()
