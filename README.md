# Fluxo de trabalho para extração de textos bioquimicos da web

## Nosso objetivo aqui é como podemos analisar e visualizar informações de textos extraídos via web scrapy usando as ferramentas de processamento de linguagem natural NLP. Nesse trabalho é introdutório, servindo mais como exercício das ferramentas de NLP. Os textos alvos são referentes a textos sobre bioquímica de produtos naturais. A biblioteca nltk permite que possamos fazer um tratamento inicial do texto, onde eliminamos as stopwords, pontuações, colchetes etc. Realizamos a lematização que reduzir as palavras a sua forma base desse modo reduzindo a complexidade do texto. Uma informação muito importante que podemos extrair de um texto e o reconhecimento de entidade nomeada [Named Entity Recognition](https://towardsdatascience.com/named-entity-recognition-with-nltk-and-spacy-8c4a7d88e7da). 

## Nessa análise usamos textos no idioma inglês, contudo podemos facilmente adaptar os algoritmos para qualquer outro idioma apenas baixando o dicionário correspondente. No final salvamos alguns dados produzidos em arquivos csv e salvando em um banco de dados MySQL.

## O diagrama do fluxo de trabalho que usamos pode ser visto abaixo
![oi](https://github.com/RondinellyMorais/Work-Flow_NLP/blob/master/fluxwork.jpg)

## Podemos visualizar o código para extrair o texto abaixo 
![código web scrapy](https://github.com/RondinellyMorais/Work-Flow_NLP/blob/master/scrapy.png)

## O código do notebook com o processamento e análise do texto se encontra nesse link [Biochermistry](https://github.com/RondinellyMorais/Work-Flow_NLP/blob/master/Biochermistry.ipynb).

## Temos a tabela salva no banco de dados [tabela_mysql](https://github.com/RondinellyMorais/Work-Flow_NLP/blob/master/sql.png)
