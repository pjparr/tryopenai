## __dict__
##  type
## __class__
"""

import random


class Phone:
    def __init__(self):
        self.number = None
        print(f"in constructor {self}", end="\n")

    # def __repr__(self):
    #     return f"{self.number}\n"

    # def __str__(self):
    #     return "str\n"

    def add_sim(self, no):
        self.number = no

    def turn_on(self):
        print("turning on:", self.number, end="\n")

    def turn_off(self):
        print("turn off:", self.number, end="\n")

    def call(self):
        print("called a number")


ph = Phone()
print(ph)
ph.add_sim("212")
print(ph)


##############################################################

# Apple packaging.
# Imagine that you receive a task description of an application that monitors the process of apple packaging before the apples are sent to a shop.

# A shop owner has asked for 1000 apples, but the total weight limitation cannot exceed 300 units.

# Write a code that creates objects representing apples as long as both limitations are met. When any limitation is exceeded, than the packaging process is stopped, and your application should print the number of apple class objects created, and the total weight.

# Your application should keep track of two parameters:

#     the number of apples processed, stored as a class variable;
#     the total weight of the apples processed; stored as a class variable. Assume that each apple's weight is random, and can vary between 0.2 and 0.5 of an imaginary weight unit;

# Hint: Use a random.uniform(lower, upper) function to create a random number between the lower and upper float values.


class Apple:
    count = 0
    total_weight = 0

    def __init__(self):
        pass

    def add(self, weight):
        new_weight = Apple.total_weight + weight
        if new_weight > 300:
            print("ewxceeed!\n")
            return False
        Apple.total_weight = new_weight
        Apple.count += 1
        return True

    @classmethod
    def get_one(cls):
        return random.uniform(0.2, 0.5)

    @staticmethod  ## semantics --- encapulation only
    def smethod():
        print("st")


a = Apple()
print("is an apple:", isinstance(a, Apple))
print(Apple.get_one(), end="\n")
for i in range(1, 1000):
    if not a.add(Apple.get_one()):
        break
print(f"Total {Apple.count} with weight {Apple.total_weight}")
print(Apple.smethod())

###########


# class Crowd(list):
#     ## collection of Person (deepcopy)
#     def add(self, person):
#         newp = Person(2, 4, 5)
#         self.append(newp)
#         ## how would you implement a copy constructor

#     ##### add a crowd to a crowd

#     def __add__(self, other):  #### add a crowd to a crowd
#         return self.weight + other.weight


# class Person(Crowd):
#     def __init__(self, weight, age, salary):
#         self.myid = id(self)
#         self.weight = weight
#         self.age = age
#         self.salary = salary


ii = int("2")
ii += ii
print(ii)


class A:
    def info(self):
        print("Class A")


class B(A):
    def info(self):
        print("Class B")


class C(A):
    def info(self):
        print("Class C")


class D(B, C):
    pass


D().info()

print(dir(10))


class MathUtils:
    @staticmethod
    def average(a, b):
        return a + b / 2


print(MathUtils.average(2, 1))


class mystr(str):
    pass
"""

#### iban example
import random


class IBANValidationError(Exception):
    pass


e = dict()  ##### takes **kwargs)
d = dict(b=24353522, asdasda=4444)
d = dict({"a": 222, "b": 24353522})
d.items()
print(d)


class IBANDict(dict):
    def __setitem__(self, _key, _val):
        if validateIBAN(_key):
            super().__setitem__(_key, _val)

    def update(
        self, *args, **kwargs
    ):  ####   *args === ,d,e,tyyy    **kwargs === as passed in
        print("args:", args)
        print("kwargs:", kwargs)
        # t = dict(*args, **kwargs)

        for _key, _val in dict(*args, **kwargs).items():
            self.__setitem__(_key, _val)


def validateIBAN(iban):
    iban = iban.replace(" ", "")

    if not iban.isalnum():
        raise IBANValidationError("You have entered invalid characters.")

    elif len(iban) < 15:
        raise IBANValidationError("IBAN entered is too short.")

    elif len(iban) > 31:
        raise IBANValidationError("IBAN entered is too long.")

    else:
        iban = (iban[4:] + iban[0:4]).upper()
        iban2 = ""
        for ch in iban:
            if ch.isdigit():
                iban2 += ch
            else:
                iban2 += str(10 + ord(ch) - ord("A"))
        ibann = int(iban2)

        if ibann % 97 != 1:
            raise IBANValidationError("IBAN entered is invalid.")

        return True


my_dict = IBANDict()
keys = [
    "GB72 HBZU 7006 7212 1253 00",
    "FR76 30003 03620 00020216907 50",
    "DE02100100100152517108",
]

for key in keys:
    my_dict[key] = random.randint(0, 1000)

print("The my_dict dictionary contains:")
for key, value in my_dict.items():
    print("XXXXXXXXXXXXXXXXXX\t{} -> {}".format(key, value))

try:
    print(my_dict)
    # my_dict[]
    my_dict.update({"dummy_account": 100, "dummy_accountqqq": 100}, sss=222, eee=888)
except IBANValidationError:
    print("adasdasdasdasd")

    ####### what get assigned to what with the unpack operators


try:
    g = int("d")
except ImportError as e:
    print(e.name
