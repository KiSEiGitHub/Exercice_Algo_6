def main():
    x = float(input("x = "))
    y = float(input("y = "))
    x, y = y, x
    print(x)
    print(y)


if __name__ == '__main__':
    main()