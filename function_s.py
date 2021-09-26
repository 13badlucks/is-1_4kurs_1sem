def triaangle(k1, k2, h1):
    # k1=int(input('длинна 1 стороны = '))
    # k2=int(input('длинна 2 стороны = '))
    # h1=int(input('длинна 3 стороны = '))

    if (k1 < (k2 + h1)) and (k2 < (k1 + h1)) and (h1 < (k2 + k1)):
        # data = 'это треугольник'
        # print(data)
        if h1 ** 2 == k1 ** 2 + k2 ** 2 or k1 ** 2 == h1 ** 2 + k2 ** 2 or k2 ** 2 == k1 ** 2 + h1 ** 2:
            data = 'треугольник прямой'
            print(data)
        if h1 ** 2 < k1 ** 2 + k2 ** 2 or k1 ** 2 < h1 ** 2 + k2 ** 2 or k2 ** 2 < k1 ** 2 + h1 ** 2:
            data = 'треугольник остроугольный'
            print(data)
            if k1 == k2 == h1:
                data = " равносторонний"
                print(data)
        if h1 ** 2 > k1 ** 2 + k2 ** 2 or k1 ** 2 > h1 ** 2 + k2 ** 2 or k2 ** 2 > k1 ** 2 + h1 ** 2:
            data = 'треугольник тупоугольный'
            print(data)
    else:
        data = 'это не треугольник'
        print(data)
    return data

def stipendion(a, b, c, n):

    # a = int(input("Введите оценку 1: "))
    # b = int(input("Введите оценку 2: "))
    # c = int(input("Введите одно значение из 2-х (y или n, где y - сессия сдана вовремя, а n - после указанного срока): "))

    if (a > 3) and (b > 3) and (c=="y"):
        if (a == 4) and (b == 4):
            pays = n
            data = f"Студент будет получать стипендию в размере: {pays} р."
            # print(data)
    if (a == 4 and b == 5) or (a == 5 and b == 4):
        pays = ( n + ((n/100)*25))
        data = f"Студент будет получать стипендию в размере: {pays}р."
        # print(data)
    if (a == 5 and b == 5):
        pays = (n + ((n/100)*50))
        data = f"Студент будет получать стипендию в размере: {pays}р."
        # print(data)
    if (a < 4) or (b < 4) or (c == "n"):
        data = "Студент не будет получать стипендию"
        # print(data)

    return str(data)