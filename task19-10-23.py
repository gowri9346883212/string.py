#intersection_update:
a: set = {'gowri','dathu','surya'}
b: set = {'dathu','surya','ganga'}
print(a.intersection_update(b))
print(a)
print(b)

#isdisjoint:
a: set = {'gowri'}
b: set = {'ganga'}
print(a.isdisjoint(b))

a: set = {'gowri','ganga'}
b: set = {'ganga'}
print(a.isdisjoint(b))

#difference:
a: set = {'gowri','dathu','surya'}
b: set = {'dathu','surya','ganga'}
print(a.difference(b))

#symmetric_difference:
a: set = {'gowri','dathu','surya'}
b: set = {'dathu','surya','ganga'}
print(a.symmetric_difference(b))

#symmetric_difference_update:
a: set = {'gowri','dathu','surya'}
b: set = {'dathu','surya','ganga'}
print(a.symmetric_difference_update(b))
print(a)
print(b)

#issubset:
a: set = {'gowri','dathu','surya'}
b: set = {'dathu','surya','ganga'}
print(a.issubset(b))

a: set = {'dathu'}
b: set = {'dathu','surya','ganga'}
print(a.issubset(b))

#issuperset:
a: set = {'gowri','dathu','surya'}
b: set = {'dathu','surya','ganga'}
print(a.issuperset(b))

a: set = {'gowri','dathu','surya'}
b: set = {'dathu'}
print(a.issuperset(b))

#frozenset:
fs = frozenset(('gowri','dathu','surya'))
print(type(fs))

#union:
fs1 = frozenset(('gowri','dathu','surya'))
fs2 = frozenset(('dathu','surya','ganga'))
print(fs1.union(fs2))

#intersection:
fs1 = frozenset(('gowri','dathu','surya'))
fs2 = frozenset(('dathu','surya','ganga'))
print(fs1.intersection(fs2))

#isdisjoin:
fs1 = frozenset(('gowri','dathu','surya'))
fs2 = frozenset(('dathu','surya','ganga'))
print(fs1.isdisjoint(fs2))

fs1 = frozenset(('gowri'))
fs2 = frozenset(('dathu'))
print(fs1.isdisjoint(fs2))

#difference:
fs1 = frozenset(('gowri','dathu','surya'))
fs2 = frozenset(('dathu','surya','ganga'))
print(fs1.difference(fs2))

#copy:
fs1 = frozenset(('a','b','c'))
fs2 = frozenset(('d','f','g'))
fs3 = fs1.copy()
print(fs3)

#symmetric_difference:
fs1 = frozenset(('gowri','dathu','surya'))
fs2 = frozenset(('dathu','surya','ganga'))
print(fs1.symmetric_difference(fs2))

#issubset:
fs1 = frozenset(('gowri','dathu','surya'))
fs2 = frozenset(('dathu','surya','ganga'))
print(fs1.issubset(fs2))

fs1 = frozenset(('5'))
fs2 = frozenset(('5','4','6'))
print(fs1.issubset(fs2))

#issuperset:
fs1 = frozenset(('gowri','dathu','surya'))
fs2 = frozenset(('dathu','surya','ganga'))
print(fs1.issuperset(fs2))

fs1 = frozenset(('g','d','s'))
fs2 = frozenset(('d'))
print(fs1.issuperset(fs2))

#dictionary datatype:
#implicit:
userdetails = {'first Name':'gowri','last Name':'lingampalli','email':'gowri@gmail.com'}
print(type(userdetails))
#explicit:
userdetails = dict({'first Name':'gowri','last Name':'lingampalli','email':'gowri@gmail.com'})
print(type(userdetails))
#datatype/variable annotation:
userdetails: dict = {'first Name':'gowri','last Name':'lingampalli','email':'gowri@gmail.com'}
print(type(userdetails))



