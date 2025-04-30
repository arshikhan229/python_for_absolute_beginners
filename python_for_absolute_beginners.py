# python_for_absolute_beginners.py

# This is a simple Python script for beginners.

# 1. Printing a message
print("Welcome to Python for Absolute Beginners!")

# 2. Variables and Data Types
name = "Alice"
age = 25
height = 1.65
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)

# 3. Taking user input
user_name = input("What is your name? ")
print("Hello,", user_name)

# 4. Conditional statements
if age > 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# 5. Loops
print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print(i)

# 6. Functions
def greet(name):
    print("Nice to meet you,", name)

greet(user_name)

# 7. Lists
fruits = ["apple", "banana", "orange"]
print("\nFruits list:")
for fruit in fruits:
    print(fruit)

# 8. Dictionaries
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

print("\nPerson dictionary:")
for key, value in person.items():
    print(key + ":", value)

# 9. Classes and Objects
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name + " says Woof!")

my_dog = Dog("Buddy")
my_dog.bark()

# 10. File handling
with open("hello.txt", "w") as file:
    file.write("This is a file created by Python!")

print("\nFile 'hello.txt' has been created.")
