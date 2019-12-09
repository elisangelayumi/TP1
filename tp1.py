from random import uniform

ESSENCE_PRIX_MIN = 102
ESSENCE_PRIX_MAX = 150

prix_essence_du_jour = round(uniform(ESSENCE_PRIX_MIN, ESSENCE_PRIX_MAX), 1)

#inputs

nom = input('Quel est votre nom? ')

print("Salut", nom)

prix_max_desire = float(input("Quel est le prix maximum que vous voulez payer par litre d'essence? (En dollars) "))
prix_max_cents = float(prix_max_desire * 100) #convertir le prix en cents

capacite = (int(input("Quelle est la capacité maximale de votre reservatoire? (En litres) ")))

periode = (int(input("Quelle est la periode que vous voulez faire l'évaluation? (en semaines) ")))
print("\n")

# variables

x = 1
somme_montant_depense = 0
somme_jours_travail = 0
somme_jours_maison = 0

# programme

while x <= periode:
    print("<< Semaine", x, ">>")
    print('''-'''*15, "\n")
    x += 1
    for i in range (1,8):
        prix_essence_du_jour = round(uniform(ESSENCE_PRIX_MIN, ESSENCE_PRIX_MAX), 1)
        print("Jour", i, ":", prix_essence_du_jour)

        if prix_essence_du_jour > prix_max_cents:
            print(nom, "a decidé de rester à la maison aujourd'hui", "\n")
            jours_maison = 1
            somme_jours_maison += jours_maison

        elif prix_essence_du_jour <= prix_max_cents:
            print(nom, "viens de faire le plein pour aller au travail", "\n")
            montant_depense = (prix_essence_du_jour * capacite) / 100   #calculer le côut de faire le pein et convertir en dollars
            somme_montant_depense += montant_depense
            jours_travail = 1
            somme_jours_travail += jours_travail


print('''='''*60, "\n")

# Calculs

litres_totales = capacite * somme_jours_travail

# Informations sommaire

print(f'Consommation totale: {litres_totales:.2f} litres.')
print(f'Montant total dépensé: {somme_montant_depense:.2f}$.')
print(f'{nom} est allé(e) au travail {somme_jours_travail:d} jours.')
print(f'{nom} a passé {somme_jours_maison:d} jours à la maison.' "\n")

# optionnel

jours_total = periode * 7  # calculer combien des jours il y a dans la periode analysé
if somme_jours_maison > (jours_total/2):
    print(f'Les factures ne vont pas se payer toutes seules {nom}!' "\n")

print('''='''*60, "\n")

input("Appuyez sur Enter pour terminer")