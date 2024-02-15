"""
a = 10
d = 20
b = a or d
c = a
global a
print(b)
print(c)

import sqlite3


def db_init():
    conn = sqlite3.connect('test.db')
    print(conn)

    conn.execute('''
        CREATE TABLE IF NOT EXISTS countries
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            artist: text
            duration: time
            album:text
            
            
    ''')
    conn.commit()

    conn.execute("INSERT INTO songs (name, artist, duration,, album) VALUES (?, ?, ?, ?, ?)",
                 ('song', 'artist', '03:45', '2023-10-25', 'album'))
    conn.commit()
    conn.close()


db_init()
class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_value):
        if not isinstance(new_value, int):
            raise TypeError("Invalid age")
        self.__age = new_value


person = Person('Jane','Doe', 23)
print(person.age)


games = []

game1 = {"game_name": "GTA 5", "genre": "shooter,open_world", "date": 2013, "editor": "None"}
games.append(game1)

game2 = {"game_name": "stand_oof2", "genre": "shooter", "date": 2015, "editor": "None"}
games.append(game2)

game3 = {"game_name": "PUBG", "genre": "shooter", "date": 2011, "editor": "None"}
games.append(game3)

for game in games:
    print(f"gameName:{game['game_name']}, Genre:{game['genre']}, Date:{game['date']}, Editor:{game['editor']}")

shopping = []

product1 = {'product_name': 'Toy', 'price': 2.5}
shopping.append(product1)

product2 = {'product_name': 'notebook', 'price': 500}
shopping.append(product2)

product3 = {'product_name': 'book', 'price': 0.35}
shopping.append(product3)

product4 = {'product_name': 'copy_book', 'price': 0.5}
shopping.append(product4)

for products in shopping:
    print(coproductName:{products["product_name"]}, Price:{products["price"]}')

total_price = [product["price"] for product in shopping]
total_cost = sum(total_price)
print(f'Total cost: {total_cost}')

students = []

student1 = {'name': "John", 'age': 17, 'Geography_grade': 3, 'Math_grade': 4}
students.append(student1)

student2 = {'name': "Max", 'age': 16, 'Geography_grade': 2, 'Math_grade': 5}
students.append(student2)

student3 = {'name': "Smith", 'age': 19, 'Geography_grade': 4, 'Math_grade': 4}
students.append(student3)

student4 = {'name': "Same", 'age': 15, 'Geography_grade': 5, 'Math_grade': 5}
students.append(student4)

for student in students: print(filename: {student["name"]}, age: {student["age"]}, Geography_grade: {student[
"Geography_grade"]}, Math_grade: {student["Math_grade"]}')

total_geography_grades = sum(student["Geography_grade"] for student in students)
total_math_grades = sum(student["Math_grade"] for student in students)
total_subjects = len(students) * 2  # Assuming every student has grades for Geography and Math
overall_average = (total_geography_grades + total_math_grades) / total_subjects

print(f'Total geography grades: {total_geography_grades}')
print(f'Total math grades: {total_math_grades}')
print(f'Overall average: {overall_average}')

class BankAccount:

    def __init__(self, balance=0):
        self. Balance = balance


    def deposit(self, amount):
        self. Balance += amount


    def withdraw(self, amount):
        if self. Balance >= amount:
            self. balance -= amount
        else:
            print("dzer hashvin chka bavarar gumar")


    def get_balance(self):
        return self. Balance


account = BankAccount()
account.deposit(5000)
account.withdraw(10000)
print(account.get_balance())

total = {}
def insert(items):
    if items in total:
        total[items] += 1

    else:
        total[items] = 1


insert('Apple')
insert('Ball')
insert('Apple')

print(len(total))


class change:
    def __init__(self, x, y, z):
        self.a = x + y + z


x = change(1, 2, 3)
y = getattr(x, 'a')
setattr(x, 'a', y+1)
print(x.a)

class A:
    def __init__(self, x = 1):
        self.x = x


class der(A):
matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
       ]
rotated_clockwise = [list(row)[::-1] for row in zip(*matrix)]
for row in rotated_clockwise:
    print(row)

print(""
      ""
      ""
      "")
rotated_anti_clockwise = [list(row) for row in zip(*matrix)][::-1]
for row in rotated_anti_clockwise:
    print(row)

class Fruit:
    def nutrition(self):
        return 0
class Apple(Fruit):
    def nutrition(self):
        return 95
class Banana(Fruit):
    def nutrition(self):
        return 105


fruit = Fruit()
apple = Apple()
banana = Banana()

print(f"Питательная ценность фрукта: {fruit.nutrition()} калорий")
print(f"Питательная ценность яблока: {apple.nutrition()} калорий")
print(f"Питательная ценность банана: {banana.nutrition()} калорий")

class Shape:
    def area(self):
        return 0

    def __init__(self, a, b, c, ):
        self.a = a
        self.b = b
        self.c = c
        self.p = (self.a + self.b + self.c)/2
class Rectangle(Shape):
    def area(self):
        return self.a * self.b


class Triangle(Shape):
    def area(self):
        return (self.p * ((self.p - self.a)*(self.p - self.b)*(self.p - self.c))) ** 0.5


rectangle = Rectangle(3, 4, 0)
triangle = Triangle(3, 4, 5)

print(rectangle.area())
print(triangle.area())




class Employee:
    def __init__(self, name, salary):
        self.name = name
        self. Salary = salary

    def display_details(self):
        return f"Имя: {self.name}, Зарплата: {self.salary}"


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def display_details(self):
        return f"Имя: {self.name}, Зарплата: {self.salary}, Язык программирования: {self.programming_language}"


class Manager(Employee):
    def __init__(self, name, salary, level):
        super().__init__(name, salary)
        self. Level = level

    def display_details(self):
        return f"Имя: {self.name}, Зарплата: {self.salary}, Уровень: {self.level}"


employee = Employee("Иван", 50000)
developer = Developer("Петр", 60000, "Python")
manager = Manager("Мария", 70000, "Senior")

print(employee.display_details())
print(developer.display_details())
print(manager.display_details())

"""
''' 
age = int(input("Enter your age:  "))
if age >= 18:
    print("You successfully entered your page")
else:
    print("Your age is not a comfortable)")'''

