# 🤖 Artificial Intelligence Customization Prompt (AI Prompt)

> **Why does this prompt exist?**  
> Neither **Notify for Xiaomi** nor **Mi Fitness mods** feature an in-app graphical interface to modify the contents of third-party watch applications on your smartphone.  
> Inside the **Xiaomi Vela / QuickApp** architecture, all shortcuts, icons, and QR code assets are **compiled directly into the binary distribution package (`.rpk`)**.  
> To personalize your shortcuts, contact links, and credentials, simply copy the prompt below into any AI assistant (**ChatGPT, Claude, Gemini, Antigravity, Cursor, etc.**).

---

## 📋 Copy and Paste the Prompt Below into Your AI Assistant:

```text
You are an expert developer specializing in the Xiaomi Vela QuickApp framework (for Xiaomi Smart Band 9 and 10).
I have cloned the "QRWallet" repository and want to customize the shortcuts, brand icons, and AMOLED QR codes with my personal credentials.

Here is my personal data for each card:
- WhatsApp: [insert your link or phone number, e.g., https://wa.me/351912345678]
- Telegram: [insert your username link, e.g., https://t.me/yourusername]
- Instagram: [insert your profile URL, e.g., https://instagram.com/yourusername]
- Revolut: [insert your payment handle, e.g., https://revolut.me/yourusername]
- GitHub: [insert your GitHub profile, e.g., https://github.com/yourusername]
- IBAN: [insert your plain bank account number without spaces, e.g., PT50000000000000000000000]
- Phone: [insert full international dialer URI, e.g., tel:+351912345678]
- Wi-Fi: [insert credentials URI, e.g., WIFI:S:MyNetworkSSID;T:WPA;P:MySecretPassword;;]

Please perform the following tasks adhering strictly to the Xiaomi Smart Band hardware specifications:

1. QR CODE OPTICAL SPECIFICATIONS:
   - Dimensions: Exactly 184 x 184 px (fits the 192px viewport with a 4px safety gutter).
   - Inverted AMOLED Mode: Pure BLACK background (#000000) and pure WHITE squares (#FFFFFF).
   - Quiet Zone Margin: Exactly 1 module (margin=1).
   - Resampling Algorithm: NEAREST (nearest neighbor) to maintain razor-sharp pixel edges without interpolation blur.
   - Destination: Save to 'src/common/qrcodes/<name>_dark.png'.

2. LIST ICON SPECIFICATIONS:
   - Dimensions: Exactly 96 x 96 px.
   - Format: RGBA PNG with alpha transparency.
   - Vector Conversion: Render SVGs directly to 96x96 px preserving brand colors and gradients.
   - Destination: Save to 'src/common/icons/<name>.png'.

3. USER INTERFACE (src/pages/index/index.ux):
   - Card height: Exactly 160px (.app-item { height: 160px; }) ensuring 3 cards per screen on the 490px/520px capsule display.
   - Icon CSS size: width: 96px; height: 96px;.
   - Typography: color: #ffffff; font-size: 24px; font-weight: normal; margin-top: 6px;.
     (CRITICAL: NEVER use 'font-weight: bold', as the Vela rendering engine introduces ugly faux-bold stroke artifacts over the native MiSans font).

4. MANIFEST AND COMPILATION:
   - In 'src/manifest.json', increment 'versionCode' and 'versionName' (mandatory to bypass band-side flash cache).
   - Build command: Run 'npm run release' (invoking 'aiot release').
   - CRITICAL COMPILATION RULE: NEVER enable '--enable-jsc' (JSC bytecode causes an immediate black-screen crash on Xiaomi HyperOS 2 / Band 10). Keep standard text ES6 JavaScript.

Update the project files or execute 'python3 generate_assets.py' with my credentials and compile the final .rpk package in the dist/ folder.
```

---

## 🎨 Guidelines for Custom Icons & Brand Logos

To ensure your shortcuts look as clean as native Xiaomi watch apps:

1. **Format & Transparency (Mandatory)**:
   - Always use **PNG with an alpha channel (RGBA)** or **vector SVG**.
   - **Background must be 100% transparent**. Because the Xiaomi Smart Band uses a pitch-black AMOLED display (`#000000`), icons with solid white or grey bounding boxes look awkward. Transparent icons blend seamlessly into the screen.
2. **Resolution & Sharpness**:
   - The native icon display size on the watch is **96 × 96 px**.
   - For best sharpness, use high-resolution source images (e.g., 256×256 or 512×512 px) and downscale using LANCZOS or let `generate_assets.py` auto-normalize them.
   - Maintain a square **1:1 aspect ratio** with the brand glyph or symbol centered.
