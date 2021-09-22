def capital(argent, annee, taux):
    for _ in range(1, annee):
        argent += 80 * taux / 100
    return argent


def main():
    while True:
        argent = float(input('argent >> '))
        annee = int(input('années >> '))
        taux = float(input('taux >> '))
        somme = capital(argent, annee, taux)
        print(f'somme total au bout de {annee} ans: {round(somme, 2)} €')
        print('-' * 50)


if __name__ == '__main__':
    main()