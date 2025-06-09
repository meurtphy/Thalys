from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import matplotlib.pyplot as plt
import io
import base64
import pandas as pd

app = Flask(__name__)

# Route : Formulaire
@app.route('/')
def index():
    return render_template('index.html')

# Route : Enregistrement des données
@app.route('/submit', methods=['POST'])
def submit():
    poste = request.form['poste']
    type_remontee = request.form['type']
    message = request.form['message']

    conn = sqlite3.connect('thalys.db')
    c = conn.cursor()
    c.execute("INSERT INTO remontées (poste, type_remontee, message, status) VALUES (?, ?, ?, ?)",
              (poste, type_remontee, message, 'ouvert'))
    conn.commit()
    conn.close()

    return redirect(url_for('tableau'))

# Route : Affichage tableau + graphique
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import matplotlib.pyplot as plt
import io
import base64
import pandas as pd

app = Flask(__name__)

# Route : Formulaire
@app.route('/')
def index():
    return render_template('index.html')

# Route : Enregistrement des données
@app.route('/submit', methods=['POST'])
def submit():
    poste = request.form['poste']
    type_remontee = request.form['type']
    message = request.form['message']

    conn = sqlite3.connect('thalys.db')
    c = conn.cursor()
    c.execute("INSERT INTO remontées (poste, type_remontee, message, status) VALUES (?, ?, ?, ?)",
              (poste, type_remontee, message, 'ouvert'))
    conn.commit()
    conn.close()

    return redirect(url_for('tableau'))

# Route : Affichage tableau + graphique
@app.route('/tableau')
def tableau():
    conn = sqlite3.connect('thalys.db')
    c = conn.cursor()
    c.execute("SELECT * FROM remontées")
    donnees = c.fetchall()

    # Utiliser pandas pour compter les types
    df = pd.read_sql_query("SELECT * FROM remontées", conn)
    conn.close()

    # Générer le graphique
    img = io.BytesIO()
    if not df.empty:
        df['type_remontee'].value_counts().plot(kind='bar', color='#005BAC')
        plt.title("Répartition des types de remontées")
        plt.xlabel("Type")
        plt.ylabel("Nombre")
        plt.tight_layout()
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        graph_url = 'data:image/png;base64,' + base64.b64encode(img.read()).decode()
    else:
        graph_url = None

    return render_template('tableau.html', donnees=donnees, graph_url=graph_url)

# Route : Marquer comme résolu
@app.route('/resolve/<int:id>')
def resolve(id):
    conn = sqlite3.connect('thalys.db')
    c = conn.cursor()
    c.execute("UPDATE remontées SET status = 'résolu' WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('tableau'))

# Route : Supprimer une ligne
@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect('thalys.db')
    c = conn.cursor()
    c.execute("DELETE FROM remontées WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('tableau'))

if __name__ == '__main__':
    app.run(debug=True)


# Route : Marquer comme résolu
@app.route('/resolve/<int:id>')
def resolve(id):
    conn = sqlite3.connect('thalys.db')
    c = conn.cursor()
    c.execute("UPDATE remontées SET status = 'résolu' WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('tableau'))

# Route : Supprimer une ligne
@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect('thalys.db')
    c = conn.cursor()
    c.execute("DELETE FROM remontées WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('tableau'))

if __name__ == '__main__':
    app.run(debug=True)
