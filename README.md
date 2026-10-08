# ⌚ QRWallet - Xiaomi Smart Band QR Codes # ⌚ Xiaomi Smart Band QR Codes & Shortcuts (QuickApp) Shortcuts (QuickApp)

Aplicativo nativo open-source para **Xiaomi Smart Band 9 e Smart Band 10** (Xiaomi Vela / HyperOS) para exibir **QR Codes e Atalhos Rápidos** na tela da pulseira sem depender de conexão contínua com a internet.

---

## ✨ Recursos

- ⚡ **100% Autônomo**: Roda diretamente na pulseira (Vela QuickApp), não precisa do telemóvel por perto.
- 📐 **Interface Otimizada**: Exibe exatamente 3 itens por tela com rolagem suave (`height: 160px`), ícones oficiais de `96x96 px` e tipografia nativa `MiSans` a `24px`.
- 🔍 **QR Codes Otimizados para AMOLED**: Formato invertido (fundo preto `#000000`, quadrados brancos `#FFFFFF`), sem margens excessivas (184x184 px), leitura instantânea pelo Google Lens e câmeras.
- 📳 **Feedback Háptico**: Vibração suave ao selecionar o item e ao retornar.
- 🛡️ **Seguro e Privado**: Nenhum dado é enviado para servidores externos. Todos os QR codes ficam gravados na memória local do relógio.

---

## 🗂️ Estrutura do Projeto

```text
QRWallet/
├── AI_CUSTOMIZATION_PROMPT.md  <-- Prompt pronto para colar em qualquer IA para customizar
├── generate_assets.py          <-- Script Python que gera os QR codes e converte os ícones
├── icon/                       <-- Vetores SVG dos ícones (96x96)
├── icon2.png                   <-- Ícone do aplicativo para o menu do relógio (128x128)
├── package.json                <-- Scripts de compilação (aiot release)
├── sign/                       <-- Chaves de assinatura do pacote
└── src/
    ├── manifest.json           <-- Configurações do app, permissões e resolução (192px)
    ├── common/
    │   ├── icons/              <-- Ícones PNG (96x96 px)
    │   ├── qrcodes/            <-- QR codes gerados (184x184 px, fundo preto)
    │   └── logo.png            <-- Ícone exibido na lista de apps da pulseira
    └── pages/
        ├── index/index.ux      <-- Lista de atalhos
        └── qrcode/qrcode.ux    <-- Tela de exibição em tela cheia do QR Code
```

---

## 🚀 Como Customizar com Inteligência Artificial

Como os apps oficiais (Mi Fitness e Notify) **não possuem painel de edição no celular** para alterar conteúdo de aplicativos Vela, todas as informações são compiladas diretamente no `.rpk`.

Para criar a sua própria versão com seus links e dados em minutos:

1. Abra o arquivo **[`AI_CUSTOMIZATION_PROMPT.md`](./AI_CUSTOMIZATION_PROMPT.md)**.
2. Copie o prompt, preencha os seus links (WhatsApp, Telegram, IBAN, Wi-Fi, etc.) e envie para o seu assistente de IA preferido (**ChatGPT, Claude, Gemini, Antigravity, Cursor**).
3. A IA executará ou guiará você com todas as dimensões e formatos exatos!

---

## 🛠️ Como Customizar Manualmente (Terminal)

### 1. Pré-requisitos
- Node.js >= 16
- Python 3 com Pillow (`pip install Pillow`)
- `qrencode` e `rsvg-convert` instalados no sistema (ex: `sudo apt install qrencode librsvg2-bin` ou `sudo pacman -S qrencode librsvg`)

### 2. Editar seus dados
Abra `generate_assets.py` e altere os valores no dicionário `QR_ITEMS`:
```python
QR_ITEMS = {
    "whatsapp": "https://wa.me/351912345678",
    "telegram": "https://t.me/seunome",
    "instagram": "https://instagram.com/seunome",
    "revolut": "https://revolut.me/seunome",
    "github": "https://github.com/seunome",
    "iban": "PT50000000000000000000000",
    "phone": "tel:+351912345678",
    "wifi": "WIFI:S:NomeDaRede;T:WPA;P:SenhaDaRede;;",
}
```

### 3. Gerar os arquivos
```bash
python3 generate_assets.py
```

### 4. Compilar o arquivo `.rpk`
```bash
npm run release
```
O pacote final será gerado em:
`dist/com.custom.qrwallet.release.1.0.0.rpk`

---

## 📲 Como Instalar na Pulseira

### Via Notify for Xiaomi:
1. Transfira o ficheiro `.rpk` gerado na pasta `dist/` para o celular.
2. No aplicativo **Notify for Xiaomi**, vá em **Definições / Dispositivo**.
3. Selecione **Aplicativo de terceiros** > **Carregar arquivo .rpk**.
4. Selecione o arquivo e aguarde a sincronização.
*(Se já tinha uma versão anterior, desinstale-a primeiro no relógio para limpar a cache).*

---

## 📜 Licença

MIT License - sinta-se livre para usar, customizar e distribuir!
