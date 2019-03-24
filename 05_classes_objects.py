# -*- coding: utf-8 -*-
"""05_Classes_Objects.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rShq-bDNQEHRPh1Q8IesEnefTqYsJQgv

#  Introduction to Python

##***Welcome to your Fifth iPython Notebook.***

![python](https://cognitiveclass.ai/wp-content/uploads/2016/10/Machine-Learning-with-Python.png)

## **About iPython Notebooks**

iPython Notebooks are interactive coding environments embedded in a webpage. You will be using iPython notebooks in this class. You only need to write code between the ### START CODE HERE ### and ### END CODE HERE ### comments. After writing your code, you can run the cell by either pressing "SHIFT"+"ENTER" or by clicking on "Run Cell" (denoted by a play symbol) in the left bar of the cell.


**In this notebook you will learn -**



* Classes
* Objects

#Python Classes and Objects

**Python is an object oriented programming language.**

**Almost everything in Python is an object, with its properties and methods.**

**A Class is like an object constructor, or a "blueprint" for creating objects.**

**Create a Class:**

To create a class, use the keyword **class**.
"""

class MyClass:
  x = 5

"""**Create an Object:**

Now we can use the class named myClass to create objects.
"""

p1 = MyClass()
print(p1.x)         #Create an object named p1, and print the value of x

"""**The __init__() Function:**
The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created.
"""

class Person:
  def __init__(self, name, age,address):
    
    self.age = age
    self.name = name
    self.address = address

p1 = Person("John",45,"mumbai")

print(p1.name)
print(p1.age)
print(p1.address)

"""Create a class named Person, use the __init__() function to assign values for name and age.

**NOTE:** The __init__() function is called automatically every time the class is being used to create a new object.

**Object Methods:**

Objects can also contain methods. Methods in objects are functions that belongs to the object.

Let us create a method in the Person class.
"""

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)
    print(self.age-6)

p1 = Person("John", 36)
p1.myfunc()

"""Insert a function that prints a greeting, and execute it on the p1 object.

**NOTE:** The self parameter is a reference to the class instance itself, and is used to access variables that belongs to the class.

# Great Job!
"""