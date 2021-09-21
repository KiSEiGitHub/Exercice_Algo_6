def hectare(L, l):
    surface = L * l
    hec = surface / 10000
    return hec, surface

def main():
    while True:
        longeur = float(input('longeur >> '))
        largeur = float(input('largeur >> '))
        hec, surface = hectare(longeur, largeur)
        print(f'Surface du terrain: {round(surface, 2)} m²')
        print(f'Soit: {round(hec, 2)} ha')
        print('-' * 50)


if __name__ == '__main__':
    main()