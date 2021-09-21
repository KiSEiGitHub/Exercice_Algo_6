def main():
    n = int(input('n >> '))
    a = 2 / n
    b = 1 / n + 1 / (2 * n) + 1 / (3 * n) + 1 / (6 * n)

    print(f'a: {a}')
    print(f'b: {b}')

if __name__ == '__main__':
    main()