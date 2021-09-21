def main():
    c = ""
    print('Entrer une chaine de plus de 9 caractères')
    while len(c) < 9:
        c = input('chaine >> ')

    d = c[8]
    e = c[0]
    f = c[6]
    g = c[7]
    s = d + e + f + g

    print(s)


if __name__ == '__main__':
    main()