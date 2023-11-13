from enum import Enum
class weekDay(Enum):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    friday = 5
    saturday = 6
    sunday = 7
#check given day is weekend or weekday
def checkday(value)->str:
    result: str = " "
    match(value):
        case weekDay.Monday.value:
            result = "weekday"
        case weekDay.Tuesday.value:
            result = "weekday"
        case weekDay.Wednesday.value:
            result = "weekday"
        case weekDay.Thursday.value:
            result = "weekday"
        case weekDay.friday.value:
            result = "weekday"
        case weekDay.saturday.value:
            result = "weekend"
        case weekDay.sunday.value:
            result = "weekend"
    return result
day = int(input("enter day value: 1.monday, 2.tuseday, 3.wednesday, 4.thursday, 5.friday, 6.saturday, 7.sunday:"))
print(checkday(day))
print(type(weekDay))
print(weekDay.Monday)
"""properties of Enum:value, name"""
print(weekDay.Monday.value)
print(weekDay.Monday.name)
#exception:
try:
    a = int(input("enter a value:"))
    b = int(input("enter b value:"))
    print(a%b)
except:
    print("exception occur.")
else:
    print("prg executed successfully.")
finally:
    print("pgm completed.")