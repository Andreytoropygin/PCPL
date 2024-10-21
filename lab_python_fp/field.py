def field(items, *args):
    assert len(args) > 0
    result = []

    if len(args) == 1:
        for item in items: 
            result.append(item[args[0]])
    else:
        for item in items:
            result.append({i: item[i] for i in args if item[i]})

    return result
