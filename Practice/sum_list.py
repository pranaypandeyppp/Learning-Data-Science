def sum_list(a:list) -> int:
    num=0
    for x in a:
        num = num+x
    return num
print(sum_list([1,2,3]))