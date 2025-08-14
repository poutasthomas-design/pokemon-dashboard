from flask import Flask, request, redirect, render_template_string
import sqlite3

app = Flask(__name__)
DB_NAME = "cartes.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS cartes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT,
        edition TEXT,
        etat TEXT,
        prix REAL
    )""")
    conn.commit()
    conn.close()

init_db()

HTML = """
<!doctype html>
<title>Dashboard Cartes Pokémon</title>
<h1>Ajouter une carte</h1>
<form method=post>
  Nom: <input type=text name=nom><br>
  Édition: <input type=text name=edition><br>
  État: <input type=text name=etat><br>
  Prix: <input type=number step=0.01 name=prix><br>
  <input type=submit value=Ajouter>
</form>

<h2>Cartes enregistrées</h2>
<ul>
{% for carte in cartes %}
  <li>{{ carte[1] }} - {{ carte[2] }} - {{ carte[3] }} - {{ carte[4] }} €
      <a href="/delete/{{ carte[0] }}">Supprimer</a></li>
{% endfor %}
</ul>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nom = request.form["nom"]
        edition = request.form["edition"]
        etat = request.form["etat"]
        prix = request.form["prix"]
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("INSERT INTO cartes (nom, edition, etat, prix) VALUES (?, ?, ?, ?)", (nom, edition, etat, prix))
        conn.commit()
        conn.close()
        return redirect("/")
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM cartes")
    cartes = c.fetchall()
    conn.close()
    return render_template_string(HTML, cartes=cartes)

@app.route("/delete/<int:id>")
def delete(id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM cartes WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
