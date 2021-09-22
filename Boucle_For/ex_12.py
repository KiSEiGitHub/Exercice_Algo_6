class capital:
    def __init__(self, argent, taux, annee):
        self.argent = argent
        self.taux = taux
        self.annee = annee

    def capital1(self):
        for _ in range(1, self.annee):
            self.argent += 80 * self.taux / 100
        return self.argent

    def capital2(self):
        a = 0
        somme = 0
        while somme <= self.argent * 2:
            somme += self.argent + 80
            a += 1
        return a


def main():
    while True:
        argent = float(input('argent >> '))
        annee = int(input('années >> '))
        taux = float(input('Taux >> '))

        resultat = capital(argent, taux, annee)

        print(f'Somme total au bout de {annee} ans: {round(resultat.capital1(), 2)} €')
        print(f'La somme aura doubler en {resultat.capital2()} ans')

        print('-' * 50)


if __name__ == '__main__':
    main()