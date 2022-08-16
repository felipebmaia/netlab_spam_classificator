# Classificador de SPAM - NetLab

#### Autor: [Felipe Maia](https://www.linkedin.com/in/felipe-b-maia/)

<br/>

A proposta deste projeto é desenvolver um classificador de SPAM utilizando uma base de dados de um aplicativo de mensagens instantâneas e medir a eficiência do modelo.

## Sumário

- [Sobre](#sobre)
- [Desenvolvimento](#desenvolvimento)
- [Resultado](#resultado)
- [Descrição_dos_Diretórios](#descrição_dos_diretórios)

## Sobre

Este projeto tem como objetivo utilizar uma base de dados de um aplicativo de mensagens instantâneas e, a partir desta base, desenvolver um modelo de Classificação utilizando técnicas de Machine Learning. O projeto consiste em um script python que utiliza a biblioteca do Scikit-Learn para realizar o Tokenizer e Classificador, e a plataforma Natural Language Toolkit (NLTK) foi usada para construir a análise de texto. Também foi utilizado o Spacy para identificar o que cada texto significa (Pós-Tagging). Após a construção do modelo, foi criado um arquivo.py para rodar o script e gerar a saída dos dados classificados.

## Desenvolvimento

Para a execução do script em ambiente local de desenvolvimento, é necessário a criação e ativação de um ambiente virtual.

```bash
python -m venv .spam
source .spam/bin/activate
```

Em seguida é necessário instalar os requirements.

```bash
pip install -r requirements.txt
```

Após a instalação dos requirements o scrip de classificação pode ser executado.

```bash
cd code
python spam_classificator.py
```

## Resultado

Ao fim da execução do script ele irá gerar um arquivo no diretório [data](./data) chamado Data_Tagged.csv que são os dados de teste classificados como SPAM (True False)

## Descrição_dos_Diretórios

- Code:
  - Notebook com toda parte de pre-processamento. Com a explicação de cada etapa realizada por meio de células de markdown.
  - Arquivo. py com o script para rodar o classificador.

- Data:
  - Base de dados em arquivo CSV, extraída de um aplicativo de mensagens instantâneas, separadas em treino e teste.
  - A base de treino possui: as mensagens, ids, e classificações e base de teste com apenas ids e mensagens.
  - Base de saída do modelo de classificação com as Tags se a mensagem é ou não do tipo SPAM.

- Model:
  - used_columms.pkl - features utilizadas.  
  - commom_spam_words.pkl - arquivo com as palavras mais comuns.  
  - numeric_columms.pkl - arquivo com todas colunas numéricas do conjunto.  
  - spacy.pkl - arquivo com o resultado do Spacy.  
  - spam.tree.pkl - Modelo de Árvore de Decisão.  
  - std_transform.pkl - arquivo com os dados transformados.
