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

## 🛠️ Local Terminal Automation (`generate_assets.py`)

If you prefer to generate your assets locally in the terminal without using an AI chat interface:

1. Open `generate_assets.py`.
2. Edit the `QR_ITEMS` dictionary with your credentials:
   ```python
   QR_ITEMS = {
       "whatsapp": "https://wa.me/351912345678",
       "telegram": "https://t.me/yourusername",
       "instagram": "https://instagram.com/yourusername",
       "revolut": "https://revolut.me/yourusername",
       "github": "https://github.com/yourusername",
       "iban": "PT50000000000000000000000",
       "phone": "tel:+351912345678",
       "wifi": "WIFI:S:MyNetwork;T:WPA;P:MyPassword;;",
   }
   ```
3. Run the automated script:
   ```bash
   python3 generate_assets.py
   ```
4. Compile the application:
   ```bash
   npm run release
   ```
5. Your signed `.rpk` will be generated in `dist/`.

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
