def factorial(n):
    if(n<2):
        return 1
    return n*factorial(n-1)

num=int(input('enter a number: '))
print('it\'s factorial is = ',factorial(num))
