n = int(input("Enter your value:"))
l = n % 10
for i in range(len(str(n))):
    f=n%10
    n= n // 10
print("First digit is {} and Last digit is {}".format(f,l))