import sqlite3

conn = sqlite3.connect('thalys.db')
c = conn.cursor()

c.execute("SELECT * FROM remontées")
lignes = c.fetchall()

# Nouvelle ligne ici :
print(f"Nombre de lignes trouvées : {len(lignes)}")

for ligne in lignes:
    print(ligne)

conn.close()
