# Use a imagem oficial do Python como base
FROM python:3.8-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia os arquivos necessários para o diretório de trabalho
COPY . .

# Instala as dependências
RUN pip install pandas sqlalchemy psycopg2-binary

# Comando padrão a ser executado quando o container for iniciado
CMD ["python", "app/pipeline.py"]