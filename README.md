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

Este projeto tem como objetivo utilizar uma base de dados de um aplicativo de mensagens instantâneas e, a partir desta base, desenvolver um modelo de Classificação utilizando técnicas de Machine Learning. O projeto consiste em um script python que utiliza a biblioteca do Scikit-Learn para realizar o Tokenizer e Classificador, e a plataforma Natural Language Toolkit (NLTK) foi usada para construir a análise de texto. Após a construção do modelo os dados foram inseridos no Docker para serem visualizados e manipulados.

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

Ao fim da execução do script ele irá gerar um arquivo no diretório data chamado Data_Tagged.csv que são os dados de teste classificados como SPAM (True False)

## Descrição dos Diretórios

- Code:
  Notebook com toda parte de pre-processamento.
  Arquivo. py com o script para rodar o classificador.

- Data:
  Base de dados em arquivo CSV, extraída de um aplicativo de mensagens instantâneas, separadas em treino e teste.
  A base de treino possui: as mensagens, ids, e classificações e base de teste com apenas ids e mensagens.
  Base de saída do modelo de classificação com as Tags se a mensagem é ou não do tipo SPAM.

- Model:
  used_columms.pkl - features utilizadas.
  
  
  commom_spam_words - base com as palavras mais comuns.
  
  numeric_columms.plk - base com todas colunas numéricas do conjunto.
  
  spacy.plk - base com o resultado do Spacy.
  
  spam.tree.plk - Modelo de Árvore de Decisão.
  
  std_transform.plk - base com os dados transformados.
