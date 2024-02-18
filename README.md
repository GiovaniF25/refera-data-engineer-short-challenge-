Este repositório foi desenvolvido para resolver o desafio proposto pela Refera-Tech, disponível no seguinte link: https://github.com/Refera-Tech/refera-data-engineer-short-challenge.

Resolução:
Implementação de uma pipeline que realiza a extração completa de todas as tabelas do banco de dados transacional, carregando os dados para o banco de dados analítico.
Construção da imagem Docker com a tag 'desafio-refera':

docker build -t desafio-refera .

Execução da imagem utilizando a rede host:

docker run --network host desafio-refera

