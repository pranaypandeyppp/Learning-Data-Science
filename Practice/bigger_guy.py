a = input('Enter the 1st number: ') # Takes the first number
b = input('Enter the 2nd number: ') # Takes the second mumber
def bigger_guy(a,b):
    '''
    bigger_guy function takes two numbers as input and prints the biggest number
    
    Parameters taken are 'a' and 'b'
    '''
    if a>b:     # Checks whether a is greater than b
        return a
    elif b>a:       # Checks whether b is greater than a
        return b
    else:
        return 'Both are Equal'
print(f'The biggest number is: {bigger_guy(a, b)}') # We are calling the biger_guy function to print the output