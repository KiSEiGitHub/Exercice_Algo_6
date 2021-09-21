def main():
    while True:
        x = int(input('x >> '))
        y = x / 9 if x % 9 == 0 else x - 9

        print(f'y = {y}')

        print('-' * 50)


if __name__ == '__main__':
    main()