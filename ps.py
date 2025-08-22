#simple_calculator
a=int(input('enter a value'))
b=int(input('enter a value'))
ope=str(input('enter a string'))
if ope=='add':
    print(a+b)
elif ope=='subtract':
    print(a-b)
elif ope=='multiply':
    print(a*b)
elif ope=='division':
    if b!=0:
        print(a/b)
        print(a//b)
        print(a%b)
    else:
        print('division by zero not possible')
else:
    print('invalid operation')