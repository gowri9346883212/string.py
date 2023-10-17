#clear
attendees = ["gowri","dathu","surya"]
print(attendees.clear())
print(type(attendees))
print(attendees)

"""#delete:
attendees = ["gowri","dathu","surya"]
del attendees[0]
print(attendees)
del attendees
print(attendees)"""

"""attendees1 = input("enter attendees name:")
attendees2 = input("enter attendees name:")
attendees3 = input("enter attendees name:")
attendees = []
attendees.append(attendees1)
attendees.append(attendees2)
attendees.append(attendees3)
print(attendees)"""

#sort list
lst = [1,5,6,2,3,4]
lst.sort()
print(lst)

#reverse list:
lst = [1,5,6,2,3,4]
lst.reverse()
print(lst)

#tuple:
#implicit:
tpl = (1,2,3)
print(type(tpl))
#explicit:
a = tuple((1,2,3,4))
print(type(a))
#data type/variable anntation
tpl: tuple  = (1,2,3)
print(type(tpl))

#tuple methods:
#conut:
tpl = tuple((1,2,3,1))
print(tpl.count(1))
#index:
tpl = tuple((1,2,3,1))
print(tpl.index(2))

tpl = tuple((1,2,3,1))
lst = list(tpl)
print(type(list))

# Python program to print a list
# without using the sort() function
# without an extra variable

l1 = [76, 23, 45, 12, 54, 9]
print("Original List:", l1)

# sorting list using nested loops
for i in range(0, len(l1)):
    for j in range(i + 1, len(l1)):
        if l1[i] >= l1[j]:
            l1[i], l1[j] = l1[j], l1[i]

# sorted list
print("Sorted List", l1)