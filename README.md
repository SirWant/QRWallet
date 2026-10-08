# QRWallet

<p align="center">
  <img src="assets/readme/hero.svg" alt="QRWallet — Autonomous QuickApp for Xiaomi Smart Band 9 & 10" width="100%">
</p>

<p align="center">
  <sub><strong>VELA QUICKAPP · AMOLED · HARDWARE OPTICAL MATRIX · HYPEROS · HAPTICS</strong></sub>
</p>

<p align="center">
  <a href="README.pt.md">🇵🇹 Português</a>
  · 🇬🇧 <strong>English</strong>
  · <a href="README.es.md">🇪🇸 Español</a>
  · <a href="README.zh.md">🇨🇳 简体中文</a>
  · <a href="README.ru.md">🇷🇺 Русский</a>
</p>

> **Autonomous QR Code & Shortcut Wallet for Xiaomi Smart Band 9 and Smart Band 10 (Xiaomi Vela / HyperOS).**  
> Direct access to your essential digital credentials (WhatsApp, Telegram, Instagram, Revolut, GitHub, IBAN, Phone Dialer, and Wi-Fi Access) rendered as optical-grade inverted AMOLED QR codes right from your wrist. Zero internet dependency. Zero phone companion daemon.

<p align="center">
  <img src="assets/readme/screen-preview.png" alt="QRWallet running on Xiaomi Smart Band" width="220">
</p>

---

## 01 / AT A GLANCE

<p align="center">
  <img src="assets/readme/at-a-glance.svg" alt="QRWallet technical architecture at a glance" width="100%">
</p>

---

## 02 / CAPABILITIES

### Architectural Highlights

- **100% Autonomous Firmware Execution**: Runs natively within the Xiaomi Vela QuickApp engine on the band's micro-controller. No background daemon on the phone and zero internet required during operation.
- **Inverted AMOLED Optics**: Standard white-background QR codes cause glare and light leakage on wrist displays. QRWallet uses pure `#000000` deep black backgrounds with pure `#FFFFFF` modules, maximizing OLED battery life and triggering camera scanners (Google Lens, iOS Camera, Bank Apps) instantly.
- **Native Ergonomic Density**: Calibrated at `height: 160px` per card, precisely presenting 3 items per screen on the 490px/520px capsule display without awkward half-item cutoffs.
- **True Vector Glyphs**: High-fidelity 96×96 px brand assets paired with the unadulterated native `MiSans` typography (rendered at 24px regular weight without faux-bold stroke deformation).
- **Haptic Confirmation**: Micro-vibration pulses triggered on card selection and route dismissal.
- **Zero-Bytecode Stability**: Packaged strictly as standard ES6 JavaScript. Bypasses the `--enable-jsc` bytecode compiler flag that causes black-screen crashes on HyperOS 2 / Band 10.

---

## 03 / DISPLAY & OPTICAL ANATOMY

<p align="center">
  <img src="assets/readme/icon-grid.png" alt="Included high-fidelity icons" width="100%">
</p>

<details>
<summary><strong>Hardware & Optical Matrix Specifications</strong></summary>

| Parameter | Specification | Purpose / Rationale |
| :--- | :--- | :--- |
| **Target Devices** | Xiaomi Smart Band 9 & 10 | Capsule OLED form-factor |
| **Virtual Canvas** | `192 × 490` (`designWidth: 192`) | Fixed coordinate raster; eliminates float rounding artifacts |
| **List Rhythm** | `height: 160px` | 3 cards visible per viewport (`490 / 160 ≈ 3.06`) |
| **Icon Geometry** | `96 × 96 px` RGBA PNG | Native standard asset dimension |
| **Typography** | `MiSans`, `24px`, `font-weight: normal` | Native system vector font; avoids faux-bold stroke aliasing |
| **QR Frame** | `184 × 184 px` (`margin: 1`) | Fills panel width while preserving the quiet-zone border |
| **Color Model** | Foreground `#FFFFFF` / Background `#000000` | High-contrast inverted optical matrix for AMOLED |
| **Interpolation** | `NEAREST` (Nearest Neighbor) | Crisp, non-interpolated square module edges |

</details>

---

## 04 / AI CUSTOMIZATION SURFACE (STEP 1: CUSTOMIZE & BUILD)

> [!NOTE]  
> **Why customize first?** Neither Notify nor Mi Fitness provides an in-app graphical editor to modify the content of third-party QuickApps on your phone. **All your credentials, links, and icons must be compiled directly into the binary `.rpk` package before installation.**

To customize this repository with your personal links, usernames, and Wi-Fi credentials in seconds, use **[`AI_CUSTOMIZATION_PROMPT.md`](./AI_CUSTOMIZATION_PROMPT.md)**.

<details>
<summary><strong>Copy-Paste AI Prompt Template</strong></summary>

Copy the block below and send it to any AI agent (**ChatGPT, Claude, Gemini, Antigravity, Cursor**):

```text
You are an expert Xiaomi Vela QuickApp developer (for Xiaomi Smart Band 9 & 10).
I have cloned the "QRWallet" repository and want to customize the shortcuts, icons, and QR codes with my own data:

My Data:
- WhatsApp: [https://wa.me/351912345678]
- Telegram: [https://t.me/yourusername]
- Instagram: [https://instagram.com/yourusername]
- Revolut: [https://revolut.me/yourusername]
- GitHub: [https://github.com/yourusername]
- IBAN: [PT50000000000000000000000]
- Phone: [tel:+351912345678]
- Wi-Fi: [WIFI:S:MyNetwork;T:WPA;P:MySecretPassword;;]

Technical Constraints:
1. QR Codes: 184x184 px, inverted dark mode (#000000 background, #FFFFFF modules), margin=1, NEAREST resampling, saved to src/common/qrcodes/<name>_dark.png.
2. Icons: 96x96 px RGBA PNG, saved to src/common/icons/<name>.png.
3. Layout: height: 160px, font-size: 24px, font-weight: normal (MiSans).
4. Build: npm run release (without --enable-jsc). Increment versionCode in manifest.json.
```

