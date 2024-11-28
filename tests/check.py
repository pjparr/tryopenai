from enum import Enum, auto


class DiscountType(Enum):
    STANDARD = auto()
    SEASONAL = auto()
    WEIGHT = auto()


def get_discounted_price(cart_weight, total_price, discount_type):
    if discount_type == DiscountType.STANDARD:
        return total_price - (total_price * 0.06)
    if discount_type == DiscountType.SEASONAL:
        return total_price - (total_price * 0.12)
    if discount_type == DiscountType.WEIGHT:
        if cart_weight < 10:
            return total_price - (total_price * 0.06)
        elif cart_weight > 10:
            return total_price - (total_price * 0.18)


print(get_discounted_price(12, 100, DiscountType.WEIGHT))


a: list[list[int]] = [[]] * 3
a[1].append(7)
print(a)

w = [j for j in range(3)]
print(w)

aoa = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a = [[row[j] for row in aoa] for j in range(3)]
print(a)

# 1 4 7
# 2 5 8
# 3 6 9
##
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n1 = [[x[idx] for x in arr] for idx in range(3)]
print(n1)

### or write as nested for loop
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n1 = []
for idx in range(3):
    temp = []
    for j in arr:
        temp.append(j[idx])
    n1.append(temp)
print(n1)

######
a2 = bin(8) + bin(8)
print(a2)


print([13, 3][False])

if [2]:
    print(
        "eee"
    )  ### considered  truthy  (not a bool value perse but evaluates to True / False by definition )

if []:
    print("eddee")  ## considered Falsy
print(2 % 0o27)


a1: list[int] = [1, 2, 3, 4]
print(a1[:-1])

print("asdad"[-2:])
print("asdad"[1:])

# r = "qwe"
# r[0] = "r"  ### not permitted strings are immutable

a = "qqq"
b = "qqq"
print(id(a) == id(b))
# The reason why that happens is because both x and y are pointing to the same memory address. What reason
# would Python have in this case to create the exact same object
# in memory twice, when not explicitly asked to do so?
## could also be a type of compiler optimization
anew: list[str] = ["apple", "orange"]
print(type(anew[-1]))  ##### returns a string


a = list(map(lambda x: x**-1, [1, 2, 3]))
print(a)

a2 = "qwerty "
for i in a:
    print(i)

print(1 & 1)

print([x * x for x in range(4) if x % 2 == 0])

a = list(filter(lambda j: j < 1, map(lambda x: x**-1, [1, 2, 3]))) # type: ignore
print(a)

a4: list[int] = list(map(lambda x: x + 1, [1, 2, 3]))
print(a4)


##### see medium article on Pythons memeory allocation mechamisms
def multiply(value, times):
    value *= times


number = 5
multiplier = 2

multiply(number, multiplier)
print(number)


def listChanger(lis: list) -> bool:
    print("Inner List :", lis)
    lis.append("ss")
    print(type(str))
    return True


"""_summary_

"""


def listChanger2(lis: list) -> bool:
    print("Inner List :", lis)
    lis.append("adasd")
    return True


fruits = ["Melon", "Orange", "Cherry"]


listChanger(fruits)
print("Original List :", fruits)


#### concept of decoupling or disassociating
# # Since we only appended a value to the list without reassigning the variable,
# # there is no decoupling or recoupling taking place. Both the inner and outer variables still refer to the same object, while the
# # content of that object has been altered by the addition of the new value.


##### replace Ruff with mypy
#### document formatter and linter ----- how to set this up


# Python has support for optional "type hints" (also called "type annotations").


# These "type hints" or annotations are a special syntax that allow declaring the type of a variable.

num = {}
num[(1, 2)] = 10
print(num)

### test sets

a = [5, 5, 5, 7, 7, 7]
b = set(a)  ### should only be 5 and 7


def test(l):
    if l in b:
        return 1
    else:
        return 0


c = filter(test, a)
for index in c:
    print(index)

di = {"q": 1, "w": 3}
"sss".__contains__("s")
di.__delitem__("q")
del di["q"]
print(di)


def myFunction():
    pass


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")


# Example usage:
person = Person("John Doe", 30)
person.greet()


# whatch Pylance vid - on configuraing and diable mypy
# to auto add type checking
###   how to auto start vitual env in terminal
########  asdadadad


def newfunc(i: int) -> int:
    """_summary_

    Args:
        i (int): _description_

    Returns:
        int: _description_
    """
    return 2


cd: int = newfunc(2)
print(cd)


#### may need to turn off some of the codeium config

# %%
a: list[list[int]] = [[]] * 3
a[1].append(7)
print(a)
