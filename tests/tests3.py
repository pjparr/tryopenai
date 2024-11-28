## extend python builtin list


class IntegerList(list):
    # static method - sematically correct as part of the list
    @staticmethod
    def is_int(value):
        if type(value) is not int:
            raise ValueError("Not an integer type")

    # override builtin method __setitem__
    def __setitem__(self, index, value):
        IntegerList.is_int(value)
        list.__setitem__(self, index, value)

    def append(self, value):
        IntegerList.is_int(value)
        list.append(self, value)

    def extend(self, iterable):
        for element in iterable:
            IntegerList.is_int(element)

        list.extend(self, iterable)


int_list = IntegerList()

int_list.append(66)
int_list.append(22)
print("Appending int elements succeed:", int_list)

int_list[0] = 49
print("Inserting int element succeed:", int_list)

int_list.extend([2, 3])
print("Extending with int elements succeed:", int_list)

try:
    int_list.append("8-10")
except ValueError:
    print("Appending string failed")

try:
    int_list[0] = "10/11"
except ValueError:
    print("Inserting string failed")

try:
    int_list.extend([997, "10/11"])
except ValueError:
    print("Extending with ineligible element failed")

print("Final result:", int_list)

print("the dir of the int list", dir(int_list))

# make a list
li: list = list([1])
print(li)


##########


class Test:
    def __init__(self, member):  ## magic method / operator overloading
        print("in constructor")
        self.m = member

    def test_method(self):
        print("test method")


print(type(type))
print(type.__class__)
print(type(int))
print(int.__class__)
print(type(int_list))
print(int_list.__class__)
print(type(Test))
print(Test.__class__)

t = Test(4)
print(type(t.m))
print(t.m.__class__)


print(dir(int))
print(dir())
