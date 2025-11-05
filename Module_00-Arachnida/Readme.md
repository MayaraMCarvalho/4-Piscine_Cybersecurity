# 🕸️ Arachnida - Módulo 00 - Piscine Cybersecurity (42 São Paulo)

Available in: [🇺🇸 English](Readme.en.md)

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)

Este projeto é uma introdução ao Web Scraping e à Análise de Metadados, como parte da Piscina de Cibersegurança. O projeto consiste em duas ferramentas de linha de comando: `spider` e `scorpion`, ambas desenvolvidas em Python.

---

## 📜 Índice

* [Visão Geral](#-visão-geral)
* [Funcionalidades](#-funcionalidades)
* [Tecnologias Utilizadas](#-tecnologias-utilizadas)
* [Instalação e Setup](#-instalação-e-setup)
* [Modo de Uso](#-modo-de-uso)
* [Autor](#-autor)

---

## 🕸️ Visão Geral

### 🕷️ Spider

O `spider` é um web scraper recursivo projetado para baixar imagens de um site. Ele navega pelas páginas a partir de uma URL inicial, identifica links de imagens e os baixa, respeitando um nível de profundidade máximo.

### 🦂 Scorpion

O `scorpion` é um analisador de metadados (EXIF) para arquivos de imagem. Ele lê os dados ocultos em arquivos de imagem (como `.jpg`, `.png`, etc.) e exibe informações sensíveis como data de criação, modelo da câmera, e às vezes até coordenadas GPS.

---

## ✨ Funcionalidades

### 🕷️Spider (`spider`)
* Baixa imagens de uma URL fornecida.
* Navega recursivamente pelo site para encontrar mais imagens (opção `-r`).
* Permite limitar a profundidade da recursão (opção `-l N`, padrão 5).
* Permite especificar um diretório de saída para as imagens (opção `-p PATH`, padrão `./data/`).
* Filtra e baixa apenas extensões específicas: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`.

### 🦂 Scorpion (`scorpion`)
* Analisa um ou mais arquivos de imagem fornecidos como argumentos.
* Exibe dados EXIF e outros metadados básicos.
* Compatível com as mesmas extensões que o `spider`.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **`requests`**: Para realizar requisições HTTP e baixar o conteúdo das páginas e imagens.
* **`BeautifulSoup4`**: Para fazer o parsing do HTML e encontrar links (`<a>`) e tags de imagem (`<img>`).
* **`Pillow` (PIL)**: Para ler e extrair os metadados EXIF dos arquivos de imagem.
* **`argparse`**: (Biblioteca nativa) Para criar as interfaces de linha de comando (`-r`, `-l`, `-p`).

---

## 🚀 Instalação e Setup

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/MayaraMCarvalho/4-Piscine_Cybersecurity/tree/master/Module_00-Arachnida arachnida
    cd arachnida
    ```

2.  **Crie e ative um ambiente virtual (Recomendado):**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    # No Windows, use: .\.venv\Scripts\activate
    ```

3.  **Crie o arquivo `requirements.txt`:**
    Crie um arquivo chamado `requirements.txt` na raiz do projeto com o seguinte conteúdo:
    ```txt
    requests
    beautifulsoup4
    Pillow
    ```

4.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Dê permissão de execução aos scripts:**
    (Adicione `#!/usr/bin/env python3` no topo dos seus arquivos `spider.py` e `scorpion.py`)
    ```bash
    chmod +x spider
    chmod +x scorpion
    # Ou renomeie seus arquivos para spider.py e scorpion.py e execute com 'python3 spider.py ...'
    ```

---

## 🔧 Usage

### 🕷️ Spider
```bash
./spider [-r] [-l N] [-p PATH] URL
```

#### 📋 Exemplos:

```bash
# 1. Baixar imagens da página (sem recursão) para ./data/
./spider [https://exemplo.com](https://exemplo.com)
```

```bash
# 2. Baixar recursivamente com profundidade 2, salvando em ./minhas_imagens/
./spider -r -l 2 -p ./minhas_imagens/ [https://exemplo.com](https://exemplo.com)
```

### 🦂 Scorpion

```bash
./scorpion ARQUIVO1 [ARQUIVO2 ...]
```

#### 📋 Exemplo:

```bash
# Analisar os metadados de duas imagens
./scorpion ./data/imagem1.jpg ./data/imagem2.png
```

---

## 👩🏻 Autora
[Mayara Carvalho / macarval]


