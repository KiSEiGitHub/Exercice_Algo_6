def main():
    nb_personne = int(input('Combien de personne: '))
    forfait_skie = 170 if nb_personne <= 5 else 210
    prix_location = 700
    prix_total = prix_location + forfait_skie / nb_personne
    print(f'Prix total par personne = {round(prix_total, 2)}€')

if __name__ == '__main__':
    main()