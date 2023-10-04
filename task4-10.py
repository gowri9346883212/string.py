#even or not
num = int(input("enter a number:"))
if (num % 2) == 0:
    print("given numberis even.")
else:
    print("given number is not.")

#prime or not
num=int(input("enter the number:"))
if num==1:
    print("is not prime number")
if num>1:
    for n in range(2,num):
        if num%2==0:
            print(num,"is not prime number")
            break
else:
    print(num,"is prime number")

#palindrome or not
n=int(input("enter the number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=(rev*10)+dig
    n=n//10
if(temp==rev):
    print("the number is a palindrome.")
else:
    print("the number is not a palindrome.")

#armstrong or not
num=input('enter number:')
sum=0
for i in num:
    sum+=int(i)**3
if sum==int(num):
    print('armstrong')
else:
    print('not armstong')

#operator
#arthematic
a= input("enter a value:")
b= input("enter b value:")
print(int(a) + int(b))

a= input("enter a value:")
b= input("enter b value:")
print(int(a) - int(b))

a= input("enter a value:")
b= input("enter b value:")
print(int(a) * int(b))#

a= input("enter a value:")
b= input("enter b value:")
print(int(a) % int(b))

a= input("enter a value:")
b= input("enter b value:")
print(int(a) // int(b))

#address
hno = (input("enter a h-no:"))
pincode = (input("enter  a pin:"))
state = (input("Enter a state:"))
street = input("enter a street name:")
if (hno.isnumeric() and pincode(len) == 6):
        print("address is valid")
elif (hno.isalpha() and pincode.isalpha()):
        print("address is  valid")
elif (state.isalpha() and street.isalpha()):
        print("address is valid")

else:
        print("address is not valid")