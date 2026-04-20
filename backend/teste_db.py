import psycopg2
import sys

# Força o sistema a aceitar erros de decode na saída do terminal
sys.stdout.reconfigure(errors='replace')

try:
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="marmoraria_db",
        user="user_marmoraria",
        password="password_marmoraria",
        port="5433",
        client_encoding='utf8'
    )
    print("Conexão bem-sucedida!")
    conn.close()
except Exception as e:
    # Captura o erro bruto e tenta imprimir de forma segura
    print(f"Erro bruto detectado: {str(e).encode('ascii', 'replace').decode('ascii')}")