import requests
import json
import os

# Liste des pays à extraire (tu peux changer)
countries = ["FR", "DE", "IT"]
url = "https://api.openaq.org/v3/locations"

# Dossier de sortie
output_path = "data/raw_data.json"

# Paramètres de requête
params = {
    "limit": 1000,
    "parameter": "pm25",
    "country": ",".join(countries),
    "format": "json"
}

print("📡 Récupération des données depuis OpenAQ...")

headers = {
    "accept": "application/json",
    "X-API-Key": os.getenv('OPENAQ_API_KEY')
}

response = requests.get(url, params=params, headers=headers)

print("🔑 Clé API utilisée :", os.getenv("OPENAQ_API_KEY"))
if response.status_code == 200:
    data = response.json()
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"✅ Données enregistrées dans {output_path}")
else:
    print("❌ Erreur lors de l’appel API :", response.status_code)
    

