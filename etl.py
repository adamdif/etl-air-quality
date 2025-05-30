import psycopg2
import os
import time

print("🔄 Démarrage du script ETL")

# Connexion à PostgreSQL avec 5 tentatives max
for i in range(5):
    try:
        print(f"🔌 Tentative {i+1} de connexion à PostgreSQL...")
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS")
        )
        print("Connexion réussie à PostgreSQL !")
        conn.close()
        break
    except Exception as e:
        print("Connexion échouée :", e)
        time.sleep(3)
