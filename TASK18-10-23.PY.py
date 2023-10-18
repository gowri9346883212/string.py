#set datatype:
#implicit:
a = {'a','b','c'}
print(a)
print(type(a))
#explicit:
a = set(('a','b','c'))
print(type(a))
#datatype/variable annotation:
a: set = {'a','b','c'}
print(type(a))

#create:
#add:
a: set = {'a','b','c'}
a.add('d')
print(a)

#update:
a: set = {'a','b','c'}
b: set = {'a','c','d'}
a.update(b)
print(a)

#delete:
#remove:
a: set = {'a','b','c'}
a.remove('b')
print(a)

#discard:
a: set = {'a','b','c'}
a.discard('d')
print(a)

#pop:
a: set = {'a','b','c'}
a.pop( )
print(a)

#union:
a: set = {'a','b','c'}
b: set = {'b','c','d'}
print(a.union(b))

#intersection:
a: set = {'a','b','c'}
b: set = {'b','c','d'}
print(a.intersection(b))

