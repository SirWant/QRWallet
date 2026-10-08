# QRWallet

<p align="center">
  <img src="assets/readme/hero.svg" alt="QRWallet — QuickApp autónoma para Xiaomi Smart Band 9 y 10" width="100%">
</p>

<p align="center">
  <sub><strong>VELA QUICKAPP · AMOLED · MATRIZ ÓPTICA DE HARDWARE · HYPEROS · HÁPTICA</strong></sub>
</p>

<p align="center">
  <a href="README.pt.md">🇵🇹 Português</a>
  · <a href="README.md">🇬🇧 English</a>
  · 🇪🇸 <strong>Español</strong>
  · <a href="README.zh.md">🇨🇳 简体中文</a>
  · <a href="README.ru.md">🇷🇺 Русский</a>
</p>

> **Billetera autónoma de códigos QR y accesos directos para Xiaomi Smart Band 9 y Smart Band 10 (Xiaomi Vela / HyperOS).**  
> Acceso directo a tus credenciales digitales esenciales (WhatsApp, Telegram, Instagram, Revolut, GitHub, IBAN, Teléfono y Wi-Fi) renderizadas como códigos QR invertidos de grado óptico para pantallas AMOLED directamente en tu muñeca. Cero dependencia de internet. Cero servicio en segundo plano en el móvil.

<p align="center">
  <img src="assets/readme/screen-preview.png" alt="QRWallet ejecutándose en Xiaomi Smart Band" width="220">
</p>

---

## 01 / VISTA GENERAL (AT A GLANCE)

<p align="center">
  <img src="assets/readme/at-a-glance.svg" alt="Arquitectura técnica de QRWallet" width="100%">
</p>

---

## 02 / CAPACIDADES

### Aspectos Arquitectónicos

- **100% Autónomo en la Pulsera**: Se ejecuta de forma nativa en el motor QuickApp de Xiaomi Vela en el microcontrolador. No requiere que el teléfono esté conectado ni necesita acceso a internet.
- **Óptica Invertida para AMOLED**: Los códigos QR convencionales con fondo blanco provocan destellos en pantallas OLED pequeñas. QRWallet utiliza un fondo negro puro `#000000` con módulos blancos `#FFFFFF`, ahorrando batería y permitiendo una lectura instantánea con Google Lens, iPhone o apps bancarias.
- **Densidad Ergonómica Nativa**: Calibrado a `height: 160px` por elemento, mostrando con precisión 3 tarjetas por pantalla en el panel de 490px/520px sin cortes visuales molestos.
- **Iconos Vectoriales Reales**: Iconos nítidos de 96×96 px emparejados con la tipografía nativa del sistema `MiSans` a 24px regular (sin distorsión de falso negrito).
- **Respuesta Háptica**: Microvibración al pulsar un atajo y al deslizar hacia atrás.
- **Estabilidad Sin Bytecode**: Empaquetado estrictamente en JavaScript estándar (ES6). Omite la compilación `--enable-jsc`, evitando la pantalla negra en HyperOS 2 / Band 10.

---

## 03 / ANATOMÍA ÓPTICA Y DE PANTALLA

<p align="center">
  <img src="assets/readme/icon-grid.png" alt="Iconos de alta fidelidad incluidos" width="100%">
</p>

<details>
<summary><strong>Especificaciones Técnicas de Hardware y Matriz Óptica</strong></summary>

