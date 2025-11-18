# 🕸️ Arachnida - Módulo 00 - Piscine Cybersecurity (42 São Paulo)

Available in: [🇺🇸 English](README.en.md)

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)

Este projeto é uma introdução ao Web Scraping e à Análise de Metadados, como parte da Piscina de Cibersegurança. O projeto consiste em duas ferramentas de linha de comando: `spider` e `scorpion`, ambas desenvolvidas em Python.

---

## 📜 Índice

* [Visão Geral](https://github.com/MayaraMCarvalho/4-Piscine_Cybersecurity/tree/master/Module_00-Arachnida#%EF%B8%8F-vis%C3%A3o-gerall)
* [Funcionalidades](https://github.com/MayaraMCarvalho/4-Piscine_Cybersecurity/tree/master/Module_00-Arachnida#-funcionalidades)
* [Tecnologias Utilizadas](https://github.com/MayaraMCarvalho/4-Piscine_Cybersecurity/tree/master/Module_00-Arachnida#%EF%B8%8F-tecnologias-utilizadas)
* [Instalação e Setup](https://github.com/MayaraMCarvalho/4-Piscine_Cybersecurity/tree/master/Module_00-Arachnida#-instala%C3%A7%C3%A3o-e-setup)
* [Modo de Uso](https://github.com/MayaraMCarvalho/4-Piscine_Cybersecurity/tree/master/Module_00-Arachnida#-modo-de-uso)
* [Autor](https://github.com/MayaraMCarvalho/4-Piscine_Cybersecurity/tree/master/Module_00-Arachnida#-autora)

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
* **Modificar Metadados:** Permite alterar valores de tags específicas (opção `-m`).
* **Deletar Metadados:** Permite remover todos os dados EXIF de um arquivo (opção `-d`).

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
    git clone https://github.com/MayaraMCarvalho/4-Piscine_Cybersecurity/
    cd Module_00-Arachnida
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

## 🤖 Automação com Makefile

Este projeto inclui um `Makefile` para simplificar a configuração do ambiente, instalação de dependências e execução de testes rápidos.

### Comandos Disponíveis

* **Setup Automático:**
    ```bash
    make
    ```
    Cria o ambiente virtual (`.venv`), instala todas as dependências do `requirements.txt` e verifica se os pacotes estão corretos.

* **Rodar o Spider (Padrão):**
    ```bash
    make run_spider
    ```
    Executa o `spider` com as configurações e URL definidas nas variáveis do Makefile. Útil para testes rápidos.

* **Rodar o Scorpion (Padrão):**
    ```bash
    make run_scorpion
    ```
    Executa o `scorpion` nos arquivos definidos no Makefile.

* **Limpeza:**
    ```bash
    make clean    # Remove arquivos de cache (__pycache__)
    make fclean   # Remove cache, arquivos baixados e o ambiente virtual (.venv)
    make re       # Reinstala tudo do zero (fclean + all)
    ```

---

## 🔧 Modo de Uso

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
./scorpion [-m TAG VALOR | -d] ARQUIVO1 [ARQUIVO2 ...]
```

#### 📋 Exemplo:

```bash
# 1. Analisar os metadados de duas imagens
./scorpion ./data/imagem1.jpg ./data/imagem2.png
```

```bash
# 2. Deletar todos os metadados de uma imagem
./scorpion -d ./data/imagem1.jpg
```

```bash
# 3. Modificar uma tag de metadados específica
# Nota: O nome da TAG deve ser exato (ex: 'Orientation', 'Software') e o tipo do VALOR deve corresponder (int ou str).
./scorpion -m Orientation 1 ./data/imagem1.jpg
./scorpion -m Software "Meu Editor Personalizado" ./data/imagem2.png
```

---

## 👩🏻 Autora
[Mayara Carvalho / macarval]
