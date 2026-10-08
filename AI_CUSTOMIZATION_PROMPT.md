# 🤖 Prompt de Customização por Inteligência Artificial (AI Prompt)

> **Por que este prompt existe?**  
> Nem o **Notify for Xiaomi** nem os **mods do Mi Fitness** possuem uma tela de edição ou configurações no telemóvel para alterar o conteúdo de aplicativos da pulseira.  
> No ecossistema **Xiaomi Vela / QuickApp**, todos os ícones, textos e QR codes são **embutidos diretamente no pacote compilado (`.rpk`)**.  
> Para alterar os seus atalhos e QR codes, basta copiar o prompt abaixo e colar em qualquer IA (ChatGPT, Claude, Gemini, Antigravity, Cursor, etc.).

---

## 📋 Copie e Cole o Texto Abaixo na sua IA:

```text
Você é um desenvolvedor especialista no framework Xiaomi Vela QuickApp (para Xiaomi Smart Band 9 e 10).
Eu tenho o projeto "QRWallet" e quero customizar os atalhos, ícones e QR Codes com os meus dados pessoais.

Aqui estão os meus dados para cada atalho:
- WhatsApp: [coloque seu link ou número, ex: https://wa.me/351912345678]
- Telegram: [coloque seu username, ex: https://t.me/seunome]
- Instagram: [coloque seu perfil, ex: https://instagram.com/seunome]
- Revolut: [coloque seu link de pagamento, ex: https://revolut.me/seurevtag]
- GitHub: [coloque seu GitHub, ex: https://github.com/seunome]
- IBAN: [coloque seu IBAN em texto simples sem espaços, ex: PT50000000000000000000000]
- Telefone: [coloque seu número completo com indicativo, ex: tel:+351912345678]
- Wi-Fi: [coloque o nome da rede e senha, ex: WIFI:S:NomeDaRede;T:WPA;P:SenhaSecreta;;]

Por favor, execute as seguintes tarefas respeitando rigorosamente as especificações técnicas da Xiaomi Smart Band:

1. ESPECIFICAÇÕES DOS QR CODES:
   - Dimensões exatas: 184 x 184 px (para caber perfeitamente na tela de 192px de largura).
   - Modo Escuro Invertido (OLED): Fundo 100% PRETO (#000000) e quadrados 100% BRANCOS (#FFFFFF).
   - Margem (Quiet Zone): borda de 1 módulo (margin=1).
   - Resampling: Interpolação NEAREST (vizinho mais próximo) para manter os cantos dos quadrados nítidos e legíveis por câmeras de telemóvel sem borrões.
   - Local de destino: salvar em 'src/common/qrcodes/<nome>_dark.png'.

2. ESPECIFICAÇÕES DOS ÍCONES DA LISTA:
   - Dimensões exatas: 96 x 96 px.
   - Formato: PNG com transparência (RGBA).
   - Ícones SVG: converter para 96x96 px mantendo as cores e gradientes oficiais das marcas.
   - Local de destino: salvar em 'src/common/icons/<nome>.png'.

3. ESPECIFICAÇÕES DA INTERFACE (index.ux):
   - Cada item da lista deve ter altura de 160px (height: 160px) para exibir exatamente 3 itens por tela no display de 490px de altura.
   - Tamanho do ícone no CSS: width: 96px; height: 96px.
   - Tipografia do título: color: #ffffff; font-size: 24px; font-weight: normal; margin-top: 6px.
     (ATENÇÃO: NUNCA usar 'font-weight: bold', pois o motor Vela aplica um contorno artificial grosso e pixelado na fonte nativa MiSans).

4. ESPECIFICAÇÕES DO MANIFEST E COMPILAÇÃO:
   - No 'src/manifest.json', incremente o 'versionCode' e 'versionName' (para evitar que a pulseira use a versão em cache).
   - Compile o pacote rodando: npm run release (que roda 'aiot release').
   - CRÍTICO: NUNCA utilize a flag '--enable-jsc' (o bytecode JSC causa tela preta no Xiaomi HyperOS / Band 10). Mantenha JavaScript padrão em texto.

Gere os arquivos ou execute o script 'python3 generate_assets.py' com meus dados e compile o .rpk final em dist/.
```

---

## 🛠️ Como Funciona o Gerador Local Automatizado (`generate_assets.py`)

Se preferir não usar o chat e quiser rodar localmente no terminal:

1. Abra o arquivo `generate_assets.py`.
2. Edite o dicionário `QR_ITEMS` com seus links/dados:
   ```python
   QR_ITEMS = {
       "whatsapp": "https://wa.me/351912345678",
       "telegram": "https://t.me/seunome",
       "instagram": "https://instagram.com/seunome",
       "revolut": "https://revolut.me/seunome",
       "github": "https://github.com/seunome",
       "iban": "PT50000000000000000000000",
       "phone": "tel:+351912345678",
       "wifi": "WIFI:S:MinhaRede;T:WPA;P:MinhaSenha;;",
   }
   ```
3. Execute o script no terminal:
   ```bash
   python3 generate_assets.py
   ```
4. Compile o arquivo `.rpk`:
   ```bash
   npm run release
   ```
5. O seu `.rpk` pronto para instalar estará na pasta `dist/`.

---

## 📲 Como Instalar na Xiaomi Smart Band

### Método 1: Pelo aplicativo "Notify for Xiaomi" (Recomendado)
1. Envie o ficheiro `.rpk` (da pasta `dist/`) para o seu telemóvel (via Telegram, WhatsApp, e-mail ou cabo USB).
2. Abra o app **Notify for Xiaomi**.
3. Vá em **Definições / Dispositivo**.
4. Toque em **Aplicativo de terceiros** (Third-party app).
5. Selecione **Carregar arquivo .rpk** e escolha o arquivo.
6. Aguarde a transferência Bluetooth ser concluída.

> 💡 **Dica Importante**: Se você já tinha uma versão anterior instalada, **desinstale-a primeiro** pelo Notify para que a pulseira limpe o cache de ícones antigos da memória flash.

### Método 2: Pelo Mi Fitness Modificado (Developer Mode)
1. No telemóvel pareado, acesse o menu de debug (`ThirdAppDebugFragment`).
2. Digite o package name: `com.custom.qrwallet`.
3. Toque em **Install third app** e selecione o ficheiro `.rpk`.
