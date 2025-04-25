# Dockerfile
FROM python:3.13-slim

# Crée le répertoire de travail dans le conteneur
WORKDIR /app

# Copie les fichiers locaux dans le conteneur
COPY . /app

# Installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Point d'entrée pour exécuter le pipeline ETL complet
CMD ["python", "etl.py"]