| Parámetro | Especificación | Propósito / Razón |
| :--- | :--- | :--- |
| **Dispositivos Objetivo** | Xiaomi Smart Band 9 y 10 | Pantalla OLED tipo cápsula |
| **Lienzo Virtual** | `192 × 490` (`designWidth: 192`) | Elimina errores de redondeo en píxeles flotantes |
| **Ritmo de Lista** | `height: 160px` | Exactamente 3 elementos visibles por pantalla |
| **Geometría de Iconos** | `96 × 96 px` RGBA PNG | Tamaño estándar oficial |
| **Tipografía** | `MiSans`, `24px`, `font-weight: normal` | Fuente nativa sin bordes borrosos |
| **Marco del QR** | `184 × 184 px` (`margin: 1`) | Llena el ancho manteniendo margen de lectura seguro |
| **Modelo de Color** | Frente `#FFFFFF` / Fondo `#000000` | Matriz invertida de alto contraste para AMOLED |
| **Interpolación** | `NEAREST` (Vecino más cercano) | Cuadrados nítidos sin desenfoque |

</details>

---

## 04 / PERSONALIZACIÓN CON IA (PASO 1: PERSONALIZAR Y COMPILAR)

> [!NOTE]  
> **¿Por qué personalizar primero?** Ni Notify ni Mi Fitness incluyen un editor gráfico para cambiar el contenido de QuickApps en el móvil. **Todas las credenciales e iconos se compilan directamente en el binario `.rpk` antes de instalar.**

Usa **[`AI_CUSTOMIZATION_PROMPT.md`](./AI_CUSTOMIZATION_PROMPT.md)** para personalizar el proyecto con cualquier IA en segundos:

<details>
<summary><strong>Plantilla de Prompt para IA (Copiar y Pegar)</strong></summary>

Copia el bloque y envíalo a tu IA favorita (**ChatGPT, Claude, Gemini, Antigravity, Cursor**):

```text
You are an expert developer specializing in the Xiaomi Vela QuickApp framework (for Xiaomi Smart Band 9 & 10).
I have cloned the "QRWallet" repository and want to customize the shortcuts, icons, and QR codes with my own data:

My Data:
- WhatsApp: [https://wa.me/34612345678]
- Telegram: [https://t.me/yourusername]
- Instagram: [https://instagram.com/yourusername]
- Revolut: [https://revolut.me/yourusername]
- GitHub: [https://github.com/yourusername]
- IBAN: [ES0000000000000000000000]
- Phone: [tel:+34612345678]
- Wi-Fi: [WIFI:S:MyNetwork;T:WPA;P:MySecretPassword;;]

Technical Constraints:
1. QR Codes: 184x184 px, inverted dark mode (#000000 background, #FFFFFF modules), margin=1, NEAREST resampling, saved to src/common/qrcodes/<name>_dark.png.
2. Icons: 96x96 px RGBA PNG, saved to src/common/icons/<name>.png.
3. Layout: height: 160px, font-size: 24px, font-weight: normal (MiSans).
4. Build: npm run release (without --enable-jsc). Increment versionCode in manifest.json.
```

</details>

### 🎨 Directrices para Iconos y Accesos Personalizados
- **PNG Transparente / SVG Vectorial**: Utiliza siempre iconos con **fondo 100% transparente (RGBA)** o archivos SVG vectoriales en la carpeta `icon/`. Debido a que la pantalla de la pulsera es AMOLED negro puro (`#000000`), los iconos con recuadros blancos o sólidos rompen la estética visual.
- **Resolución Nativa 96 × 96 px**: Las imágenes de alta resolución (ej. 512×512) colocadas en `src/common/icons/` se redimensionarán y normalizarán automáticamente a 96×96 RGBA al ejecutar `python3 generate_assets.py`. Mantén una proporción 1:1 con el logo centrado.
- **Añadir / Eliminar Accesos**: Puedes añadir cualquier servicio (Discord, Spotify, Pix, Twitch) o eliminar los que no necesites editando `APP_ITEMS` en `src/pages/index/index.ux` y `QR_ITEMS` en `generate_assets.py`.
- **Formatos URI**: Consulta [`AI_CUSTOMIZATION_PROMPT.md`](./AI_CUSTOMIZATION_PROMPT.md) para ver la guía completa de esquemas de datos (`tel:+`, `https://wa.me/`, `WIFI:S:...;T:WPA;P:...;;`, etc.).

---

