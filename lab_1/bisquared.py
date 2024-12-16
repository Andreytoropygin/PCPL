import sys

def get_coef(index, prompt):
    try:
        coef_str = sys.argv[index]
    except:
        print(prompt)
        coef_str = input()
    coef = float(coef_str)
    return coef


def solve(a, b, c):
    D = b*b - 4*a*c
    roots = []
    if D > 0:
        t1 = (-b + D**0.5) / 2 / a
        roots += solve_square(t1)
        t2 = (-b - D**0.5) / 2 / a
        roots += solve_square(t2)
    elif D == 0:
        t = -b / 2 / a
        roots += solve_square(t)
    return roots


def solve_square(n):
    roots = []
    if n > 0: 
        roots.append(n**0.5)
        roots.append(-n**0.5)
    elif n == 0:
        roots.append[n]
    return roots
    

a = get_coef(1, 'Введите коэффициент А:')
b = get_coef(2, 'Введите коэффициент B:')
c = get_coef(3, 'Введите коэффициент C:')

roots = solve(a, b, c)
roots.sort()
match len(roots):
    case 0:
        print("Не найдено действительных корней")
    case 1:
        print("Один корень: {}".format(roots[0]))
    case 2:
        print("Два корня: {}, {}".format(roots[0], roots[1]))
    case 3:
        print("Три корня: {}, {}, {}".format(roots[0], roots[1], roots[2],))
    case 4:
        print("Четыре корня: {}, {}, {}, {}".format(roots[0], roots[1], roots[2], roots[3]))
