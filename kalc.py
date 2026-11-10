def discriminant(a, b, c):
    """Функция для нахождения дискриминанта"""
    dis = (b ** 2) - (4 * a * c)

    return dis

def solution(a, b, c):
    """Функция для нахождения корней квадратного уравнения"""
    dis = discriminant(a, b, c)
    if dis > 0:
        d1 = (-b + (dis ** 0.5)) / (2 * a)
        d2 = (-b - (dis ** 0.5)) / (2 * a)
        print (f'Уравнение имеет два корня: х1 = {d1}, х2 = {d2}.')
        return d2, d1
    elif dis == 0:
        d = -b / (2 * a)
        print (f'Уравнение имеет один корень: х = {d}.')
        return d
    else:
        return 'Корней нет и даже не жди :)'
