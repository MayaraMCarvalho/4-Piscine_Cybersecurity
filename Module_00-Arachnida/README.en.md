# 🕸️ Arachnida - Module 00 - Cybersecurity Piscine (42 São Paulo)

Available in: [🇧🇷 Português](README.md)

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)

This project is an introduction to Web Scraping and Metadata Analysis, as part of the Cybersecurity Piscine. The project consists of two command-line tools: `spider` and `scorpion`, both developed in Python.

---

## 📜 Table of Contents

* [Overview](https://github.com/MayaraMCarvalho/4-Piscine_Cybersecurity/blob/master/Module_00-Arachnida/Readme.en.md#%EF%B8%8F-overview)
* [Features](https://github.com/MayaraMCarvalho/4-Piscine_Cybersecurity/blob/master/Module_00-Arachnida/Readme.en.md#-features)
* [Technologies Used](https://github.com/MayaraMCarvalho/4-Piscine_Cybersecurity/blob/master/Module_00-Arachnida/Readme.en.md#%EF%B8%8F-technologies-used)
* [Installation & Setup](https://github.com/MayaraMCarvalho/4-Piscine_Cybersecurity/blob/master/Module_00-Arachnida/Readme.en.md#-installation--setup)
* [Usage](https://github.com/MayaraMCarvalho/4-Piscine_Cybersecurity/blob/master/Module_00-Arachnida/Readme.en.md#-usage)
* [Author](https://github.com/MayaraMCarvalho/4-Piscine_Cybersecurity/blob/master/Module_00-Arachnida/Readme.en.md#-author)

---

## 🕸️ Overview

### 🕷️ Spider

The `spider` is a recursive web scraper designed to download images from a website. It crawls pages starting from an initial URL, identifies image links, and downloads them, respecting a maximum depth level.

### 🦂 Scorpion

The `scorpion` is a metadata (EXIF) analyzer for image files. It reads the hidden data within image files (like `.jpg`, `.png`, etc.) and displays sensitive information such as creation date, camera model, and sometimes even GPS coordinates.

---

## ✨ Features

### 🕷️Spider (`spider`)
* Downloads images from a provided URL.
* Recursively crawls the website to find more images (option `-r`).
* Allows limiting the recursion depth (option `-l N`, default 5).
* Allows specifying an output directory for the images (option `-p PATH`, default `./data/`).
* Filters and downloads only specific extensions: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`.

### 🦂 Scorpion (`scorpion`)
* Analyzes one or more image files provided as arguments.
* Displays EXIF and other basic metadata.
* Supports the same extensions as `spider`.

---

## 🛠️ Technologies Used

* **Python 3.x**
* **`requests`**: For making HTTP requests and downloading page/image content.
* **`BeautifulSoup4`**: For parsing HTML and finding link (`<a>`) and image (`<img>`) tags.
* **`Pillow` (PIL)**: For reading and extracting EXIF metadata from image files.
* **`argparse`**: (Built-in library) For creating the command-line interfaces (`-r`, `-l`, `-p`).

---

## 🚀 Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://[YOUR_REPO_URL] arachnida
    cd arachnida
    ```

2.  **Create and activate a virtual environment (Recommended):**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    # On Windows, use: .\.venv\Scripts\activate
    ```

3.  **Create the `requirements.txt` file:**
    Create a file named `requirements.txt` in the project root with the following content:
    ```txt
    requests
    beautifulsoup4
    Pillow
    ```

4.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Make the scripts executable:**
    (Add `#!/usr/bin/env python3` to the top of your `spider.py` and `scorpion.py` files)
    ```bash
    chmod +x spider
    chmod +x scorpion
    # Alternatively, rename your files to spider.py and scorpion.py and run with 'python3 spider.py ...'
    ```
---

## 🔧 Usage

### 🕷️ Spider
```bash
./spider [-r] [-l N] [-p PATH] URL
```

#### 📋 Examples:

```bash
# 1. Download images from the page (no recursion) to ./data/
./spider [https://example.com](https://example.com)
```

```bash
# 2. Recursively download with depth 2, saving to ./my_images/
./spider -r -l 2 -p ./my_images/ [https://example.com](https://example.com)
```

### 🦂 Scorpion

```bash
./scorpion FILE1 [FILE2 ...]
```

#### 📋 Example:

```bash
# Analyze the metadata of two images
./scorpion ./data/image1.jpg ./data/image2.png
```

---

## 👩🏻 Author
[Mayara Carvalho / macarval]
