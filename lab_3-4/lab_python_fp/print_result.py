def print_result(func):
    
    def wrapper(*args, **kwargs):
        print(func.__name__)
        result = func(*args, **kwargs)
        if type(result) == list:
                print("\n".join(map(str, result)))

        elif type(result) == dict:
                for i in result.keys():
                    print(i, '=', result[i])

        else:
            print(result)
        return func(*args, **kwargs)
        
    return wrapper         


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
    test_1()
    test_2()
    test_3()
    test_4()
