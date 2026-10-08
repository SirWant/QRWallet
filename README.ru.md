# QRWallet

<p align="center">
  <img src="assets/readme/hero.svg" alt="QRWallet — Автономный QuickApp для Xiaomi Smart Band 9 и 10" width="100%">
</p>

<p align="center">
  <sub><strong>VELA QUICKAPP · AMOLED · ОПТИЧЕСКАЯ МАТРИЦА · HYPEROS · ТАКТИЛЬНЫЙ ОТКЛИК</strong></sub>
</p>

<p align="center">
  <a href="README.pt.md">🇵🇹 Português</a>
  · <a href="README.md">🇬🇧 English</a>
  · <a href="README.es.md">🇪🇸 Español</a>
  · <a href="README.zh.md">🇨🇳 简体中文</a>
  · 🇷🇺 <strong>Русский</strong>
</p>

> **Автономный кошелек QR-кодов и быстрых контактов для Xiaomi Smart Band 9 и Smart Band 10 (Xiaomi Vela / HyperOS).**  
> Мгновенный доступ к важным контактам и реквизитам (WhatsApp, Telegram, Instagram, Revolut, GitHub, IBAN, Телефон и Wi-Fi) прямо с вашего запястья. Специальные инвертированные QR-коды для AMOLED-экранов: 100% автономная работа без интернета и без фоновых приложений на смартфоне.

<p align="center">
  <img src="assets/readme/screen-preview.png" alt="QRWallet на экране Xiaomi Smart Band" width="220">
</p>

---

## 01 / ТЕХНИЧЕСКАЯ СВОДКА (AT A GLANCE)

<p align="center">
  <img src="assets/readme/at-a-glance.svg" alt="Архитектура QRWallet в деталях" width="100%">
</p>

---

## 02 / ОСОБЕННОСТИ И ФУНКЦИОНАЛ

### Архитектурные преимущества

- **100% Автономность на браслете**: Работает полностью локально во встроенном движке Xiaomi Vela QuickApp. Смартфон не требуется держать включенным, интернет не нужен.
- **Инвертированная AMOLED-оптика**: Обычные QR-коды с белым фоном на маленьком экране браслета дают сильные паразитные засветы, из-за чего камера смартфона слепнет. QRWallet использует глубокий черный фон `#000000` и белые модули `#FFFFFF`, что экономит батарею браслета и считывается Google Объективом или банковскими приложениями с первой миллисекунды.
- **Идеальная плотность интерфейса**: Каждая карточка откалибрована под `height: 160px`, что дает ровно 3 полноценных пункта на экране без обрезки по краям.
- **Чёткие векторные иконки**: Крупные значки 96×96 px с прозрачностью и системный шрифт `MiSans` 24px обычной толщины (без размытого псевдо-жирного контура).
- **Тактильная виброотдача**: Легкая вибрация при клике по карточке и при возврате свайпом.
- **Сборка без JSC-бага**: Собрано как чистый ES6 JavaScript без флага `--enable-jsc`, вызывающего черный экран на HyperOS 2 / Band 10.

---

## 03 / ДЕТАЛИ ИНТЕРФЕЙСА И ОПТИКИ

<p align="center">
  <img src="assets/readme/icon-grid.png" alt="Включенные иконки высокого разрешения" width="100%">
</p>

<details>
<summary><strong>Техническая таблица характеристик дисплея и оптики</strong></summary>

| Параметр | Значение | Обоснование |
| :--- | :--- | :--- |
| **Целевые устройства** | Xiaomi Smart Band 9 и 10 | Капсульный AMOLED-дисплей |
| **Виртуальный холст** | `192 × 490` (`designWidth: 192`) | Фиксированная сетка без ошибок округления |
| **Шаг списка** | `height: 160px` | Ровно 3 пункта на экране (`490 / 160 ≈ 3.06`) |
| **Размер иконок** | `96 × 96 px` RGBA PNG | Официальный нативный стандарт |
| **Типографика** | `MiSans`, `24px`, `font-weight: normal` | Чёткий векторный шрифт без размытия |
| **Размер QR-кода** | `184 × 184 px` (`margin: 1`) | Максимальная площадь с защитной рамкой в 1 модуль |
| **Цветовая модель** | Тело `#FFFFFF` / Фон `#000000` | Высококонтрастная инвертированная матрица |
| **Сэмплинг** | `NEAREST` (Ближайший сосед) | Максимально резкие границы пикселей |

</details>

---

## 04 / КАСТОМИЗАЦИЯ ЧЕРЕЗ ИИ (ШАГ 1: СНАЧАЛА СОБРАТЬ ПОД СЕБЯ)

> [!NOTE]  
> **Почему сначала кастомизация?** Ни Notify, ни Mi Fitness **не имеют редактора содержимого** на смартфоне. Все ваши контакты, ссылки и картинки вшиваются непосредственно в файл `.rpk` на этапе компиляции перед установкой.

Для настройки приложения под свои контакты используйте файл **[`AI_CUSTOMIZATION_PROMPT.md`](./AI_CUSTOMIZATION_PROMPT.md)**.

<details>
<summary><strong>Шаблон промпта для ИИ (Скопировать и вставить)</strong></summary>

Скопируйте текст ниже и отправьте любой нейросети (**ChatGPT, Claude, Gemini, Antigravity, Cursor**):

