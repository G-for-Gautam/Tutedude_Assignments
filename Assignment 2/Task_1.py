try:
    num=int(input('enter a number: '))
    if(num % 2 == 0):
        print(num ,'is an even number')
    else:
        print(num, 'is an odd number')
except ValueError:
    print('please enter a number')
