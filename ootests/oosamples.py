# # 1  print exex
# class Ex(Exception):
#     def __init__(self, msg):
#         # super().__init__(self, msg + msg)
#         Exception.__init__(self, msg + msg)

#     pass


# try:
#     raise (Ex("ex"))
# except Ex as e:
#     print(e)
# except Exception as e:
#     print(e)


# 2


# # If you don't define a __str__() method for a class, then the built-in object implementation
# # calls the __repr__() method instead.27 Jan 2023
# class I:
#     def __init__(self):
#         self.s = "abc"
#         self.index = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index == len(self.s):
#             raise StopIteration
#         v = self.s[self.index]
#         self.index += 1
#         return v


# for x in I():
#     # x. next
#     print(x, end="   ")


# # 3
# try:
#     raise Exception (1,2,3)


# ### try to understand constructors
# class A:
#     def __str__(self):
#         return "a"


# class B:
#     def __str__(self):
#         return "b"


# class C(B, A):
#     pass


# o = C()
# print(o)


# class A:
#     A=1


# issubclass()


# class A:
#     def __str__(self):
#         return "a"


# class B(A):
#     def __str__(self):
#         return "b"


# class C(B):
#     pass


# o = C()
# print(o)

# hasattr


class A:
    def __init__(self):
        pass


a = A()
print(hasattr(a, "A"))


### try unpack operators

# class methods

# function and class decorators
