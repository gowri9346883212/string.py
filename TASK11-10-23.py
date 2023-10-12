"""num = 5
i = 1
fact = 1
while i <= num:
    fact *= i
    i += 1
    print(fact)
    """
"""#prime or not:
num = 8
i = 1
res = True
while i <= num:
    if(i != 1 and num%i == 0 and i != num):
        res = False
        break
        i += 1
        if(res == True):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is a not prime number.")
"""
a = 1
b = 2
a = a + b
b = a - b
a = a - b
print(a,b)

a = 2
b = 1
temp = a
a = b
b = temp
print(a,b)

n = 10
a = 1
b = 0
i = 1
while i <= n:
    print(b)
    a = a + b
    b = a - b
    i += 1
