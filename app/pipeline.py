import pandas as pd
from sqlalchemy import create_engine

# Dados de conexão para o banco de dados transacional (PostgreSQL)
transacional_config = {
    'host': 'transactional',
    'database': 'dvdrental',
    'user': 'postgres',
    'password': 'password',
    'port': '5432'
}

# Construir a URL de conexão para o banco de dados transacional
transacional_db_url = f"postgresql://{transacional_config['user']}:{transacional_config['password']}@{transacional_config['host']}:{transacional_config['port']}/{transacional_config['database']}"

# Configuração do banco de dados analítico (MySQL)
analitico_config = {
    'host': 'analytics',
    'database': 'analytics',
    'user': 'postgres',
    'password': 'password',
    'port': '5440',
}

# Construir a URL de conexão para o banco de dados analítico
analytics_db_url = f"postgresql://{analitico_config['user']}:{analitico_config['password']}@{analitico_config['host']}:{analitico_config['port']}/{analitico_config['database']}"

# Lista de todas as tabelas desejadas
TABLES = [
    'address', 'category', 'city', 'country', 'customer', 'film', 'film_actor', 
    'film_category', 'inventory', 'language', 'payment', 'rental', 'staff', 'store'
]

def extrair_tabela(engine, tabela):
    connection = engine.connect()

    # Leitura dos dados da tabela específica
    query = f"SELECT * FROM {tabela};"
    dados_tabela = pd.read_sql(query, connection)

    connection.close()
    
    return dados_tabela

def carregar_tabela_analytics(engine_analytics, tabela, dados_tabela):
    connection_analytics = engine_analytics.connect()

    # Carrega os dados na tabela correspondente no banco de dados analítico
    dados_tabela.to_sql(tabela, connection_analytics, index=False, if_exists='replace')

    connection_analytics.close()

if __name__ == "__main__":
    # Criar engine para o banco de dados transacional
    engine_transacional = create_engine(transacional_db_url)

    # Criar engine para o banco de dados analítico
    engine_analytics = create_engine(analytics_db_url)

    # Iterar sobre todas as tabelas desejadas
    for tabela_desejada in TABLES:
        print(f"Extraindo dados da tabela {tabela_desejada} do banco de dados transacional.")
        dados_tabela = extrair_tabela(engine_transacional, tabela_desejada)
        print(f"Dados extraídos. Carregando para a tabela {tabela_desejada} no banco de dados analítico.")
        carregar_tabela_analytics(engine_analytics, tabela_desejada, dados_tabela)
        print(f"Processo concluído para a tabela {tabela_desejada}.")