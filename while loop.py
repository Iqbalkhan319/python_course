### Basic while loop
x=6
while x:
    x-=1
    print(x)


L=['red','green','blue']
while L:
    #L.pop() print(L)
    print(L.pop())

x='payel'
while x:
    #x=x[0:] print(x)
    print(x)
    x = x[1:]


#### Break in While loop
x=6
while x:
    print(x)
    x-=1
    if x==2:
        break


### continue in while loop
x=10
while x:
    x-=1
    if x%2!=0:
        continue
    print(x)


### Else while loop
x=10
while x:
    print(x)
    x-=2
else:
    print('Done!')


x=0
while x:
    print(x)
    x-=2
else:
    print('Done!')



x=6
while x:
    print(x)
    x-=1
    if x==2:
        break
else:
    print('Done!')


### While True game
#while True:
   # name=input('Enter your name:')
   # if name=='stop':
   #     break
   # print('Hello,',name)

### While loop seris
#(1+2+3+4+...+100=?)

x=0
while x:
    x=x+1
    print(x)

#1+2+3+....+100
num=1
sum=0
while (num<=100):
    sum=num+sum
    num=num+1
print(sum)

n=100
s=int(n*(n+1)/2)
print(s,type(s))


### 1^2+2^2+3^2+....
n=1
s=0
while (n<=100):
    s=(n**2)+s
    n=n+1
print(s)


### 1^3+2^3+3^3+....+100^3
n=1
s=0
while (n<=100):
    s=(n**3)+s
    n=n+1
print(s)


#sum of natural number
while True:
    n=int(input("Enter number:"))
    s=0
    if n<0:
        print("negative or zero")
    else:
        while n>0:
            s=n+s
            n=n-1
        print(s)


