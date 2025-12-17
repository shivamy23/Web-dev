# class Welcome:
#     def greet(self):
#           print("Welcome to Code Debugging")  //Indentation Error

# obj = Welcome()
# obj.greet()


# class Calculator:
#     def add(a, b): //self
#         return a + b

# calc = Calculator()
# print(calc.add(3, 4))

# class Student:
#     def display(self):
#         print("Student Details")
#// s = Student()
# display()  //s.display


# class Event   //:
#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print("Event:",name)  //self.attribute_name

# e = Event("404 Not Found")
# e.show()


#Round2

# class Voter:
#     def __init__(self, age):
#         self.age = age

#     def is_eligible(self):
#         if self.age > 18:   // only a = sign is missing 
#             return "Eligible"
#         else:
#             return "Not Eligible"

# v = Voter(18)
# print(v.is_eligible())

# class Counter:
#     count = 0

#     def increment():  //self
#         count += 1   //className.variable

# c = Counter()
# c.increment()
# print(c.count)


# class Marks:
#     def __init__(self, scores):
#         self.scores = scores

#     def average(self):
#         return sum(self.scores) / 3   ///wrong average calculation

# m = Marks([80, 70, 90])
# print(m.average())

# class Printer:
#     def print_numbers(self):
#         for i in range(1, 6):  //expected value is 1 to 5 number 
#             print(i)

# p = Printer()
# p.print_numbers()


#Round 3

# class User:
#     def __init__(self,name):  //self is missing 
#         self.name = name

#     def show(self):
#         print("User:", self.name)

# u = User("Admin")
# u.show()


# class MathOps:
#     def square(self, n):
#         return n * n      //return is mmissing 

# m = MathOps()
# print(m.square(5))


# class Factorial:
#     def fact(self, n):
#         if n == 0:
#             return 1   //return value should be 1
#         return n * self.fact(n - 1)

# f = Factorial()
# print(f.fact(5))


# class Bank:
#     def __init__(self, balance):
#         self.balance = balance

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient balancel")  //# Correct message
#         else:
#             self.balance -= amount
#             print("Withdrawal successful")  ///# Correct message

# b = Bank(500)
# b.withdraw(300)
# print(b.balance)
