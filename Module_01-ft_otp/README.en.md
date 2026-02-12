# 🔐 ft_otp - Module 01 - Cybersecurity Piscine
(42 São Paulo)

Available in: [🇧🇷 Português](README.md)

![Language](https://img.shields.io/badge/language-Python-blue.svg) ![Security](https://img.shields.io/badge/security-TOTP-red.svg) ![GUI](https://img.shields.io/badge/interface-Tkinter-pink.svg)

This project consists of implementing a **TOTP (Time-based One-Time Password)** authentication system. The goal is to create a program capable of generating ephemeral 6-digit time-based passwords, compatible with the RFC 6238 standard, similar to how Google Authenticator works.

---

## 📜 Table of Contents

* [Overview](#%EF%B8%8F-overview)
* [Features](#-features)
* [Technologies Used](#%EF%B8%8F-technologies-used)
* [Installation & Setup](#-installation--setup)
* [Usage (CLI)](#-usage-cli)
* [Graphical Interface (GUI)](#-graphical-interface-gui)
* [Author](#-author)

---

## 🔐 Overview

`ft_otp` is a tool that allows for the management of secret keys and the generation of two-factor authentication (2FA) tokens. It operates via both **Command Line** and **Graphical Interface**, ensuring secure storage and ease of use.

The project strictly follows these specifications:
* **RFC 4226** (HOTP: HMAC-Based One-Time Password Algorithm)
* **RFC 6238** (TOTP: Time-Based One-Time Password Algorithm)

---

## ✨ Features

* **Secure Registration (`-g`):** Receives a hexadecimal key (64+ chars) and stores it securely (encrypted) in `ft_otp.key`.
* **Automatic QR Code:** Generates a `ft_otp_qr.png` file compatible with authenticator apps (Google Auth, Authy) upon registration.
* **Token Generation (`-k`):** Generates a new 6-digit token valid for 30 seconds.
* **Compatibility:** The generated tokens are verifiable by standard tools like `oathtool`.
* **Graphical User Interface (GUI):**
    * Real-time token display.
    * Visual progress bar for expiration time.
    * "Copy to Clipboard" button.
    * Pop-up window to scan the QR Code.

---

## 🛠️ Technologies Used

* **Language:** Python 3.x
* **Encryption:** `cryptography` (Fernet/AES) for the key file.
* **Algorithms:** `hmac`, `hashlib`, `struct`, and `time` for TOTP logic.
* **Interface:** `tkinter` (Native) and `ttk` for the GUI.
* **Utilities:**
    * `qrcode` & `Pillow`: Image generation and display.
    * `pyperclip`: Robust clipboard manipulation.
    * `argparse`: Command-line arguments.
    * `python-dotenv`: Environment variable management.

---

## 🚀 Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/MayaraMCarvalho/4-Piscine_Cybersecurity/](https://github.com/MayaraMCarvalho/4-Piscine_Cybersecurity/)
    cd Module_01-ft_otp
    ```

2.  **Automatic Setup (Makefile):**
    This command creates the virtual environment, installs dependencies, and configures the executable.
    ```bash
    make
    ```

    > **Note for Linux:** If the GUI fails to launch, install the system package:
    > `sudo apt-get install python3-tk`

---

## 🔧 Usage (CLI)

### 1. Register a new key (`-g`)
The key must be a hexadecimal string with at least 64 characters.
   ```bash
    ./ft_otp -g <file_containing_hex_key>
   ```
*This will create the encrypted `ft_otp.key` file and the `ft_otp_qr.png` image.*

### 2. Generate Token (`-k`)
Generates an instant token using the previously saved key.
   ```bash
    ./ft_otp -k ft_otp.key
   ```
*Expected output: A 6-digit code (e.g., 123456).*

**External Validation (Oathtool)**
You can validate if the generated code is correct by comparing it with oathtool:
   ```bash
    oathtool --totp -b $(cat key.hex)
   ```

---

## 🎨 Graphical Interface (GUI)

<div align="center">
   <img src="https://github.com/user-attachments/assets/b59525ee-bd94-4c70-9cb9-a214a9d95182" alt="ft_otp Interface Gráfica" width="600">
</div>

For a complete visual experience, use the command below. The Makefile ensures that sensitive file permissions (`chmod 600`) are correct before opening the window.
   ```bash
    make interface
   ```

**Interface Features:**
1. **Register:** Paste your Hex key in the top field and click "Save & Generate".
2. **QR Code:** Click "View QR" to open a pop-up and scan it with your phone.
3. **Active Token:** The code updates automatically every 30 seconds.
4. **Copy:** Click "Copy Token" to copy the code to your clipboard.

---

## 👩🏻 Author
**Mayara Carvalho**
<br>
[:octocat: @MayaraMCarvalho](https://github.com/MayaraMCarvalho) | 42 Login: `macarval`

---
