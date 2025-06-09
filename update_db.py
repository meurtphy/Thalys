import sqlite3

conn = sqlite3.connect('thalys.db')
c = conn.cursor()

# On ajoute une colonne 'status' si elle n'existe pas
try:
    c.execute("ALTER TABLE remontées ADD COLUMN status TEXT DEFAULT 'ouvert'")
    print("✅ Colonne 'status' ajoutée.")
except sqlite3.OperationalError as e:
    print("⚠️ Colonne 'status' existe déjà ou erreur :", e)

conn.commit()
conn.close()
