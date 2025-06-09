# Thalys – Carnet de Bord Digital pour Atelier Industriel

Ce projet a été réalisé dans le cadre d’une candidature à un poste en transformation digitale chez Thales (site de Thonon-les-Bains).  
Il propose une solution simple et humaine pour collecter, visualiser et exploiter les retours terrain d’un atelier industriel, dans une logique d’amélioration continue.

---

## 🎯 Objectif

Créer un outil digital éthique et utile permettant :

- La remontée d’informations terrain (anomalies, suggestions, remarques)
- Leur visualisation claire dans un tableau centralisé
- Leur analyse automatique avec un graphique dynamique
- La gestion du cycle de vie des remontées (résolu / ouvert / suppression)
- Une interface sobre, utilisable facilement en contexte industriel

---

## 🌍 Pourquoi ce projet ?

> "Je ne veux pas juste participer à la transformation digitale. Je veux qu’elle soit éthique, utile et humaine. Ce projet, je l’ai conçu pour que la tech **aide**, pas qu’elle **surveille**."

---

## 🛠️ Stack technique

- **Python 3.10**
- **Flask** (micro-framework web)
- **SQLite** (base de données légère, locale)
- **Pandas** (traitement de données)
- **Matplotlib** (visualisation)
- **Bootstrap 5** (design sobre et responsive)

---

## 🖼️ Aperçu

- Interface formulaire responsive
- Visualisation claire des remontées avec filtres
- Graphique dynamique intégré dans la page
- Actions directes : marquer comme résolu, supprimer

---

## 📦 Fonctionnalités

| Fonction                       | Description |
|-------------------------------|-------------|
| 📥 Saisie de remontée         | Formulaire HTML simple |
| 💾 Sauvegarde locale          | Via SQLite |
| 📊 Analyse automatique        | Nombre de remontées par type |
| 📋 Affichage par tableau      | Interface claire, triée |
| ✅ Gestion des statuts        | Ouvert / Résolu |
| 🔍 Filtres par statut         | Navigation rapide |
| 🧼 Suppression manuelle       | Ligne par ligne |

---

## ▶️ Lancer le projet

1. Cloner le dépôt
2. Installer les dépendances :

```bash
pip install flask pandas matplotlib
Initialiser la base de données (si besoin)

bash
Copier
Modifier
python init_db.py
Lancer le serveur :

bash
Copier
Modifier
python app.py
Ouvrir http://localhost:5000

✅ Ce que ça démontre
Capacité à proposer une solution métier simple et fonctionnelle

Maîtrise des outils de transformation digitale (de la collecte à l’analyse)

Attention portée à l’ergonomie et à l’éthique

Approche agile : itératif, adaptable, efficace

🙋‍♂️ Auteur
Erwan – Développeur en formation, passionné par l’impact humain de la tech.
Projet conçu pour postuler à une alternance chez Thales, dans un esprit d’initiative, de rigueur et d’innovation utile.

💡 À venir
Export CSV

Authentification

Historique des actions

Interface multi-utilisateur (en option)

yaml
Copier
Modifier