## 05 / AUTOMATIZACIÓN LOCAL (TERMINAL)

Para generar los archivos localmente desde la terminal:

```bash
# 1. Edita tus credenciales en generate_assets.py
nano generate_assets.py

# 2. Ejecuta el generador automático
python3 generate_assets.py

# 3. Compila el paquete para la pulsera
npm run release
```

El archivo final `.rpk` se guardará en:  
`dist/com.custom.qrwallet.release.1.0.0.rpk`

---

## 06 / INSTALACIÓN EN LA PULSERA (PASO 2: INSTALAR EL .RPK)

Una vez compilado tu `.rpk` personalizado (o para probar la versión de muestra de **[Releases](https://github.com/mastermaiolo/QRWallet/releases)**):

### Método Rápido (Notify for Xiaomi — Recomendado)

1. Localiza tu paquete compilado en `dist/com.custom.qrwallet.release.1.0.0.rpk` (o descárgalo de Releases).
2. Transfiere el archivo `.rpk` a tu teléfono móvil.
3. Abre **Notify for Xiaomi** → **Ajustes / Dispositivo** → **Aplicación de terceros**.
4. Pulsa en **Subir archivo .rpk** y selecciona el archivo.
5. Espera a que termine la sincronización Bluetooth.

> [!IMPORTANT]
> **Limpieza de Caché**: Si ya tenías instalada una versión anterior, **desinstálala primero** desde Notify o desde el reloj antes de flashear la nueva versión, para que la pulsera borre la caché de iconos antiguos de la memoria flash.

### Método Alternativo (Mi Fitness Modificado)

1. Abre Mi Fitness modificado en el móvil emparejado.
2. Accede a la pantalla de depuración (`ThirdAppDebugFragment`).
3. Ingresa el nombre de paquete: `com.custom.qrwallet`.
4. Pulsa **Install third app** y selecciona el archivo `.rpk`.

---

## 07 / ESTRUCTURA DEL PROYECTO

```text
QRWallet/
├── AI_CUSTOMIZATION_PROMPT.md    # Instrucciones para IA (en inglés)
├── generate_assets.py            # Script automático de generación
├── icon/                         # Vectores SVG originales (96x96)
├── icon2.png                     # Icono de la aplicación (128x128)
├── package.json                  # Scripts de compilación
├── sign/                         # Claves criptográficas de firma
└── src/
    ├── manifest.json             # Manifiesto y permisos
    ├── app.ux                    # Ciclo de vida
    ├── common/
    │   ├── icons/                # Iconos PNG de 96x96 px
    │   ├── qrcodes/              # Códigos QR invertidos de 184x184 px
    │   └── logo.png              # Icono mostrado en la lista de apps
    └── pages/
        ├── index/index.ux        # Lista de accesos directos
        └── qrcode/qrcode.ux      # Visor de código QR en pantalla completa
```

---

## 08 / SOLUCIÓN DE PROBLEMAS

| Síntoma | Causa | Solución |
| :--- | :--- | :--- |
| **Pantalla negra al abrir** | Compilación con JSC activada | Asegúrate de que `--enable-jsc` esté desactivado (`false`). |
| **Aparecen los iconos viejos** | Caché interna de la pulsera | Desinstala la app antes de enviar la nueva versión. |
| **Texto borroso o pixelado** | Falso negrito en CSS | Usa `font-weight: normal; font-size: 24px;`. Nunca uses `bold`. |
| **El móvil no lee el QR** | Escala errónea o fondo blanco | Mantén 184×184 px con `NEAREST` y fondo puro `#000000`. |

---

## 09 / CRÉDITOS Y LICENCIA

- **Autor / Arquitectura**: [mastermaiolo](https://github.com/mastermaiolo)
- **Firma de Estudio**: **MAIOLO / SYSTEMS LAB** · **食**
- **Licencia**: [MIT](LICENSE) — Libre para uso personal, modificación y distribución.
