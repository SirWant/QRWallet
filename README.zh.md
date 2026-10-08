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

## 04 / 安装指南

### 推荐路径（使用 Notify for Xiaomi）

1. 在 **[Releases](https://github.com/mastermaiolo/QRWallet/releases)** 页面下载预编译好的安装包（`com.custom.qrwallet.release.1.0.0.rpk`）。
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

## 05 / 人工智能一键定制 (AI Prompt)

由于官方 Mi Fitness 和 Notify 均**不提供在手机界面动态修改快应用内容的功能**，所有自定义信息都必须在打包时直接编译进 `.rpk` 二进制包中。

为了让你无需手写前端代码即可拥有专属版本，我们准备了 **[`AI_CUSTOMIZATION_PROMPT.md`](./AI_CUSTOMIZATION_PROMPT.md)**。

<details>
<summary><strong>AI 定制提示词模板（可直接复制）</strong></summary>

直接复制下方内容发送给任何大模型助手（**ChatGPT、Claude、Gemini、Antigravity、Cursor**）：

```text
你是一名精通小米 Vela 快应用（针对小米手环 9 与 10）的前端工程师。
我已经克隆了 "QRWallet" 项目，现在希望用我个人的数据定制专属的二维码和快捷方式：

我的数据：
- 微信/WhatsApp: [你的链接，如 https://wa.me/8613800000000]
- Telegram: [https://t.me/你的用户名]
- Instagram: [https://instagram.com/你的用户名]
- 支付宝/Revolut: [你的链接]
- GitHub: [https://github.com/你的用户名]
- 银行卡/IBAN: [卡号纯文本]
- 电话拨号: [tel:+8613800000000]
- Wi-Fi 无线网络: [WIFI:S:WiFi名称;T:WPA;P:WiFi密码;;]

技术实现规范：
1. 二维码：尺寸 184x184 px，AMOLED反色模式（纯黑背景 #000000，纯白模块 #FFFFFF），margin=1，采用 NEAREST 插值，保存到 src/common/qrcodes/<name>_dark.png。
2. 列表图标：96x96 px RGBA PNG，透明背景，保存到 src/common/icons/<name>.png。
3. 界面样式：每项高 160px，字体 24px normal（使用手环原生 MiSans）。
4. 编译输出：执行 npm run release（禁止使用 --enable-jsc 避免黑屏），递增 manifest.json 的 versionCode。
```

</details>

---

## 06 / 本地脚本生成

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

## 07 / 代码库架构

```text
QRWallet/
├── AI_CUSTOMIZATION_PROMPT.md    # AI 定制专用提示词
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
