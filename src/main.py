import pandas as pd
from playwright.sync_api import sync_playwright

lista = []

with sync_playwright() as p:
    
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    pagina.goto("https://www.w3schools.com/html/html_tables.asp")

    extrair_tabela = pagina.locator("#customers")
    linhas_tabela = extrair_tabela.locator("tr")

    for i in range(1, linhas_tabela.count()):
        linha = linhas_tabela.nth(i)
        celula = linha.locator("td")

        empresa = celula.nth(0).inner_text()
        contato = celula.nth(1).inner_text()
        pais = celula.nth(2).inner_text()

        lista.append({
            "Empresa":empresa,
            "Contato":contato,
            "Pais":pais
        })
    
    input("C L I Q U E  E N T E R P A R A E N C E R R A R")
    navegador.close()

try:
    df = pd.DataFrame(lista)
    df.to_excel("output/empresas.xlsx", index=False)
except FileNotFoundError:
    print("Arquivo Não Encontrado!")
except PermissionError:
    print("Permissão Negada!")
except Exception as e:
    print("Ocorrreu um Erro inesperado:",{e})
