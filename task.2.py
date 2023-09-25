#strin concatenation
#operator overloading
fname = "gowri"
lname = "ganga"
print(fname + " " + lname)
print("fullName:" + fname + " " + lname)
#f'string/interpolation:
fname = "gowri"
lname = "ganga"
fullName = f"{fname} {lname}"
print(fullName)
print(f"fullName: { fname } {lname}")

#string join method:
fname = "gowri"
lname = "ganga"
lst = (fname, lname) #tuple creation
print(" " .join(lst))
list = ("fuiiName:", fname, lname)
print(list)

#strin split
#split
email = "gowri@gmail.com"
print(email.split( " @ " ))

#split lines
addres: str =""" 1-16
lampakalova,
prathipadu(M)
kakinada(D)
"""
print(addres.splitlines())

#partition
email = "a@gowri@gmail.com"
print(email.partition("@"))

#rpartition
email = "a@gowri@gmail.com"
print(email.rpartition("@"))

