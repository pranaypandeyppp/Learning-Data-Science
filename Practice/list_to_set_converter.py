# def unique(a):
''' 
unique is a function thet coverts a list into a set
'''
#     return set(a)
unique = lambda a:set(a)
'''
same unique function is converted into a lambda function
normal function and lambda function perform the same operation, but in a different way
Syntax of lambda function is a bit different, that's it
'''
print(unique([1,2,3,3,4,4,7,8]))
