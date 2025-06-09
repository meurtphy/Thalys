import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Connexion à la base SQLite
conn = sqlite3.connect('thalys.db')

# Charger les données dans un DataFrame
df = pd.read_sql_query("SELECT * FROM remontées", conn)
conn.close()

# Affichage simple des données
print("📊 Données :\n", df)
print("\n📌 Total :", len(df))
print("\n🧮 Répartition par type :\n", df['type_remontee'].value_counts())

# 📈 Affichage graphique
df['type_remontee'].value_counts().plot(kind='bar')
plt.title("Répartition des types de remontées")
plt.xlabel("Type de remontée")
plt.ylabel("Nombre")
plt.tight_layout()
plt.show()
