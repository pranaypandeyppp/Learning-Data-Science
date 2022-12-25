def word_frequency(a:str) -> dict:
    x = {}
    b = a.split()
    for num in b:
        if num not in x:
            x[num] = 1
        else:
            x[num] = x[num]+1
    return x
print(word_frequency('I love myself coz loving is love'))