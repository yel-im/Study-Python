def FilterList(x):
    return x > 0

print(list(filter(FilterList, [1, -3, 2, -5, 8, -3])))

# print(list(filter(lambda a:a>0, [1, -3, 2, -5, 8, -3])))

