import pandas as pd

cartes = [
    {"nom": "Pikachu VMAX Rainbow Rare", "prix_liste": 43.62, "prix_marche": 60.0},
    {"nom": "Charizard GX Full Art", "prix_liste": 60.0, "prix_marche": 75.0},
    {"nom": "Rayquaza VMAX", "prix_liste": 35.0, "prix_marche": 50.0},
    {"nom": "Lucario GX", "prix_liste": 22.0, "prix_marche": 28.0}
]

bonnes_affaires = []

for carte in cartes:
    reduction = 100 * (1 - carte["prix_liste"] / carte["prix_marche"])
    if reduction >= 20:
        carte["reduction"] = round(reduction, 2)
        bonnes_affaires.append(carte)

df = pd.DataFrame(bonnes_affaires)
print("Bonnes affaires détectées :")
print(df)
