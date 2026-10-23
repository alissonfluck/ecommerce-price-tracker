import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def coletar_precos_livros():
    # categoria Science
    url = "https://books.toscrape.com/catalogue/category/books/science_22/index.html"

    response = requests.get(url)
    dados = BeautifulSoup(response.text, 'html.parser')

    dados_livros = []

    livros = dados.find_all('article', class_='product_pod')

    for livro in livros:
        h3_tag = livro.find('h3')
        p_tag = livro.find('p', class_='price_color')

        try:
            if h3_tag and h3_tag.a and p_tag:
                titulo = h3_tag.a['title']
                preco = p_tag.text

                preco_limpo = float(preco.replace('Â£', '').replace('£', ''))

                dados_livros.append({
                    'product_name': titulo,
                    'price': preco_limpo,
                    'scraped_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
        except Exception as e:
            print(f"Erro: {e}. Elemento HTML não encontrado, pulando item.")

    df = pd.DataFrame(dados_livros)
    print("Extração concluída com sucesso:")
    print(df.head())

    return df

if __name__ == "__main__":
    coletar_precos_livros()