```text
You are an expert developer specializing in the Xiaomi Vela QuickApp framework (for Xiaomi Smart Band 9 & 10).
I have cloned the "QRWallet" repository and want to customize the shortcuts, icons, and QR codes with my own data:

My Data:
- WhatsApp: [https://wa.me/XXXXXXXXXXX]
- Telegram: [https://t.me/yourusername]
- Instagram: [https://instagram.com/yourusername]
- Revolut: [https://revolut.me/yourusername]
- GitHub: [https://github.com/yourusername]
- IBAN: [PT50000000000000000000000]
- Phone: [tel:+XXXXXXXXXXX]
- Wi-Fi: [WIFI:S:MyNetwork;T:WPA;P:MySecretPassword;;]

Technical Constraints:
1. QR Codes: 184x184 px, inverted dark mode (#000000 background, #FFFFFF modules), margin=1, NEAREST resampling, saved to src/common/qrcodes/<name>_dark.png.
2. Icons: 96x96 px RGBA PNG, saved to src/common/icons/<name>.png.
3. Layout: height: 160px, font-size: 24px, font-weight: normal (MiSans).
4. Build: npm run release (without --enable-jsc). Increment versionCode in manifest.json.
```

</details>

---

## 05 / ЛОКАЛЬНАЯ СБОРКА ЧЕРЕЗ ТЕРМИНАЛ

Для тех, кто предпочитает локальный запуск через скрипт:

```bash
# 1. Впишите свои контакты в generate_assets.py
nano generate_assets.py

# 2. Запустите генератор (создаст QR-коды и сконвертирует SVG)
python3 generate_assets.py

# 3. Скомпилируйте релизный пакет
npm run release
```

Готовый файл `.rpk` появится в папке:  
`dist/com.custom.qrwallet.release.1.0.0.rpk`

---

## 06 / ИНСТРУКЦИЯ ПО УСТАНОВКЕ (ШАГ 2: ПРОШИВКА НА БРАСЛЕТ)

После того как вы собрали свой кастомный пакет `.rpk` (или если хотите протестировать шаблон по умолчанию из **[Releases](https://github.com/mastermaiolo/QRWallet/releases)**):

### Способ 1: Через Notify for Xiaomi (Рекомендуется)

1. Возьмите готовый файл `dist/com.custom.qrwallet.release.1.0.0.rpk` (или скачайте из Releases).
2. Перенесите файл `.rpk` в память смартфона.
3. Откройте **Notify for Xiaomi** → **Настройки / Устройство** → **Сторонние приложения** (*Third-party app*).
4. Нажмите **Загрузить файл .rpk** и выберите скачанный файл.
5. Дождитесь окончания передачи по Bluetooth.

> [!IMPORTANT]
> **Очистка кэша**: Если на браслете уже была установлена старая версия, **обязательно удалите её** через Notify или меню приложений браслета перед установкой новой. Это заставит систему Vela очистить кэш старых иконок из флеш-памяти.

### Способ 2: Через модифицированный Mi Fitness

1. Откройте мод Mi Fitness на телефоне.
2. Перейдите в скрытое отладочное меню (`ThirdAppDebugFragment`).
3. Введите имя пакета: `com.custom.qrwallet`.
4. Нажмите **Install third app** и выберите `.rpk`.

---

## 07 / СТРУКТУРА ПРОЕКТА

```text
QRWallet/
├── AI_CUSTOMIZATION_PROMPT.md    # Готовый промпт для нейросетей (на английском)
├── generate_assets.py            # Локальный скрипт сборки ресурсов
├── icon/                         # Векторные SVG-иконки (96x96)
├── icon2.png                     # Иконка кошелька для меню (128x128)
├── package.json                  # Скрипты компиляции (aiot-toolkit 2.x)
├── sign/                         # Ключи для подписи пакета
└── src/
    ├── manifest.json             # Манифест приложения и разрешения
    ├── app.ux                    # Жизненный цикл приложения
    ├── common/
    │   ├── icons/                # PNG-иконки 96x96 px
    │   ├── qrcodes/              # Инвертированные QR-коды 184x184 px
    │   └── logo.png              # Значок для списка приложений браслета
    └── pages/
        ├── index/index.ux        # Главный список карточек (160px)
        └── qrcode/qrcode.ux      # Полноэкранный просмотрщик QR с вибрацией
```

---

## 08 / РЕШЕНИЕ ПРОБЛЕМ

| Симптом | Причина | Решение |
| :--- | :--- | :--- |
| **Черный экран при запуске** | Включена компиляция JSC | Убедитесь, что `--enable-jsc` выключен (`false`). |
| **Отображаются старые иконки** | Кэш во флеш-памяти браслета | Полностью удалите приложение с браслета перед установкой новой версии. |
| **Текст карточек мыльный/с обводкой** | Включен `bold` в CSS | Используйте `font-weight: normal; font-size: 24px;`. |
| **Телефон не считывает QR-код** | Размытый скейлинг или белый фон | Соблюдайте размер 184×184 px, режим `NEAREST` и фон `#000000`. |

---

## 09 / АВТОРСТВО И ЛИЦЕНЗИЯ

- **Автор и архитектура систем**: [mastermaiolo](https://github.com/mastermaiolo)
- **Фирменная подпись**: **MAIOLO / SYSTEMS LAB** · **食**
- **Лицензия**: [MIT](LICENSE) — Свободное использование, модификация и распространение.
