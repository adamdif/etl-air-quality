import psycopg2
import os

print("Hello, World!")

# Test de connexion à PostgreSQL
try:
    connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS")
    )
    print("✅ Connexion réussie à PostgreSQL !")
    connection.close()
except Exception as e:
    print("❌ Erreur de connexion :", e)