3. **Where to place custom icons**:
   - **Vector icons**: Save your `.svg` files into the `icon/` directory (e.g., `icon/discord.svg`).
   - **Raster icons**: Save your `.png` files directly into `src/common/icons/` (e.g., `src/common/icons/discord.png`).

---

## 📝 How to Add, Rename, or Remove Shortcuts

You are not limited to the default 8 services! You can add Discord, LinkedIn, Spotify, Pix, Twitch, or remove anything you don't need:

### Step 1: Update the User Interface (`src/pages/index/index.ux`)
Open `src/pages/index/index.ux` and locate the `APP_ITEMS` array (around line 67). Edit, add, or delete entries:

```javascript
const APP_ITEMS = [
  {
    id: "discord",
    title: "Discord",
    icon: "/common/icons/discord.png",
    qrDark: "/common/qrcodes/discord_dark.png"
  },
  {
    id: "spotify",
    title: "Spotify",
    icon: "/common/icons/spotify.png",
    qrDark: "/common/qrcodes/spotify_dark.png"
  }
]
```

### Step 2: Update the Asset Generator (`generate_assets.py`)
In `generate_assets.py`, update `QR_ITEMS` with matching keys and your desired payload:

```python
QR_ITEMS = {
    "discord": "https://discord.gg/yourserver",
    "spotify": "https://open.spotify.com/user/yourprofile",
}
```

---

## 📋 QR Code Payload Cheat Sheet

Use these exact URI formats when defining your QR codes to trigger the phone's native handlers immediately:

| Shortcut Type | Format / URI Scheme | Example Value |
| :--- | :--- | :--- |
| **Web Link / Social** | Standard URL | `https://instagram.com/myusername` |
| **WhatsApp Direct** | `https://wa.me/<country_code><number>` | `https://wa.me/351912345678` |
| **Telegram Profile** | `https://t.me/<username>` | `https://t.me/myusername` |
| **Phone Dialer** | `tel:<country_code><number>` | `tel:+351912345678` |
| **Wi-Fi Auto-Join** | `WIFI:S:<SSID>;T:<WPA\|WEP\|nopass>;P:<password>;;` | `WIFI:S:MyHome;T:WPA;P:Secret123;;` |
| **Email Message** | `mailto:<email>?subject=<text>` | `mailto:contact@example.com` |
| **IBAN / Bank Account** | Plain alphanumeric text without spaces | `PT50000000000000000000000` |
| **Cryptocurrency** | `<coin>:<wallet_address>` | `bitcoin:1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa` |

---

## 🛠️ Local Terminal Automation (`generate_assets.py`)

If you prefer to generate your assets locally in the terminal:

1. **Install dependencies (First time only)**:
   ```bash
   npm install
   pip install Pillow
   ```
2. **Edit your credentials**:
   Open `generate_assets.py` and modify `QR_ITEMS`.
3. **Run the generator**:
   ```bash
   python3 generate_assets.py
   ```
   *(This automatically generates inverted AMOLED QR codes and normalizes all icons to 96×96 RGBA PNG)*.
4. **Compile the release package**:
   ```bash
   npm run release
   ```
   The signed `.rpk` will be generated in `dist/com.custom.qrwallet.release.1.0.0.rpk`.

---

## 📲 How to Install onto the Xiaomi Smart Band

### Method 1: Via "Notify for Xiaomi" (Recommended)
1. Send the newly compiled `.rpk` file from `dist/` to your smartphone (via Telegram, WhatsApp, email, or USB).
2. Open the **Notify for Xiaomi** app.
3. Go to **Settings / Device**.
4. Select **Third-party app** (*Aplicativo de terceiros*).
5. Tap **Upload .rpk file** and choose the package.
6. Wait for the Bluetooth file transfer to complete.

> 💡 **Important Cache Rule**: If you already have an older version installed on the band, **uninstall it first** via Notify or through the band's application menu before uploading the new `.rpk`. This clears the cached icon assets from the band's internal flash memory.

### Method 2: Via Modded Mi Fitness (Developer Menu)
1. Open the modded Mi Fitness app on your paired smartphone.
2. Launch the hidden developer debug activity (`ThirdAppDebugFragment`).
3. Enter the package name: `com.custom.qrwallet`.
4. Tap **Install third app** and choose the `.rpk` file.
