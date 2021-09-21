class calcul:
    def __init__(self):
        self.x = 2
        self.y = -2
        self.z = -4
        self.s = 1
        self.t = 3

    def calc_z(self):
        return self.x + self.y

    def calc_t(self):
        return self.z * self.t

    def calc_s(self):
        return 3 * self.x

    def calc_x(self):
        return -self.t

    @staticmethod
    def calc_y():
        return 8

    @staticmethod
    def affich(a, b, c, d, e):
        print(f'x: {a}')
        print(f'y: {b}')
        print(f'z: {c}')
        print(f's: {d}')
        print(f't: {e}')


class calcul2:
    def __init__(self):
        self.x = 2
        self.y = -2
        self.z = -4
        self.s = 1
        self.t = 3

    def calc_t(self):
        return - self.y

    def calc_z(self):
        return self.t ** 2

    def calc_x(self):
        return self.z - self.x

    def calc_t2(self):
        return self.x

    @staticmethod
    def calc_y():
        return 8

    @staticmethod
    def affich(a, b, c, e):
        print(f'x: {a}')
        print(f'y: {b}')
        print(f'z: {c}')
        print(f's: 0')
        print(f't: {e}')


def main():
    print('Calcul 1')
    clc = calcul()
    clc.affich(
        clc.calc_x(), clc.calc_y(), clc.calc_z(),
        clc.calc_s(), clc.calc_t()
    )
    print('-' * 50)

    print('Calcul 2')
    clc2 = calcul2()
    clc2.affich(
        clc2.calc_x(), clc2.calc_y(), clc2.calc_z(),
        clc2.calc_t()
    )


if __name__ == '__main__':
    main()