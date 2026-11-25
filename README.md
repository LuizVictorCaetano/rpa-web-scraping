# RPA Web Scraping

Projeto de automação desenvolvido com Python e Playwright para extração de dados de uma tabela HTML e geração automática de relatórios Excel.

## Tecnologias utilizadas

- Python
- Playwright
- Pandas
- Openpyxl

## Funcionalidades

- Acessa uma página web automaticamente.
- Localiza uma tabela HTML.
- Extrai empresas, contatos e países.
- Armazena os dados em uma lista de dicionários.
- Converte os dados em um DataFrame usando Pandas.
- Exporta os dados para um arquivo Excel.

## Como executar

1. Clone este repositório.
2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Instale o Chromium:

```bash
playwright install chromium
```

4. Execute:

```bash
python src/main.py
```

## Fonte dos dados

[W3Schools - HTML Tables](https://www.w3schools.com/html/html_tables.asp)

## Objetivo

Projeto desenvolvido como parte dos meus estudos de Python e RPA, com foco em automação web, extração e manipulação de dados.
