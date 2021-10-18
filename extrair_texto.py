# Importando as bibliotecas necessárias
import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) ApplewebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}

# Inserindo link 
url = 'https://en.wikipedia.org/wiki/Natural_product'
url1 = 'https://en.wikipedia.org/wiki/Biochemistry'
bio = [url, url1]

def get_url(x):
    site = requests.get(x)
    soup = BeautifulSoup(site.content, 'html.parser')
    return soup

# Obtendo o texto da webpage
#df = soup.get_text()
df = get_url(url).get_text()

# Criando o arquivo .txt
with open("Biochemistry_and_Natural_Products.txt","w", encoding="utf-8") as f:
    f.write(df+'\n')
