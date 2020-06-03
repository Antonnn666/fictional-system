first_number = int(input('First number:\n'))
second_number  = int(input('Second number:\n'))
a,b = first_number,second_number
while True:
    x = a % b
    print(a,'=',a//b,'*',b,'+',x)
    if x == 0:
        break
    a,b = b,x
print('\nThe greatest common divisor (GCD) of',first_number,'and',second_number,'is',b,'\n',first_number,'=',b,'*',first_number//b,'\n',second_number,'=',b,'*',second_number//b)