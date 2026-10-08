# QRWallet

<p align="center">
  <img src="assets/readme/hero.svg" alt="QRWallet — 小米手环 9 / 10 离线快捷二维码快应用" width="100%">
</p>

<p align="center">
  <sub><strong>VELA 快应用 · AMOLED · 硬件光学矩阵 · HYPEROS · 触觉震动反馈</strong></sub>
</p>

<p align="center">
  <a href="README.pt.md">🇵🇹 Português</a>
  · <a href="README.md">🇬🇧 English</a>
  · <a href="README.es.md">🇪🇸 Español</a>
  · 🇨🇳 <strong>简体中文</strong>
  · <a href="README.ru.md">🇷🇺 Русский</a>
</p>

> **小米手环 9 及 10（小米 Vela / 澎湃 HyperOS）专属离线快速二维码卡包。**  
> 抬腕立显你的核心数字凭证（微信/WhatsApp、Telegram、Instagram、Revolut、GitHub、银行 IBAN、直接电话拨号及 Wi-Fi 连接码），专为 AMOLED 屏幕优化的反色光学级二维码。零网络依赖，手机无需常驻后台伴侣程序。

<p align="center">
  <img src="assets/readme/screen-preview.png" alt="在小米手环上运行的 QRWallet" width="220">
</p>

---

## 01 / 技术概览 (AT A GLANCE)

<p align="center">
  <img src="assets/readme/at-a-glance.svg" alt="QRWallet 架构总览" width="100%">
</p>

---

## 02 / 核心能力与特性

### 架构亮点

- **手环端 100% 独立脱机运行**：基于手环微控制器内的 Xiaomi Vela 快应用引擎原生运行，手机无需安装或常驻任何后台服务，出门无需手机联网即可随时展示。
- **AMOLED 反色光学矩阵**：传统白底二维码在小尺寸可穿戴屏幕上容易引起强烈反光和边缘溢光，导致手机镜头难以对焦。QRWallet 采用纯黑 `#000000` 背景与高纯白 `#FFFFFF` 码块，不仅大幅降低手环耗电，还能被各种扫码工具（微信扫一扫、Google Lens、iOS 相机）秒级瞬时识别。
- **专为跑道屏定制的人体工学排版**：每张卡片高度严格设定为 `height: 160px`，在 490px/520px 高度屏幕上恰好呈现 3 个完整项目，滑动如丝般顺滑，杜绝半截卡片断层。
- **真矢量高清图标**：96×96 像素独立品牌图标，搭配手环内置 `MiSans` 系统字体（24px 正常字重），杜绝快应用伪粗体带来的毛边与锯齿。
- **线性马达震动**：进入二维码与滑动返回均带触觉微震动反馈。
- **免 JSC 字节码兼容性保障**：采用标准纯文本 ES6 JS 打包，彻底避开 `--enable-jsc` 在 HyperOS 2 / 手环 10 上引发黑屏的底层缺陷。

---

## 03 / 显示规格与光学结构

<p align="center">
  <img src="assets/readme/icon-grid.png" alt="内置高清图标" width="100%">
</p>

<details>
<summary><strong>硬件及光学显示参数详表</strong></summary>

| 参数项 | 规格标准 | 设计意图 / 依据 |
| :--- | :--- | :--- |
| **适配设备** | 小米手环 9 及 10 (Smart Band 9 / 10) | 胶囊跑道屏 OLED 面板 |
| **虚拟画布** | `192 × 490` (`designWidth: 192`) | 整数定点坐标系，杜绝浮点缩放毛刺 |
| **列表节奏** | `height: 160px` | 每屏显示 3 个完整卡片 (`490 / 160 ≈ 3.06`) |
| **图标规格** | `96 × 96 px` RGBA PNG | 原生手环推荐标准尺寸 |
| **文字样式** | `MiSans`, `24px`, `font-weight: normal` | 原生系统矢量字体，无虚假粗体描边 |
| **二维码画幅** | `184 × 184 px` (`margin: 1`) | 贴合屏幕宽度极限同时保留 1 模块安全边距 |
| **颜色模型** | 前景 `#FFFFFF` / 背景 `#000000` | 高对比度 AMOLED 反色光学矩阵 |
| **图像采样** | `NEAREST` (最近邻插值) | 矩阵边缘绝对锐利，杜绝模糊 |

</details>

---

## 04 / 人工智能定制 (步骤一：先定制并打包)

> [!NOTE]  
> **为什么必须先定制再安装？** 官方 Mi Fitness 和 Notify 均**不提供在手机界面动态修改快应用内容的功能**，你的个人凭证、链接与二维码必须在安装前直接编译进 `.rpk` 二进制安装包中。

为了让你无需手写前端代码即可拥有专属版本，请使用 **[`AI_CUSTOMIZATION_PROMPT.md`](./AI_CUSTOMIZATION_PROMPT.md)**。

<details>
<summary><strong>AI 定制提示词模板（可直接复制）</strong></summary>

直接复制下方内容发送给任何大模型助手（**ChatGPT、Claude、Gemini、Antigravity、Cursor**）：

```text
You are an expert developer specializing in the Xiaomi Vela QuickApp framework (for Xiaomi Smart Band 9 & 10).
I have cloned the "QRWallet" repository and want to customize the shortcuts, icons, and QR codes with my own data:

My Data:
- WhatsApp: [https://wa.me/8613800000000]
- Telegram: [https://t.me/yourusername]
- Instagram: [https://instagram.com/yourusername]
- Revolut: [https://revolut.me/yourusername]
- GitHub: [https://github.com/yourusername]
- IBAN: [Your plain account number]
- Phone: [tel:+8613800000000]
- Wi-Fi: [WIFI:S:MyNetwork;T:WPA;P:MySecretPassword;;]

Technical Constraints:
1. QR Codes: 184x184 px, inverted dark mode (#000000 background, #FFFFFF modules), margin=1, NEAREST resampling, saved to src/common/qrcodes/<name>_dark.png.
2. Icons: 96x96 px RGBA PNG, saved to src/common/icons/<name>.png.
3. Layout: height: 160px, font-size: 24px, font-weight: normal (MiSans).
4. Build: npm run release (without --enable-jsc). Increment versionCode in manifest.json.
```

