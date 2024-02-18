Desafio da Refera
link desafio: https://github.com/Refera-Tech/refera-data-engineer-short-challenge

Criação de uma pipeline que faz a extração total de todas as tabelas do banco de dados transactional carregando os dados para o banco de dados analytics.
Construção de a imagem Docker com a tag 'desafio-refera'
:docker build -t desafio-refera:

Execução da imagem utilizando a rede host:
docker run --network host desafio-refera
