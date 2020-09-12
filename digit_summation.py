#Summation of digit
num=int(input("Enter your digit:"))     #Take input from keyboard. Ex: num=1234
sum = 0                                 #sum=0
for i in range(len(str(num))):          #find lenght of num value and convert num value integer to string. It's loop time
    digit = num%10                      #digit=1234%10=4___123%10=3
    sum = sum+digit                     #sum=0+4=4____3+4=7
    num = num//10                       #num=1234//10=123____123//10=12
print("The Summation of digit",sum)     #Final output