</details>

### 🎨 自定义图标与快捷方式规范
- **透明 RGBA PNG / 矢量 SVG**：务必使用**100% 透明背景 (RGBA)**的 PNG 或保存在 `icon/` 中的 SVG 矢量图。手环采用纯黑 AMOLED 屏幕 (`#000000`)，带有白色或实色矩形底色的图标会严重破坏界面纯净感。
- **原生 96 × 96 像素分辨率**：放入 `src/common/icons/` 的高分辨率图片（如 512×512）在运行 `python3 generate_assets.py` 时会自动缩放并标准化为 96×96 RGBA。请保持 1:1 比例并使主体居中。
- **添加 / 删除快捷方式**：你可以自由增加（例如 Discord, Spotify, 微信, 支付宝）或删除项目，只需同步修改 `src/pages/index/index.ux` 中的 `APP_ITEMS` 和 `generate_assets.py` 中的 `QR_ITEMS`。
- **URI 链接格式**：更多数据格式（`tel:+`, `https://wa.me/`, `WIFI:S:...;T:WPA;P:...;;` 等）详见 [`AI_CUSTOMIZATION_PROMPT.md`](./AI_CUSTOMIZATION_PROMPT.md)。

---

## 05 / 本地脚本生成 (本地终端备用路径)

如果你习惯本地控制台自动化：

```bash
# 1. 在 generate_assets.py 中填入你的个人链接
nano generate_assets.py

# 2. 运行自动化生成脚本（一键生成二维码与转换SVG）
python3 generate_assets.py

# 3. 编译发布包
npm run release
```

编译出的 `.rpk` 文件位于：  
`dist/com.custom.qrwallet.release.1.0.0.rpk`

---

## 06 / 安装指南 (步骤二：刷入手环)

打包出专属的 `.rpk` 后（或如果想先体验 **[Releases](https://github.com/mastermaiolo/QRWallet/releases)** 中的演示模板）：

### 推荐路径（使用 Notify for Xiaomi）

1. 找到编译好的安装包 `dist/com.custom.qrwallet.release.1.0.0.rpk`（或从 Releases 下载）。
2. 将 `.rpk` 文件传至手机存储中。
3. 打开手机上的 **Notify for Xiaomi** App → 进入 **设置 / 设备** → **第三方应用 (Third-party app)**。
4. 点击 **加载 .rpk 文件** 并选择该安装包。
5. 等待蓝牙传输完毕即可在手环应用列表打开。

> [!IMPORTANT]
> **缓存刷新注意事项**：若之前已安装过旧版，**请务必先在 Notify 或手环应用列表卸载旧版**，再上传新版安装包。这能强制 Vela 系统清空 Flash 闪存中的图标缓存。

### 备用路径（使用 Mi Fitness 修改版开发者菜单）

1. 在手机上启动支持第三方调试的 Mi Fitness 修改版。
2. 调出隐藏调试页面（`ThirdAppDebugFragment`）。
3. 包名填写：`com.custom.qrwallet`。
4. 点击 **Install third app** 选择 `.rpk` 文件安装。

---

## 07 / 代码库架构

```text
QRWallet/
├── AI_CUSTOMIZATION_PROMPT.md    # AI 定制专用提示词（英文母版）
├── generate_assets.py            # 本地全自动资源生成脚本
├── icon/                         # 原始 96x96 SVG 图标库
├── icon2.png                     # 手环主菜单钱包图标 (128x128)
├── package.json                  # 构建配置及脚本
├── sign/                         # 本地签名私钥与公钥
└── src/
    ├── manifest.json             # 快应用清单与系统权限配置
    ├── app.ux                    # 应用生命周期
    ├── common/
    │   ├── icons/                # 96x96 px PNG 界面图标
    │   ├── qrcodes/              # 184x184 px 反色 AMOLED 二维码
    │   └── logo.png              # 手环应用抽屉展示图标
    └── pages/
        ├── index/index.ux        # 卡片快捷方式主列表
        └── qrcode/qrcode.ux      # 全屏二维码展示器（带返回震动）
```

---

## 08 / 常见故障排查

| 异常现象 | 诱发原因 | 解决方案 |
| :--- | :--- | :--- |
| **手环打开应用瞬间黑屏** | 启用了 JSC 字节码编译 | 确保打包未传递 `--enable-jsc`（保持为 `false`）。 |
| **刷入新版后依然显示旧图标** | 手环 Flash 闪存缓存了原路径 | 安装前务必在手环端将旧应用完全卸载一次。 |
| **卡片文字有粗糙描边毛刺** | CSS 启用了伪粗体 `bold` | 将样式更改为 `font-weight: normal; font-size: 24px;`。 |
| **手机相机无法识别手环二维码** | 二维码缩放模糊或白底反光 | 严格维持 184×184 像素、`NEAREST` 采样及纯黑背景。 |

---

## 09 / 鸣谢与开源协议

- **作者 / 架构设计**：[mastermaiolo](https://github.com/mastermaiolo)
- **工作室签名**：**MAIOLO / SYSTEMS LAB** · **食**
- **开源协议**：[MIT](LICENSE) — 允许自由修改、定制及分发。
