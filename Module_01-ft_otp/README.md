# 🔐 ft_otp - Módulo 01 - Piscine Cybersecurity
(42 São Paulo)

Available in: [🇺🇸 English](README.en.md)

![Language](https://img.shields.io/badge/language-Python-blue.svg) ![Security](https://img.shields.io/badge/security-TOTP-red.svg) ![GUI](https://img.shields.io/badge/interface-Tkinter-pink.svg)

Este projeto consiste na implementação de um sistema de autenticação **TOTP (Time-based One-Time Password)**. O objetivo é criar um programa capaz de gerar senhas efêmeras de 6 dígitos baseadas em tempo, compatível com o padrão RFC 6238, similar ao funcionamento do Google Authenticator.

---

## 📜 Índice

* [Visão Geral](#%EF%B8%8F-vis%C3%A3o-geral)
* [Funcionalidades](#-funcionalidades)
* [Tecnologias Utilizadas](#%EF%B8%8F-tecnologias-utilizadas)
* [Instalação e Setup](#-instala%C3%A7%C3%A3o-e-setup)
* [Modo de Uso (CLI)](#-modo-de-uso-cli)
* [Interface Gráfica (GUI)](#-interface-gr%C3%A1fica-gui)
* [Autora](#-autora)

---

## 🔐 Visão Geral

O `ft_otp` é uma ferramenta que permite gerenciar chaves secretas e gerar tokens de autenticação de dois fatores (2FA). Ele opera tanto via **Linha de Comando** quanto via **Interface Gráfica**, garantindo segurança no armazenamento e facilidade no uso.

O projeto segue estritamente as especificações:
* **RFC 4226** (HOTP: HMAC-Based One-Time Password Algorithm)
* **RFC 6238** (TOTP: Time-Based One-Time Password Algorithm)

---

## ✨ Funcionalidades

* **Registro de Chave (`-g`):** Recebe uma chave hexadecimal de 64+ caracteres e a armazena de forma segura (criptografada) em um arquivo `ft_otp.key`.
* **QR Code Automático:** Gera um arquivo `ft_otp_qr.png` compatível com apps autenticadores (Google Auth, Authy) no momento do registro.
* **Geração de Token (`-k`):** Gera um novo token de 6 dígitos válido por 30 segundos.
* **Compatibilidade:** Os tokens gerados são verificáveis por ferramentas padrão como `oathtool`.
* **Interface Gráfica (GUI):**
    * Visualização do token em tempo real.
    * Barra de progresso visual para o tempo de expiração.
    * Botão de cópia para área de transferência (Clipboard).
    * Pop-up para escanear o QR Code na tela.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Criptografia:** `cryptography` (Fernet/AES) para o arquivo de chave.
* **Algoritmos:** `hmac`, `hashlib`, `struct` e `time` para a lógica TOTP.
* **Interface:** `tkinter` (Nativo) e `ttk` para a GUI.
* **Utilitários:**
    * `qrcode` & `Pillow`: Geração e exibição de imagens.
    * `pyperclip`: Manipulação robusta da área de transferência.
    * `argparse`: Argumentos de linha de comando.
    * `python-dotenv`: Gerenciamento de variáveis de ambiente.

---

## 🚀 Instalação e Setup

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/MayaraMCarvalho/4-Piscine_Cybersecurity/](https://github.com/MayaraMCarvalho/4-Piscine_Cybersecurity/)
    cd Module_01-ft_otp
    ```

2.  **Setup Automático (Makefile):**
    Este comando cria o ambiente virtual, instala as dependências e configura o executável.
    ```bash
    make
    ```

    > **Nota para Linux:** Se a interface gráfica falhar, instale o pacote do sistema:
    > `sudo apt-get install python3-tk`

---

## 🔧 Modo de Uso (CLI)

### 1. Registrar uma nova chave (`-g`)
A chave deve ser uma string hexadecimal com pelo menos 64 caracteres.

    ```bash
    ./ft_otp -g <arquivo_com_chave_hex>
    ```
*Isso criará o arquivo `ft_otp.key` criptografado e o `ft_otp_qr.png`.*

### 2. Gerar Token (`-k`)
Gera um token instantâneo usando a chave salva anteriormente.

    ```bash
    ./ft_otp -k ft_otp.key
    ```
*Saída esperada: Um código de 6 dígitos (ex: 123456).*

**Validação Externa (Oathtool)**
Você pode validar se o código gerado está correto comparando com o oathtool:

    ```bash
    oathtool --totp -b $(cat key.hex)
    ```

---

## 🎨 Interface Gráfica (GUI)
Para uma experiência visual completa, utilize o comando abaixo. O Makefile garantirá que as permissões dos arquivos sensíveis (`chmod 600`) estejam corretas antes de abrir a janela.

    ```bash
    make interface
    ```

**Recursos da Interface:**
1. **Registro:** Cole sua chave Hex no campo superior e clique em "Save & Generate".
2. **QR Code:** Clique em "View QR" para abrir um pop-up e escanear com o celular.
3. **Token Ativo:** O código é atualizado automaticamente a cada 30 segundos.
4. **Cópia:** Clique em "Copy Token" para copiar o código para a área de transferência.

---

## 👩🏻 Autora
**Mayara Carvalho**
<br>
[:octocat: @MayaraMCarvalho](https://github.com/MayaraMCarvalho) | 42 Login: `macarval`

---