'''number= int(input("Enter your number: "))
for i in range(number, 0, -2):
    print(i)
'''
'''number = int(input("Enter your number: "))
if number % 2 != 0 and number % 3 != 0:
    print("Tivd bajnvav xer migrator )))")
else:
    print("Defiles ynger")Ц
    
name = input('enter your name:')
age = int(input('enter your age:'))

print('hi', name, 'letter 10 years your age is', age + 10)

number1 = int(input('enter your number1:'))
number2 = int(input('enter your number2:'))
number3 = int(input('enter your number3:'))
print((number1 + number2 + number3)/3)

number = int(input('enter your number:'))
if number % 2 == 0:
    print(True)
else:
    print(False)

number = int(input('enter your number:'))
print(number, '*', 1, '=',  number * 1)
print(number, '*', 2, '=',  number * 2)
print(number, '*', 3, '=',  number * 3)
print(number, '*', 4, '=',  number * 4)
print(number, '*', 5, '=',  number * 5)
print(number, '*', 6, '=',  number * 6)
print(number, '*', 7, '=',  number * 7)
print(number, '*', 8, '=',  number * 8)
print(number, '*', 9, '=',  number * 9)
print(number, '*', 10, '=',  number * 10)

while True:
    number = int(input('enter positive number:'))
    if number > 0:
        start = int(input('enter start diapason:'))
        finish = int(input('enter finish diapason:'))
        for i in range(start, finish + 1):
            result = number * i
            print(result)

class BankAccount:

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withrow(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('dzer hashvin chka bavarar gumar')

account = BankAccount()

account.deposit(10000)
account.withrow(5000)
print(account.balance)

class Calculator:
    def __init__(self, x, y):
        self.num1 = x
        self.num2 = y

    def sum(self):
        return self.num1 + self.num2

    def double(self):
        return self.num1 * 2, self.num2 * 2

    def sqrt(self):
        return self.num1 ** 0.5 and self.num2 ** 0.5

    def minus(self):
        if self.num1 < self.num2:
            return self.num1 - self.num2
        else:
            return 'your num1 is smallest'


obj = Calculator(10, 20)
print(obj.sqrt())
class Person:

    def __init__(self, name, surname, gender, age):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age

    def __repr__(self):
        return "{} {} - {} : {}".format(self.name, self.surname, self.gender, self.age)


p = Person('Narek', 'Chqolian', 'Male', '15')
print(p)

'''
'''
class Person:
    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

    def __repr__(self):
        return "Name:{}, Surname:{}, - Gender:{}, : years old:{}".format(self.name, self.surname, self.gender, self.age)


person = Person("Narek", "Chqolian", 15, "Male")

print(person)

class Person:

    def __init__(self, n, s, g, a, u, f, c, m_s):
        self.name = n
        self.surname = s
        self.gender = g
        self.age = a
        self.university = u
        self.faculty = f
        self.course = c
        self.middle_score = m_s

    def __repr__(self):
        return "Name:{} Surname:{}  Gender:{}  Age:{}".format(self.name, self.surname, self.gender, self.age)


class Student(Person):

    def __repr__(self):
        return "middle_score:{}, course:{}, faculty:{}, university:{}".format(self.middle_score, self.course, self.faculty, self.university)

    def get_score(self):
        return sum(self.middle_score)/len(self.middle_score)

    def get_course(self):
        return self.course

    def get_faculty(self):
        return self.faculty

    def get_university(self):
        return self.university

def sum_of_even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            sum(numbers)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = sum_of_even_numbers(numbers)
print(result)

def is_palindrome(s):
    s = "".join(s.split())
    s = s.lower()
    return s == s[::-1]

result = is_palindrome("helleh")
print(result)


class Shape:

    def __init__(self, name):
        self.name = name


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

        if self.base < 0 or height < 0:
            raise ValueError("Значения base и height должны быть неотрицательными.")

    def calculate_area(self):
        return (self.base * self.height) / 2

    def __repr__(self):
        return f"Triangle({self.base, self.height})"

    def get_info(self):
        return f"{self.name}: base = {self.base}, height= {self.height}, area = {self.calculate_area()}"

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width
        if length < 0 or width < 0:
            raise ValueError("Значения length и width должны быть неотрицательными")


    def calculate_area_Rectangle(self):
        return self.length * self.width

    def __repr__(self):
        return f"Rectangle({self.length, self.width})"

    def get_info(self):
        return f"{self.name}: length = {self.length}, width = {self.width}, area = {self.calculate_area_Rectangle()}"

class Square(Shape):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side
        if side < 0:
            raise ValueError("Значения side должен быть неотрицательным")


    def calculate_area_square(self):
        return self.side * self.side

    def __repr__(self):
        return f"Square({self.side})"

    def get_info(self):
        return f"{self.name}: side = {self.side}, area = {self.calculate_area_square()}"


try:
    triangle1 = Triangle(10, 15)
    area1 = triangle1.calculate_area()
    print(f"area of triangle 1:{area1}")
    print(repr(triangle1))

    triangle2 = Triangle(5, -5)
    area2 = triangle2.calculate_area()
    print(f"area of triangle 2:{area2}")
    print(repr(triangle2))

    rectangle1 = Rectangle(5, 10)
    area_rectangle1 = rectangle1.calculate_area_Rectangle()
    print(f"area of rectangle 1: {area_rectangle1}")
    print(repr(rectangle1))

    rectangle2 = Rectangle(1, 4)
    area_rectangle2 = rectangle2.calculate_area_Rectangle()
    print(f"area of rectangle 2: {area_rectangle2}")
    print(repr(rectangle2))

    square1 = Square(5)
    area_square1 = square1.calculate_area_square()
    print(f"area of square 1: {area_square1}")
    print(repr(square1))

    square2 = Square(1)
    area_square2 = square2.calculate_area_square()
    print(f"area of square 2: {area_square2}")
    print(repr(square2))


except ValueError as e:
    print(f"Error {e}")


number = 2


if number % 2 == 0:
    print("number is even")
else:
    print("number is not even")

while True:
    age = int(input("enter your age:"))
    if age >= 18:
        break

string = input("enter number(for text):")

try:
    string = int(string)

except ValueError:
    print("the entered string cannot be converted to a number")
else:
    print(string * 2)
finally:
    print("exit program")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
try:
    user_input = input("enter your number for using factorial:")
    user_input = int(user_input)
    if user_input < 0:
        raise TypeError("A negative number is not valid input")
except ValueError:
    print("the entered string cannot be converted to a number")
except TypeError as e:
    print(f"Error:{e}")
else:
    result = factorial(user_input)
    print(f"result {result}")
finally:
    print("Exit program")

words = ["banana", "apple", "hello", "sis", "map", "hell"]

filtered_words = list(filter(lambda x: len(x) > 5, words))

print(f"standard words {words}")
print(f"filtered words {filtered_words}")

names = ["Alex", "Max", "Alena", "Jack", "Tom"]
filtered_names = list(filter(lambda x: x[0] == "A", names))
mapped_names = list(map(lambda x: x + "!", names))

print(f"names:{names}")
print(f"names, with started A:{filtered_names}")
print(f"names, with ended !:{mapped_names}")

numbers = [1, 2, 3, 4, 5, 6, 7, -5, -8, 10, -3]

filtered_numbers = list(filter(lambda x: x > 0, numbers))
mapped_numbers = list(map(lambda x: x ** 2, numbers))

print(f"numbers: {numbers}")
print(f"positive numbers:{filtered_numbers}")
print(f"squared numbers,{mapped_numbers}")

texts = ["Hello bro my name is Jack", "Masisy txur e Anin avervac", "what you talking about me?"]
filtered_texts = list(filter(lambda x: len(x) > 5, texts))
filtered_texts2 = list(filter(lambda x: "e" in x, texts))
print(f"texts, with 5+ words:{filtered_texts}")
print(f"texts, with 'e' in words:{filtered_texts2}")


def my_decorator(func):
    def wrapper():
        print("this is start")
        func()
        print("this is end")
    return wrapper

@my_decorator
def say_hello():
    print("hello!")


say_hello()




def message_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"name of func:{func.__name__}, args:{args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"result of func {func.__name__}:{result}")
        return result
    return wrapper


@message_decorator
def add_number(a, b):
    return a + b


@message_decorator
def multiply_number(x, y):
    return x * y


add_number(5, 6)
multiply_number(10, 55)

from functools import reduce

numbers = [1, 3, 5, 10, 15, 20, 150]


sum_numbers = lambda x, y: x + y

product = reduce(sum_numbers, numbers)


print(product)


from functools import reduce

words = ["hi", "my", "name", "is", "Jack"]
sum_words = reduce(lambda x, y: x + y + ",", words)
print(sum_words)

from functools import reduce

numbers = [1, 10, -5, 60, 3, -88, 6, -1]

positive_numbers = list(filter(lambda x: x >= 0, numbers))

multiply_positive_numbers = reduce(lambda x, y: x * y, positive_numbers)
print(f"this is the positive numbers:{positive_numbers}")
print(f"this is the multiply of positive numbers:{multiply_positive_numbers}")


students = [
    {"name": "Jack", "grades": 98},
    {"name": "Max", "grades": 89},
    {"name": "Bob", "grades": 33},
    {"name": "Jason", "grades": 92},
    {"name": "John", "grades": 91},
    {"name": "Jane", "grades": 66},
    {"name": "Same", "grades": 23},
            ]

max_grades = 90
min_grades = 40

max_grades_student = list(filter(lambda student: student["grades"] >= max_grades, students))
min_grades_student = list(filter(lambda student: student["grades"] <= min_grades, students))

print(f"students, with grades are biggest or equal of max grades:{max_grades_student}")
print(f"students, with grades are smallest or equal of min grades:{min_grades_student}")


def max_result_decorator(max_value):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result >= max_value:
                print(f"your result is greater than {max_value}. Truncating to {max_value}")
                return max_value
            return result
        return wrapper
    return decorator


@max_result_decorator(100)
def add_numbers(x, y):
    return x + y


result = add_numbers(10, 100)
print(result)

total_dogs = 0
total_cats = 0


class Dog:
    def __init__(self):
        global total_dogs
        total_dogs += 1


class Cat:
    def __init__(self):
        global total_cats
        total_cats += 1


dogs1 = Dog()
dogs2 = Dog()
cats1 = Cat()

print(f"total dogs:{total_dogs}")
print(f"total cats:{total_cats}")
'''
