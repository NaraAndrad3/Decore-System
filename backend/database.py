from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexão (usando as credenciais do seu docker-compose)
SQLALCHEMY_DATABASE_URL = "postgresql://user_marmoraria:password_marmoraria@127.0.0.1:5433/marmoraria_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Função para obter a sessão do banco nas rotas
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()