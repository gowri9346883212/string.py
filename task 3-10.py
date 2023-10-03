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
print(int(a) // int(b))#

#logical
a= input("enter a value:")
b= input("enter b value:")
print(int(a<b) and (a>b))

a= input("enter a value:")
b= input("enter b value:")
print(int(a<b) or  (a>b))

a= input("enter a value:")
b= input("enter b value:")
print(int(not((a<b and a>b))))

#comparsion operators
a= input("enter a value:")
b= input("enter b value:")
print(int(a) <= int(b))
print(int(a) >= int(b))
print(int(a) != int(b))
print(int(a) > int(b))
print(int(a) <= int(b))
#bitwise

print(int(a) & int(b))
print(int(a) |int(b))
print(int(a) ^ int(b))

#leftshift
print(int(a) >> int(b))
print(int(a) << int(b))

#identity
print(int(a) is  int(b))
print(int(a) is not int(b))

#strigs check functions
print(a.isnumeric())
print(a.isdigit())
print(a.isascii())
print(a.isupper())
print(a.istitle())
print(a.islower())
print(a.isspace())
print(a.isprintable())
print(a.isidentifier())
print(a.isdecimal())

#string transform functions
firstname = input(" enter firstname:")
lasttname = input(" enter lastname:")
fullname = firstname +  " " + lasttname
print(fullname)


fullname = f" {firstname}  {lasttname}"
print(fullname)

lst = (firstname,lasttname)
print("".join(lst))

#splitlines
email= "gowrilingampalli@gmail.com"
print(email.split("@"))

#splitlines
email= "gowrilingampalli@gmail.com"
print(email.splitlines())

#partition
email= "gowrilingampalli@gmail.com 15"
print(email.partition("15"))

#rpartition
email= "gowrilingampalli@gmail.com"
print(email.rpartition("@"))

#capitalize
print(firstname.capitalize())
print(firstname.title())
print(firstname.upper())
print(firstname.lower())
print(firstname.casefold())
print(firstname.swapcase())

