# a = [1,2,3,4,5]
# def double(x:list) -> list:
#     lol = 0
#     while lol != 5:
#         x[lol] = int(x[lol])*2
#         lol+=1
#     return x
# print(double(a))

def double(a:list) -> list:
    x=[]
    for y in a:
        x.append(y*2)
    return x
print(double([1,2,3]))
