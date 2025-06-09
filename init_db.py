import sqlite3

# Connexion à la base (fichier créé s'il n'existe pas)
conn = sqlite3.connect('thalys.db')

# Création du curseur (permet d'exécuter des commandes SQL)
c = conn.cursor()

# Création de la table pour stocker les remontées
c.execute('''
    CREATE TABLE IF NOT EXISTS remontées (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        poste TEXT,
        type_remontee TEXT,
        message TEXT
    )
''')

# Sauvegarde + fermeture
conn.commit()
conn.close()

print("Base et table créées ✅")
