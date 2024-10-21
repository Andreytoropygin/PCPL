import time
from field import field
from gen_random import gen_random
from unique import Unique
from print_result import print_result
from cm_timer import cm_timer_1, cm_timer_2

#field
goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
]

print(", ".join(list(map(str, field(goods, 'title')))))

#gen_random
print(", ".join(list(map(str, gen_random(5, 0, 100)))))

#Unique
data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
a = Unique(data)

for _ in range(2):
    print(next(a))

data = gen_random(10, 1, 3)
a = Unique(data)

for _ in range(3):
    print(next(a))
 
data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
a = Unique(data, ignore_case=True)

for _ in range(4):
    print(next(a))

#print_result
@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()

# cm_timer
with cm_timer_1():
    time.sleep(1)

with cm_timer_2():
    time.sleep(1)
