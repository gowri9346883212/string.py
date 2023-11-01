"""
#global scope
class emp:
    fname:str="gowri"
    lname:str="ganga"
emp1=emp()
print(emp1.lname)

#partially private scope
class emp:
    _fname:str="gowri"
    _lname:str="ganga"
emp1=emp()
print(emp1._fname)

#strictly private scope
class emp:
    __fname:str="gowri"
    __lname:str="ganga"
emp1=emp()
print(emp1.__fname)

#global variable
def fullname():
    global lname
    fname="gowri"
    lname="ganga"
fullname()
print(lname)
print(fname)#error

#functional scope
def fullname():
    global lname
    fname="satya"
    lname="swamy"
fullname()
print(lname)
print(fname)#error"""


#abstraction
class emp:
    __fname:str="gowri"
    __lname:str="ganga"
    def fullname(self):
      return self.__fname+" "+self.__lname
emp1=emp()
emp1.__fname="ABC"
print(emp1.__fname)
print(emp1.fullname())
