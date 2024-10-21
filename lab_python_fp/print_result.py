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
