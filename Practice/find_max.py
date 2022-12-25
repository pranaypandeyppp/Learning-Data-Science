def find_max(a:list) ->int:
    num = a[0]
    for x in a:
        if x>num:
            num = x
    return num
print(find_max([1,2,3,-10,5]))