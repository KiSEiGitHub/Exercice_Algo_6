def main():
    t = [int(input('note >> ')) for _ in range(3)]
    print(f'moyenne = {round(sum(t) / 3, 2)}')


if __name__ == '__main__':
    main()