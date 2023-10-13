#string slicing
#start, end are indexes.end index will be not be included
name = "python"
print(name[0:3])

#start, end indexes are optional.
name = "python"
print(name[ : ])
print(name[0: ])
print(name[ :5])

#nagative index:
name = "python"
print(name[-6:-1])
print(name[-6: ])
print(name[ :-1])

#list deata types:
#implicit:
attendees =["gowri","surya","dattu"]
print(type(attendees))
#explicit:
attendees =list(("gowri","surya","dattu"))
print(type(attendees))
#datatype/variable annotation:
attendees: list =["gowri","surya","dattu"]
print(type(attendees))
attendees:list = list(("gowri","surya","dattu"))
print(type(attendees))

#accessing list items
attendees: list =["gowri","surya","dattu"]
print(attendees[0])
print(attendees[-1])

#list slicing:
attendees: list =["gowri","surya","dattu"]
print(attendees[0])
print(attendees[-1])
print(attendees[:])
print(attendees[0:2])
print(attendees[-2:-1])
print(attendees[-2:])

#reverse a string
a = "python"[::-1]
print(a)

#reverse a string without a slicing
name = "surya padmini"
string = ""
for i in name:
    string = i + string
print("reversed string",string)

#reverse a list item
attendees: list = ["gowri","dattu","surya"]
print(attendees[::-1])