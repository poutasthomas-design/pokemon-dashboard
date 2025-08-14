import tkinter as tk
from tkinter import messagebox

def generate_description():
    nom = entry_nom.get()
    edition = entry_edition.get()
    rarete = entry_rarete.get()
    etat = entry_etat.get()
    prix = entry_prix.get()

    description = f"""🃏 Carte Pokémon : {nom}
📦 Édition : {edition}
✨ Rareté : {rarete}
📋 État : {etat}
💰 Prix : {prix} €
🔍 Description optimisée :
Découvrez la carte Pokémon {nom} issue de l'édition {edition}, classée comme {rarete}. Elle est en état {etat}, idéale pour les collectionneurs ou les joueurs souhaitant renforcer leur deck. Profitez de cette opportunité à seulement {prix} € ! Envoi rapide et soigné. N'hésitez pas à poser vos questions."""
    
    text_result.delete("1.0", tk.END)
    text_result.insert(tk.END, description)

root = tk.Tk()
root.title("Générateur de description eBay")

tk.Label(root, text="Nom de la carte").grid(row=0, column=0)
entry_nom = tk.Entry(root)
entry_nom.grid(row=0, column=1)

tk.Label(root, text="Édition").grid(row=1, column=0)
entry_edition = tk.Entry(root)
entry_edition.grid(row=1, column=1)

tk.Label(root, text="Rareté").grid(row=2, column=0)
entry_rarete = tk.Entry(root)
entry_rarete.grid(row=2, column=1)

tk.Label(root, text="État").grid(row=3, column=0)
entry_etat = tk.Entry(root)
entry_etat.grid(row=3, column=1)

tk.Label(root, text="Prix (€)").grid(row=4, column=0)
entry_prix = tk.Entry(root)
entry_prix.grid(row=4, column=1)

tk.Button(root, text="Générer la description", command=generate_description).grid(row=5, column=0, columnspan=2)

text_result = tk.Text(root, height=10, width=60)
text_result.grid(row=6, column=0, columnspan=2)

root.mainloop()
