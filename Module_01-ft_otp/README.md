# 🔐 ft_otp - Módulo 01 - Piscine Cybersecurity
(42 São Paulo)

Available in: [🇺🇸 English](README.en.md)

![Language](https://img.shields.io/badge/language-Python%20%7C%20C-blue.svg) ![Security](https://img.shields.io/badge/security-TOTP-red.svg)

Este projeto consiste na implementação de um sistema de autenticação **TOTP (Time-based One-Time Password)**. O objetivo é criar um programa capaz de gerar senhas efêmeras de 6 dígitos baseadas em tempo, compatível com o padrão RFC 6238, similar ao funcionamento do Google Authenticator.

---

## 📜 Índice

* [Visão Geral](https://github.com/MayaraMCarvalho/4-Piscine_Cybersecurity/tree/master/Module_01-ft_otp#%EF%B8%8F-vis%C3%A3o-geral)
* [Funcionalidades](https://github.com/MayaraMCarvalho/4-Piscine_Cybersecurity/tree/master/Module_01-ft_otp#-funcionalidades)
* [Tecnologias Utilizadas](https://github.com/MayaraMCarvalho/4-Piscine_Cybersecurity/tree/master/Module_01-ft_otp#%EF%B8%8F-tecnologias-utilizadas)
* [Instalação e Setup](https://github.com/MayaraMCarvalho/4-Piscine_Cybersecurity/tree/master/Module_01-ft_otp#-instala%C3%A7%C3%A3o-e-setup)
* [Modo de Uso](https://github.com/MayaraMCarvalho/4-Piscine_Cybersecurity/tree/master/Module_01-ft_otp#-modo-de-uso)
* [Autora](https://github.com/MayaraMCarvalho/4-Piscine_Cybersecurity/tree/master/Module_01-ft_otp#-autora)

---

## 🔐 Visão Geral

O `ft_otp` é uma ferramenta de linha de comando que permite gerenciar chaves secretas e gerar tokens de autenticação de dois fatores (2FA). Ele opera em dois modos principais: registro seguro de uma chave mestra e geração de tokens temporários baseados no algoritmo HOTP/TOTP.

O projeto segue estritamente as especificações:
* **RFC 4226** (HOTP: HMAC-Based One-Time Password Algorithm)
* **RFC 6238** (TOTP: Time-Based One-Time Password Algorithm)

---

## ✨ Funcionalidades

* **Registro de Chave (`-g`):** Recebe uma chave hexadecimal de 64+ caracteres e a armazena de forma segura (criptografada) em um arquivo `ft_otp.key`.
* **Geração de Token (`-k`):** Lê a chave armazenada e gera um novo token de 6 dígitos válido por 30 segundos.
* **Compatibilidade:** Os tokens gerados são verificáveis por ferramentas padrão como `oathtool`.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x (ou C, edite conforme sua escolha).
* **`hmac` & `hashlib`:** Para implementação do algoritmo de hash (HMAC-SHA1).
* **`struct`:** Para manipulação de bytes e conversão de dados para o truncamento dinâmico.
* **`time`:** Para captura do timestamp Unix e cálculo dos passos de tempo.
* **`argparse`:** Para tratamento dos argumentos de linha de comando.
* **`cryptography` / `Fernet`:** Para criptografia simétrica do arquivo de chave (se aplicável em Python).

---

## 🚀 Instalação e Setup

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/MayaraMCarvalho/4-Piscine_Cybersecurity/](https://github.com/MayaraMCarvalho/4-Piscine_Cybersecurity/)
    cd Module_01-ft_otp
    ```

2.  **Crie o ambiente virtual (se Python):**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Instale dependências (se houver):**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Dê permissão de execução:**
    ```bash
    chmod +x ft_otp
    ```

---

## 🔧 Modo de Uso

### 1. Registrar uma nova chave (`-g`)
A chave deve ser uma string hexadecimal com pelo menos 64 caracteres.

    ```bash
    ./ft_otp -g <arquivo_com_chave_hex>
    ```
*Isso criará o arquivo ft_otp.key criptografado.*

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

👩🏻 Autora
[Mayara Carvalho / macarval]

---
