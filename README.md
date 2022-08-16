# Classificador de SPAM - NetLab

#### Autor: [Felipe Maia](https://www.linkedin.com/in/felipe-b-maia/)

<br/>

A proposta deste projeto é desenvolver um classificador de SPAM utilizando uma base de dados de um aplicativo de mensagens instantâneas e medir a eficiência do modelo.

## Sumário

- [Sobre](#sobre)
- [Desenvolvimento](#desenvolvimento)
- [Implantação](#implantação)

## Sobre

Este projeto tem como objetivo utilizar uma base de dados de um aplicativo de mensagens instantâneas e, a partir desta base, desenvolver um modelo de Classificação utilizando técnicas de Machine Learning. O projeto consiste em um script python que utiliza a biblioteca do Scikit-Learn para realizar o Tokenizer e Classificador, e a plataforma Natural Language Toolkit (NLTK) foi usada para construir a análise de texto. Após a construção do modelo os dados foram inseridos no Docker para serem visualizados e manipulados.

## Desenvolvimento

Para a execução do script em ambiente local de desenvolvimento, é utilizada a ferramenta docker-compose através do seguinte comando:

```bash
$ docker-compose up
```

Após a execução do script, os dados estarão indexados no Docker e poderão ser visualizados e manipulados através do mesmo na url [http://localhost:5601](http://localhost:5601)

## Implantação

Por ora o projeto não contempla um processo automatizado de implantação. Mas a arquitetura e os procedimentos necessários para implantação do projeto em Cloud estão descritos em um documento markdown à parte que pode ser acessado [CLICANDO AQUI.](./docs/deployment.md)
<br/>
