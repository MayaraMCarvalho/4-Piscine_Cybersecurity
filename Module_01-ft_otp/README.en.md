# 🔐 ft_otp - Module 01 - Cybersecurity Piscine
(42 São Paulo)

Available in: [🇧🇷 Português](README.md)

![Language](https://img.shields.io/badge/language-Python%20%7C%20C-blue.svg) ![Security](https://img.shields.io/badge/security-TOTP-red.svg)

This project consists of implementing a **TOTP (Time-based One-Time Password)** authentication system. The goal is to create a program capable of generating ephemeral 6-digit time-based passwords, compatible with the RFC 6238 standard, similar to how Google Authenticator works.

---

## 📜 Table of Contents

* [Overview](https://github.com/MayaraMCarvalho/4-Piscine_Cybersecurity/tree/master/Module_01-ft_otp#%EF%B8%8F-overview)
* [Features](https://github.com/MayaraMCarvalho/4-Piscine_Cybersecurity/tree/master/Module_01-ft_otp#-features)
* [Technologies Used](https://github.com/MayaraMCarvalho/4-Piscine_Cybersecurity/tree/master/Module_01-ft_otp#%EF%B8%8F-technologies-used)
* [Installation & Setup](https://github.com/MayaraMCarvalho/4-Piscine_Cybersecurity/tree/master/Module_01-ft_otp#-installation--setup)
* [Usage](https://github.com/MayaraMCarvalho/4-Piscine_Cybersecurity/tree/master/Module_01-ft_otp#-usage)
* [Author](https://github.com/MayaraMCarvalho/4-Piscine_Cybersecurity/tree/master/Module_01-ft_otp#-author)

---

## 🔐 Overview

`ft_otp` is a command-line tool that allows for the management of secret keys and the generation of two-factor authentication (2FA) tokens. It operates in two main modes: secure registration of a master key and generation of temporary tokens based on the HOTP/TOTP algorithm.

The project strictly follows these specifications:
* **RFC 4226** (HOTP: HMAC-Based One-Time Password Algorithm)
* **RFC 6238** (TOTP: Time-Based One-Time Password Algorithm)

---

## ✨ Features

* **Key Registration (`-g`):** Receives a hexadecimal key of 64+ characters and stores it securely (encrypted) in a file named `ft_otp.key`.
* **Token Generation (`-k`):** Reads the stored key and generates a new 6-digit token valid for 30 seconds.
* **Compatibility:** The generated tokens are verifiable by standard tools like `oathtool`.

---

## 🛠️ Technologies Used

* **Language:** Python 3.x (or C, edit according to your choice).
* **`hmac` & `hashlib`:** For implementing the hash algorithm (HMAC-SHA1).
* **`struct`:** For byte manipulation and data conversion for dynamic truncation.
* **`time`:** For capturing the Unix timestamp and calculating time steps.
* **`argparse`:** For handling command-line arguments.
* **`cryptography` / `Fernet`:** For symmetric encryption of the key file (if applicable in Python).

---

## 🚀 Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/MayaraMCarvalho/4-Piscine_Cybersecurity/](https://github.com/MayaraMCarvalho/4-Piscine_Cybersecurity/)
    cd Module_01-ft_otp
    ```

2.  **Create a virtual environment (if Python):**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install dependencies (if any):**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Grant execution permissions:**
    ```bash
    chmod +x ft_otp
    ```

---

## 🔧 Usage

### 1. Register a new key (`-g`)
The key must be a hexadecimal string with at least 64 characters.

    ```bash
    ./ft_otp -g <file_containing_hex_key>
    ```
*This will create the encrypted ft_otp.key file.*

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

👩🏻 Author
[Mayara Carvalho / macarval]

---
