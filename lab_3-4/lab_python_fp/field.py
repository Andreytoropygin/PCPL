def field(items, *args):
    assert len(args) > 0
    result = []

    if len(args) == 1:
        for item in items: 
            result.append(item[args[0]])
    else:
        for item in items:
            result.append({i: item[i] for i in args if i in item.keys()})

    return result

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'}
]

if __name__ == '__main__':
    print(field(goods, 'title'))
    print(field(goods, 'title', 'price'))