</details>

### 🎨 Guidelines for Custom Icons & Shortcuts
- **Transparent PNG / Vector SVG**: Always use icons with a **100% transparent background (RGBA)** or vector SVGs in `icon/`. Because the band has a pitch-black AMOLED screen (`#000000`), icons with white or solid bounding boxes look unnatural.
- **Native 96 × 96 px Resolution**: High-resolution icons (e.g. 512×512) placed into `src/common/icons/` will be automatically resized and normalized to 96×96 RGBA when running `python3 generate_assets.py`. Maintain a 1:1 aspect ratio with centered glyphs.
- **Add / Remove Shortcuts**: You can add any service (Discord, Spotify, Pix, Twitch) or remove entries by updating `APP_ITEMS` in `src/pages/index/index.ux` and `QR_ITEMS` in `generate_assets.py`.
- **Payload Schemes**: Check [`AI_CUSTOMIZATION_PROMPT.md`](./AI_CUSTOMIZATION_PROMPT.md) for full URI formats (`tel:+`, `https://wa.me/`, `WIFI:S:...;T:WPA;P:...;;`, etc.).

---

## 05 / LOCAL AUTOMATION (ALTERNATIVE BUILD PATH)

For local generation without chat interfaces, use the included automation script:

```bash
# 1. Edit your personal credentials in generate_assets.py
nano generate_assets.py

# 2. Run the automated asset generator (renders QR codes + converts SVGs)
python3 generate_assets.py

# 3. Compile the production package
npm run release
```

The resulting signed package will be ready at:  
`dist/com.custom.qrwallet.release.1.0.0.rpk`

---

## 06 / INSTALLATION (STEP 2: FLASH TO BAND)

Once your custom `.rpk` has been compiled (or if you want to test the default template from **[Releases](https://github.com/mastermaiolo/QRWallet/releases)**), install it using one of the two methods below:

### Fast Path (Notify for Xiaomi — Recommended)

1. Locate your compiled package at `dist/com.custom.qrwallet.release.1.0.0.rpk` (or download the pre-built template from Releases).
2. Transfer the `.rpk` file to your mobile phone.
3. Open **Notify for Xiaomi** → Navigate to **Settings / Device** → **Third-party app** (*Aplicativo de terceiros*).
4. Tap **Upload .rpk file** and select the package.
5. Wait for the Bluetooth synchronisation to finish.

> [!IMPORTANT]
> **Cache Invalidation Rule**: If you already have a prior build of the app installed on the band, **uninstall it first** through Notify or on the band's application menu before flashing the new build. This forces Xiaomi Vela to purge cached icons from flash storage.

### Alternative Path (Mi Fitness Modded / Developer Menu)

1. Open the modded Mi Fitness app on your paired smartphone.
2. Launch the hidden developer fragment (`ThirdAppDebugFragment`).
3. Set the package identifier: `com.custom.qrwallet`.
4. Tap **Install third app** and choose the `.rpk` file.

---

## 07 / ARCHITECTURE

```text
QRWallet/
├── AI_CUSTOMIZATION_PROMPT.md    # Reusable AI instructions (in English)
├── generate_assets.py            # Local asset pipeline (qrencode + Pillow + rsvg)
├── icon/                         # Master SVG vector assets (96x96)
├── icon2.png                     # App launcher icon source (128x128)
├── package.json                  # Toolkit scripts (aiot-toolkit 2.x)
├── sign/                         # Debug & Release cryptographic keys
└── src/
    ├── manifest.json             # Manifest definition (permissions, designWidth: 192)
    ├── app.ux                    # Application lifecycle controller
    ├── common/
    │   ├── icons/                # 96x96 px PNG icon assets
    │   ├── qrcodes/              # 184x184 px inverted AMOLED QR codes
    │   └── logo.png              # Launcher badge displayed in band drawer
    └── pages/
        ├── index/index.ux        # Main scrollable card list (160px rhythm)
        └── qrcode/qrcode.ux      # Fullscreen AMOLED QR viewer with haptic back
```

---

## 08 / TROUBLESHOOTING & FAILURE MODES

| Symptom | Cause | Solution |
| :--- | :--- | :--- |
| **Black screen on launch** | Bytecode compilation enabled | Ensure `--enable-jsc` is set to `false` in `package.json` / build options. |
| **Old icons still showing after flash** | Flash memory cache | Rename icon directory (e.g. `icons_v2`) or uninstall the app completely from the band before uploading. |
| **Text looks pixelated / blurry** | Faux-bold stroke | Set `font-weight: normal; font-size: 24px;`. Never use `font-weight: bold` with MiSans on Vela. |
| **QR code won't scan on phone** | Blurry interpolation or white glare | Keep resolution at 184×184 with `NEAREST` resampling and pure `#000000` background. |

---

## 09 / PROVENANCE & LICENCE

- **Author / Systems Architecture**: [mastermaiolo](https://github.com/mastermaiolo)
- **Studio Signature**: **MAIOLO / SYSTEMS LAB** · **食**
- **Licence**: [MIT](LICENSE) — Open for personal customization and distribution.
