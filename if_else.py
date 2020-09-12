### Find negative or positive number

"""n=float(input('Enter number:'))
if (n<=0):
    if (n<0):
        print('negative')
    elif (n==0):
         print('zero')
else:
     print('positive')

### Find even or odd number
n=int(input('Enter number:'))
if n%2==0:
    print('{0} is even'.format(n))
else:
    print('{0} is odd'.format(n))"""

### Find prime number
n=int(input('Enter number:'))
if n>1:
    for i in range(2,n):
        if (n%i==0):
            print('{0 is not prime number} M.format(n)')
    print('{0 is prime number}'.format(n))
else:
    print('{0 is not prime number}'.format(n))
