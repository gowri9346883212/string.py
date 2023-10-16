#append:
lst = ["gowri",1,True]
print(lst)

lst: list = []
lst.append("gowri")
print(lst)

#insert:
attendees = ["gowri","dathu","surya"]
attendees.insert(1,"ganga")
print(attendees)

#read-access/get items from the list:
attendees = ("gowri","dathu","surya")
print(attendees.index("dathu"))

#count:
attendees = ["gowri","dathu","surya","dathu"]
print(attendees.count("dathu"))

attendees = ["gowri","dathu","surya","dathu"]
print(attendees.count('abc'))

attendees = ["gowri","dathu","surya","dathu"]
if(attendees.count("ganga") > 0):
    print(attendees.index("ganga"))

#update:
#by using index:
attendees = ["gowri","dathu","surya","dathu"]
attendees[1] = "siva dathu"
print(attendees)

#extend
attendees = ["gowri","dathu","surya"]
attendees1 = ["ganga","siva","padmini"]
attendees.extend(attendees1)
print(attendees)
print(attendees1)

#delete:
#remove:
attendees = ["gowri","dathu","surya"]
attendees.remove("surya")
print(attendees)

#pop with index
attendees = ["gowri","dathu","surya"]
attendees.pop(1)
print(attendees)

#pop without index:
attendees = ["gowri","dathu","surya"]
attendees.pop()
attendees.pop()
print(attendees)