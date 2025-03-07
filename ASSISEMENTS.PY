# BASICS OF PYTHON
#Print the name
print("JALA COMPANY ASS")

#Single line comment
#Multi Line
#Comment
print("Multi-line Comment")

a = 10
print("the type of ", a, type(a))

f = 100.9
print("the type of ", f, type(f))

B = True
print("type of ", B, type(B))

C = "JALA"
print("type of ", C, type(C))

#Define the local and Global variables with the same
# name and print both variables and understand the scope of the variables.
# Global variable
x = 50


def test_scope():
    # Local variable with the same name
    x = 20
    print("Inside function, local x:", x)  # Local x will be printed


# Calling the function
test_scope()

# Printing the global variable
print("Outside function, global x:", x)  # Global x will be printed


#2-Operators
#Write a function for arithmetic operators(+,-,*,/)
def arithmetic_operations(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:  # Prevent division by zero
            return a / b
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operator"


# Example usage
num1 = 10
num2 = 5

print("Addition:", arithmetic_operations(num1, num2, '+'))
print("Subtraction:", arithmetic_operations(num1, num2, '-'))
print("Multiplication:", arithmetic_operations(num1, num2, '*'))
print("Division:", arithmetic_operations(num1, num2, '/'))


#Write a method for increment and decrement operators(++, --)
def increment_decrement(value, operation):
    if operation == "++":
        return value + 1  # Increment
    elif operation == "--":
        return value - 1  # Decrement
    else:
        return "Invalid operation"


# Example usage
num = 10

print("Increment:", increment_decrement(num, "++"))  # Output: 11
print("Decrement:", increment_decrement(num, "--"))  # Output: 9


#Write a program to find the two numbers equal or not
def check_equality(num1, num2):
    if num1 == num2:
        return "The numbers are equal."
    else:
        return "The numbers are not equal."


a = 10
b = 20

print(check_equality(a, b))  # Output: The numbers are not equal.


#   Program for relational operators (<,<==, >, >==)

def compare_numbers(a, b):
    print(f"{a} < {b}: {a < b}")  # Less than
    print(f"{a} <= {b}: {a <= b}")  # Less than or equal to
    print(f"{a} > {b}: {a > b}")  # Greater than
    print(f"{a} >= {b}: {a >= b}")  # Greater than or equal to


# Example usage
num1 = 10
num2 = 20

compare_numbers(num1, num2)


#Print the smaller and larger number
def find_smaller_larger(a, b):
    smaller = min(a, b)  # Find smaller number
    larger = max(a, b)  # Find larger number
    print(f"Smaller number: {smaller}")
    print(f"Larger number: {larger}")


# Example usage
num1 = 10
num2 = 20

find_smaller_larger(num1, num2)

#3-Loops
#Write a program to print “Bright IT Career” ten times using for loop
for i in range(10):
    print("Bright IT Career")


#Write a java program to print 1 to 20 numbers using the while loop
#Program to equal operator and not equal operators
def check_equality(a, b):
    print(f"{a} == {b}: {a == b}")  # Checks if values are equal
    print(f"{a} != {b}: {a != b}")  # Checks if values are not equal


# Example usage
num1 = 10
num2 = 20

check_equality(num1, num2)


#Write a program to print the odd and even numbers.
def print_odd_even(n):
    print("Even numbers:")
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i, end=" ")

    print("\nOdd numbers:")
    for i in range(1, n + 1):
        if i % 2 != 0:
            print(i, end=" ")


# Example usage
num = 20
print_odd_even(num)


#Write a program to print largest number among three numbers.

def find_largest(a, b, c):
    largest = max(a, b, c)  # Using built-in max function
    print(f"The largest number is: {largest}")


# Example usage
num1 = 10
num2 = 25
num3 = 15

find_largest(num1, num2, num3)
#Write a program to print even number between 10 and 20 using while

num = 10  # Start from 10

while num <= 20:  # Loop until 20
    if num % 2 == 0:  # Check if even
        print(num, end=" ")
    num += 1  # Increment by 1
#Write a program to print 1 to 10 using the do-while loop statement.
num = 1  # Initialize

while True:  # Simulating do-while
    print(num, end=" ")  # Print number
    num += 1  # Increment
    if num > 10:  # Exit condition
        break


#Write a program to find Armstrong number or not
def is_armstrong(number):
    original_num = number
    power = len(str(number))  # Count number of digits
    armstrong_sum = 0

    while number > 0:
        digit = number % 10  # Extract last digit
        armstrong_sum += digit ** power  # Add digit^power
        number


#Write a program to find the prime or not.

#Write a program to palindrome or not.
s = "malayalam"  # string

i,j = 0, len(s) - 1  # two pointers

is_palindrome = True  # assume palindrome
while i < j:
    if s[i] != s[j]:  # mismatch found
        is_palindrome = False
        break
    i += 1
    j -= 1

if is_palindrome:
    print("Yes")
else:
    print("No")

# # Python program to check if the input number is odd or even.
x = 24
# Check the remainder dividing x by 2 is 0
if x % 2 == 0:
    print("Even")
else:
    print("Odd")

# Checking another number
x = 7

if x % 2 == 0:

  print("Even")
else:
    print("Odd")

#Print gender (Male/Female) program according to given M/F using switch

#4-Arrays
#Write a function to add integer values of an array
def sum_of_array(arr):
    return sum(arr)  # Using the built-in sum() function

# Example usage
numbers = [10, 20, 30, 40, 50]
print("Sum of array:", sum_of_array(numbers))
#Write a function to calculate the average value of an array of integers
def average_of_array(arr):
    return sum(arr) / len(arr) if arr else 0  # Avoid division by zero

# Example usage
numbers = [10, 20, 30, 40, 50]
print("Average of array:", average_of_array(numbers))

#Write a program to find the index of an array element
a = [10, 20, 30, 40, 50]

# Find the index of the element 30 in the list 'a'
idx = a.index(30)
print(idx)
# Write a function to test if array contains a specific value
a = [10, 20, 30, 40, 50]

# Check if 30 exists in the list
if 30 in a:
    print("Element exists in the list")
else:
    print("Element does not exist")
#Write a function to remove a specific element from an array
# Python program to remove given element from the list
list1 = [1, 9, 8, 4, 9, 2, 9]

# Printing initial list
print("original list : " + str(list1))

remove = 9

# using pop()
# to remove list element 9
if remove in list1:
    # get index of 9 and pop it out
    list1.pop(list1.index(remove))

# Printing list after removal
print("List after element removal is : " + str(list1))
#Write a function to copy an array to another array


# importing the module
from numpy import *

# creating the first array
arr1 = array([2, 6, 9, 4])

# displaying the identity of arr1
print(id(arr1))

# assigning arr1 to arr2
arr2 = arr1

# displaying the identity of arr2
print(id(arr2))

# making a change in arr1
arr1[1] = 7

# displaying the arrays
print(arr1)
print(arr2)

#Write a function to insert an element at a specific position in the array
# creating a list
fruit = ["banana","cherry","grape"]
fruit.insert(1,"apple")
print(fruit)
#Write a function to find the minimum and maximum value of an array
import sys

# Define an array
a = [1, 423, 6, 46, 34, 23, 13, 53, 4]

# Sort the array using the built-in sorted() function
a_sorted = sorted(a)

# Find the minimum and maximum values
min_value = a_sorted[0]
max_value = a_sorted[-1]

# Print the results
print(f"min-{min_value} max-{max_value}")

#Write a function to reverse an array of integer values
a = [1, 2, 3, 4, 5]

# Reverse the list in-place
a.reverse()
print(a)

#Write a function to find the duplicate values of an array
a = [1, 2, 3, 1, 2, 4, 5, 6, 5]

# Initialize an empty set to store seen elements
s = set()

# List to store duplicates
dup = []

for n in a:
    if n in s:
        dup.append(n)
    else:
        s.add(n)

print(dup)
## Python Program for find commom element using two array
import array

arr1 = array.array('i', [1, 2, 3, 4, 5])
arr2 = array.array('i', [3, 4, 5, 6, 7])
result = array.array('i')

print("Common elements are:", end=" ")

#Write a program to find the common values between two arrays
# To traverse array1.
for i in range(len(arr1)):
    # To traverse array2.
    for j in range(len(arr2)):
        # To match elements of array1 with elements of array2.
        if arr1[i] == arr2[j]:
            # Check whether the found element is already present in the result array or not.
            if arr1[i] not in result:
                result.append(arr1[i])
                print(arr1[i], end=" ")
                break

#Write a method to remove duplicate elements from an array
def remove_duplicates(arr):
    return list(set(arr))

# Example usage
arr = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(arr))  # Output: [1, 2, 3, 4, 5] (Order not guaranteed)
#Write a method to find the second largest number in an array
a = [10, 20, 4, 45, 99]

# Sorting the list in descending order
a.sort(reverse=True)

# Second largest number will be at index 1
print(a[1])

#Write a method to find the second largest number in an array
a = [10, 20, 4, 45, 99]

# Sorting the list in descending order
a.sort(reverse=True)

# Second largest number will be at index 1
print(a[1])

# Write a method to find number of even number and odd numbers in an array
from collections import Counter

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Counting even and odd numbers using Counter
counts = Counter(['even' if num % 2 == 0 else 'odd' for num in a])

# Printing the results
print("Even numbers:", counts['even'])
print("Odd numbers:", counts['odd'])

#Write a function to get the difference of largest and smallest value
def difference_max_min(arr):
    if not arr:
        return None  # Handle empty list case
    return max(arr) - min(arr)

# Example usage
arr = [10, 20, 4, 45, 99]
print(difference_max_min(arr))  # Output: 95 (99 - 4)
#Write a method to verify if the array contains two specified elements(12,23)

def isSubset(a, b):
    m = len(a)
    n = len(b)
    # Iterate over each element in the second array
    for i in range(n):
        found = False

        # Check if the element exists in the first array
        for j in range(m):
            if b[i] == a[j]:
                found = True
                break

        # If any element is not found, return false
        if not found:
            return False

    # If all elements are found, return true
    return True


if __name__ == "__main__":
    a = [11, 1, 13, 21, 3, 7]
    b = [11, 3, 7, 1]

    if isSubset(a, b):
        print("true")
    else:
        print("false")

#Write a program to remove the duplicate elements and return the new array
def remove_duplicates(arr):
    return list(set(arr))

# Example usage
arr = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(arr))  # Output: [1, 2, 3, 4, 5] (Order not guaranteed)
#5-static
#Define a static variable and access that through a class
class MyClass:
    static_var = 100  # Static variable

# Accessing through class name
print(MyClass.static_var)  # Output: 100

# Accessing through an instance
obj = MyClass()
print(obj.static_var)  # Output: 100

# Modifying via instance (creates an instance attribute, doesn't change the class variable)
obj.static_var = 200
print(obj.static_var)       # Output: 200 (instance attribute)
print(MyClass.static_var)   # Output: 100 (class variable remains unchanged)

# Define a static variable and access that through a instance
class MyClass:
    static_var = 100  # Static variable (class-level attribute)

# Creating an instance
obj = MyClass()

# Accessing static variable through the instance
print(obj.static_var)  # Output: 100

# Accessing static variable through the class
print(MyClass.static_var)  # Output: 100

#Define a static variable and change within the instance
class MyClass:
    static_var = 100  # Static (class) variable

obj1 = MyClass()
obj2 = MyClass()

# Accessing the static variable
print(obj1.static_var)  # Output: 100
print(obj2.static_var)  # Output: 100

# Modifying the static variable through an instance
obj1.static_var = 200  # Creates an instance attribute, doesn't change the class variable

print(obj1.static_var)  # Output: 200 (Instance-level change)
print(obj2.static_var)  # Output: 100 (Still refers to class variable)
print(MyClass.static_var)  # Output: 100 (Class variable remains unchanged)

#. Define a static variable and change within the class
class MyClass:
    static_var = 100  # Static (class) variable

    @classmethod
    def change_static_var(cls, new_value):
        cls.static_var = new_value  # Modifies the class variable

# Accessing before modification
print(MyClass.static_var)  # Output: 100

# Modifying the static variable within the class
MyClass.change_static_var(500)

# Accessing after modification
print(MyClass.static_var)  # Output: 500

# Creating instances to check the value
obj1 = MyClass()
obj2 = MyClass()

print(obj1.static_var)  # Output: 500
print(obj2.static_var)  # Output: 500

#6-Strings
#. Different ways creating a string

str1 = 'Hello, World!'   # Single quotes
str2 = "Hello, World!"   # Double quotes

print(str1)  # Output: Hello, World!
print(str2)  # Output: Hello, World!

#Concatenating two strings using + operator
str1 = "Hello"
str2 = "World"

# Concatenation
result = str1 + " " + str2  # Adding a space between words

print(result)  # Output: Hello World
#Finding the length of the string
str1 = "Hello, World!"
length = len(str1)

print(length)  # Output: 13
#Extract a string using Substring
text = "Hello, World!"

# Extracting "Hello"
substring = text[0:5]  # Start at index 0, stop before index 5

print(substring)  # Output: Hello
#Searching in strings using index()
text = "Python is awesome"

# Searching for "is"
position = text.index("is")

print(position)  # Output: 7

#Matching a String Against a Regular Expression With matches()

import re

pattern = r"\d{3}-\d{2}-\d{4}"  # Pattern for a Social Security Number (SSN)
text = "123-45-6789"

if re.fullmatch(pattern, text):
    print("Pattern matches the string exactly!")
else:
    print("No match found.")

#Comparing strings
str1 = "Hello"
str2 = "Hello"
str3 = "World"

print(str1 == str2)  # True (Both are identical)
print(str1 != str3)  # True (Different strings)

#startsWith(), endsWith() and compareTo()
text = "Hello, World!"

print(text.startswith("Hello"))  # True
print(text.startswith("World"))  # False

#Trimming strings with strip()
text = "   Hello, World!   "

trimmed_text = text.strip()
print(trimmed_text)  # Output: "Hello, World!"

#. Replacing characters in strings with replace()
text = "Hello, World!"
new_text = text.replace("World", "Python")

print(new_text)  # Output: "Hello, Python!"

#Splitting strings with split()
text = "Python is awesome"
words = text.split()

print(words)  # Output: ['Python', 'is', 'awesome']
#2. Converting integer objects to Strings
num = 123
num_str = str(num)

print(num_str)       # Output: "123"
print(type(num_str)) # Output: <class 'str'>
#Converting to uppercase and lowercase
text = "hello world"
upper_text = text.upper()

print(upper_text)  # Output: "HELLO WORLD"


#7-inhertance
#Create three methods in each class, 2 methods are specific to each class and third
#method (override method) should be in all three Classes A, B and C
# Superclass A
# Superclass A
class A:
    def method_a1(self):
        print("Method A1: Unique to Class A")

    def method_a2(self):
        print("Method A2: Unique to Class A")

    def show(self):  # Overridden method
        print("Show method from Class A")

# Subclass B (Inherits from A)
class B(A):
    def method_b1(self):
        print("Method B1: Unique to Class B")

    def method_b2(self):
        print("Method B2: Unique to Class B")

    def show(self):  # Overriding method
        print("Show method from Class B")

# Subclass C (Inherits from B)
class C(B):
    def method_c1(self):
        print("Method C1: Unique to Class C")

    def method_c2(self):
        print("Method C2: Unique to Class C")

    def show(self):  # Overriding method
        print("Show method from Class C")

# Testing the classes
obj_a = A()
obj_b = B()
obj_c = C()

print("\nCalling methods from Class A:")
obj_a.method_a1()
obj_a.method_a2()
obj_a.show()

print("\nCalling methods from Class B:")
obj_b.method_a1()  # Inherited from A
obj_b.method_b1()
obj_b.method_b2()
obj_b.show()  # Overridden method

print("\nCalling methods from Class C:")
obj_c.method_a1()  # Inherited from A
obj_c.method_b1()  # Inherited from B
obj_c.method_c1()
obj_c.method_c2()
obj_c.show()  # Overridden method in C

#Create a class with main method. Create an object for each class A, B and C in main
#method and call every method of each class using its own object/instance.
# Superclass A
class A:
    def method_a1(self):
        print("Method A1: Unique to Class A")

    def method_a2(self):
        print("Method A2: Unique to Class A")

    def show(self):  # Overridden method
        print("Show method from Class A")

# Subclass B (Inherits from A)
class B(A):
    def method_b1(self):
        print("Method B1: Unique to Class B")

    def method_b2(self):
        print("Method B2: Unique to Class B")

    def show(self):  # Overriding method
        print("Show method from Class B")

# Subclass C (Inherits from B)
class C(B):
    def method_c1(self):
        print("Method C1: Unique to Class C")

    def method_c2(self):
        print("Method C2: Unique to Class C")

    def show(self):  # Overriding method
        print("Show method from Class C")

# Main Class
class Main:
    def main_method():
        # Creating objects for each class
        obj_a = A()
        obj_b = B()
        obj_c = C()

        # Calling methods from Class A
        print("\nCalling methods from Class A:")
        obj_a.method_a1()
        obj_a.method_a2()
        obj_a.show()

        # Calling methods from Class B
        print("\nCalling methods from Class B:")
        obj_b.method_a1()  # Inherited from A
        obj_b.method_b1()
        obj_b.method_b2()
        obj_b.show()  # Overridden method

        # Calling methods from Class C
        print("\nCalling methods from Class C:")
        obj_c.method_a1()  # Inherited from A
        obj_c.method_b1()  # Inherited from B
        obj_c.method_c1()
        obj_c.method_c2()
        obj_c.show()  # Overridden method in C

# Calling the main method
if __name__ == "__main__":
    Main.main_method()

#Call an overridden method with super class reference to B and C class’s objects


# Superclass A
class A:
    def method_a1(self):
        print("Method A1: Unique to Class A")

    def method_a2(self):
        print("Method A2: Unique to Class A")

    def show(self):  # Overridden method
        print("Show method from Class A")

# Subclass B (Inherits from A)
class B(A):
    def method_b1(self):
        print("Method B1: Unique to Class B")

    def method_b2(self):
        print("Method B2: Unique to Class B")

    def show(self):  # Overriding method
        print("Show method from Class B")

# Subclass C (Inherits from B)
class C(B):
    def method_c1(self):
        print("Method C1: Unique to Class C")

    def method_c2(self):
        print("Method C2: Unique to Class C")

    def show(self):  # Overriding method
        print("Show method from Class C")

# Main function
if __name__ == "__main__":
    # Superclass reference pointing to Subclass B
    ref_b = A()  # Superclass object
    ref_b.show()  # Calls A's show()

    ref_b = B()  # Reference of A pointing to B
    ref_b.show()  # Calls B's overridden show()

    # Superclass reference pointing to Subclass C
    ref_c = C()  # Reference of A pointing to C
    ref_c.show()  # Calls C's overridden show()

#Runtime Polymorphism with Data Members/Instance variables, Repeat the above
#process only for data members
# Superclass A
class A:
    def __init__(self):
        self.value = "Value from Class A"

# Subclass B (Inherits from A)
class B(A):
    def __init__(self):
        super().__init__()  # Calls A's constructor
        self.value = "Value from Class B"  # Overrides the instance variable

# Subclass C (Inherits from B)
class C(B):
    def __init__(self):
        super().__init__()  # Calls B's constructor
        self.value = "Value from Class C"  # Overrides the instance variable

# Main function
if __name__ == "__main__":
    # Superclass reference pointing to subclass objects
    ref_b = A()  # A's object
    print(ref_b.value)  # Output: "Value from Class A"

    ref_b = B()  # A's reference pointing to B
    print(ref_b.value)  # Output: "Value from Class B"

    ref_c = C()  # A's reference pointing to C
    print(ref_c.value)  # Output: "Value from Class C"

#8-Access modifiers
#Create a class with PRIVATE fields, private method and a main method. Print the fields
#in main method. Call the private method in main method.
#Create a sub class and try to access the private fields and methods from sub class.
# Superclass with private fields and methods
class A:
    def __init__(self):
        self.__private_field = "I am a private field"  # Private instance variable

    def __private_method(self):
        print("I am a private method")

    def access_private_members(self):
        # Accessing private field and method inside the class
        print(self.__private_field)
        self.__private_method()


# Subclass attempting to access private members
class B(A):
    def try_access_private(self):
        try:
            print(self.__private_field)  # Attempt to access private field (Will fail)
        except AttributeError:
            print("Cannot access private field directly in subclass!")

        try:
            self.__private_method()  # Attempt to access private method (Will fail)
        except AttributeError:
            print("Cannot access private method directly in subclass!")


# Main function
if __name__ == "__main__":
    obj_a = A()

    print("Accessing private members inside class:")
    obj_a.access_private_members()  # Works because it's inside the class

    print("\nTrying to access private members outside the class:")
    try:
        print(obj_a.__private_field)  # Will cause an error
    except AttributeError:
        print("Cannot access private field directly!")

    try:
        obj_a.__private_method()  # Will cause an error
    except AttributeError:
        print("Cannot access private method directly!")

    # Subclass attempting to access private members
    obj_b = B()
    print("\nAccessing private members from subclass:")
    obj_b.try_access_private()

#Create a class with PROTECTED fields and methods. Access these fields and methods
#from any other class in the same package.
#Also, Access the PROTECTED fields and methods from child class located in a different package
#Access the PROTECTED fields and methods from any class in different package

# File: package1/class_a.py
class A:
    def __init__(self):
        self._protected_field = "I am a protected field"

    def _protected_method(self):
        print("I am a protected method")

# Another class in the same package
class SamePackageClass:
    def access_protected(self):
        obj = A()
        print("Accessing protected field in same package:", obj._protected_field)
        obj._protected_method()

#Create a class with PUBLIC fields and methods.
#Access the public methods and fields from any class in the same package or different package.

# File: package1/class_a.py
class A:
    def __init__(self):
        self.public_field = "I am a public field"

    def public_method(self):
        print("I am a public method")

# Another class in the same package
class SamePackageClass:
    def access_public(self):
        obj = A()
        print("Accessing public field in same package:", obj.public_field)
        obj.public_method()

#9-Abstract class
#Create an abstract class with abstract and non-abstract methods
from abc import ABC, abstractmethod

# Abstract class
class AbstractClass(ABC):

    def __init__(self):
        self.value = "This is a non-abstract field in an abstract class"

    @abstractmethod
    def abstract_method(self):
        """This is an abstract method that must be implemented in a subclass."""
        pass

    def non_abstract_method(self):
        """This is a regular method that can be inherited without changes."""
        print("This is a non-abstract method.")

# Concrete subclass implementing the abstract method
class ConcreteClass(AbstractClass):

    def abstract_method(self):
        print("Implemented abstract method in ConcreteClass.")

# Main Execution
if __name__ == "__main__":
    # obj = AbstractClass()  # ❌ This will raise an error! Abstract classes cannot be instantiated.

    obj = ConcreteClass()
    obj.abstract_method()      # ✅ Implemented method will be called
    obj.non_abstract_method()  # ✅ Non-abstract method inherited and called
    print(obj.value)           # ✅ Accessing non-abstract field

#Create a sub class for an abstract class. Create an object in the child class for the
#abstract class and access the non-abstract methods
from abc import ABC, abstractmethod

# Abstract Class
class AbstractClass(ABC):

    def __init__(self):
        self.value = "This is a non-abstract field from AbstractClass"

    @abstractmethod
    def abstract_method(self):
        """Abstract method that must be implemented in a subclass."""
        pass

    def non_abstract_method(self):
        """Non-abstract method that can be used by subclasses."""
        print("This is a non-abstract method from AbstractClass.")

# Subclass Implementing Abstract Method
class ConcreteClass(AbstractClass):

    def __init__(self):
        # Creating an instance of the abstract class within the subclass
        super().__init__()

    def abstract_method(self):
        print("Implemented abstract method in ConcreteClass.")

    def access_abstract_class_methods(self):
        """Accessing non-abstract method from the abstract class"""
        self.non_abstract_method()  # Calling non-abstract method
        print(self.value)  # Accessing non-abstract field

# Main Execution
if __name__ == "__main__":
    obj = ConcreteClass()
    obj.abstract_method()  # ✅ Implemented abstract method
    obj.access_abstract_class_methods()  # ✅ Accessing non-abstract method


#Create an instance for the child class in child class and call abstract methods

from abc import ABC, abstractmethod

# Abstract Class
class AbstractClass(ABC):

    @abstractmethod
    def abstract_method(self):
        """Abstract method that must be implemented in a subclass."""
        pass

# Subclass Implementing Abstract Method
class ConcreteClass(AbstractClass):

    def abstract_method(self):
        print("Implemented abstract method in ConcreteClass.")

    def create_and_call(self):
        """Creates an instance of ConcreteClass and calls the abstract method"""
        obj = ConcreteClass()  # Creating an instance of itself
        obj.abstract_method()  # Calling the abstract method

# Main Execution
if __name__ == "__main__":
    obj = ConcreteClass()
    obj.create_and_call()  # ✅ Creating instance inside itself and calling abstract method

#Create an instance for the child class in child class and call non-abstract methods
from abc import ABC, abstractmethod

# Abstract Class
class AbstractClass(ABC):

    def non_abstract_method(self):
        """This is a non-abstract method"""
        print("This is a non-abstract method from AbstractClass.")

    @abstractmethod
    def abstract_method(self):
        """Abstract method that must be implemented in a subclass."""
        pass

# Subclass Implementing Abstract Method
class ConcreteClass(AbstractClass):

    def abstract_method(self):
        print("Implemented abstract method in ConcreteClass.")

    def create_and_call(self):
        """Creates an instance of ConcreteClass and calls non-abstract methods"""
        obj = ConcreteClass()  # Creating an instance of itself
        obj.non_abstract_method()  # Calling non-abstract method

# Main Execution
if __name__ == "__main__":
    obj = ConcreteClass()
    obj.create_and_call()  # ✅ Creating instance inside itself and calling non-abstract method

#10-packages
#Create a program to create two class.
# 1.1. Create a constructor and a method for each class
# 1.2. Create a __init__.py for adding all packages1.3. Import the respective packages
# 1.4. Call each class by creating an object to it
#1.5. Create a program by all the above

# File: package1/class_a.py
class ClassA:
    def __init__(self):
        print("ClassA Constructor Called")

    def method_a(self):
        print("Method from ClassA")

# File: package2/class_b.py
class ClassB:
    def __init__(self):
        print("ClassB Constructor Called")

    def method_b(self):
        print("Method from ClassB")

# This file allows `package1` to be treated as a package
# This file allows `package2` to be treated as a package

#11-Files
#Write a program to read text file
# Open and read a text file
file_path = "sample.txt"  # Replace with your actual file path

try:
    with open(file_path, "r") as file:
        content = file.read()  # Read entire file content
        print("File Content:\n")
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
#Write a program to write text to .txt file using InputStream
with open("output.txt", "a") as file:
    file.write("\nAdditional text appended.")  # Appends text to the file

#Write a program to read a file stream
# Define file path
file_path = "sample.txt"  # Replace with your actual file name

# Open file in read mode
try:
    with open(file_path, "r") as file:
        print("Reading file stream...\n")

        # Read file content
        for line in file:
            print(line.strip())  # strip() removes extra spaces and newline characters

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

#Write a program to read a file stream supports random access

# Define file path
file_path = "sample.txt"  # Replace with your actual file name

try:
    with open(file_path, "r") as file:
        print("Reading file stream with random access...\n")

        # Move to the 10th byte (character)
        file.seek(10)
        print(f"Reading from position 10: {file.read(10)}")  # Read next 10 characters

        # Move to the beginning
        file.seek(0)
        print(f"\nReading first line: {file.readline().strip()}")

        # Move to a specific position and read one character
        file.seek(5)
        print(f"\nReading character at position 5: {file.read(1)}")

        # Check current position
        print(f"\nCurrent file position: {file.tell()}")

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

#Write a program to read a file a just to a particular index using seek()
# Define file path
file_path = "sample.txt"  # Replace with your actual file name

try:
    with open(file_path, "r") as file:
        # Move to the specified index (e.g., 15th byte)
        index = 15
        file.seek(index)

        # Read content from the index onward
        content = file.read(20)  # Read next 20 characters
        print(f"Content from index {index}: {content}")

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

#Write a program to check whether a file is having read access and write access permissions
import os

# Define file path
file_path = "sample.txt"  # Replace with your actual file name

# Check read permission
has_read_access = os.access(file_path, os.R_OK)

# Check write permission
has_write_access = os.access(file_path, os.W_OK)

# Display the results
print(f"File: {file_path}")
print(f"Read Access: {'Yes' if has_read_access else 'No'}")
print(f"Write Access: {'Yes' if has_write_access else 'No'}")

#12-Constructors

#Write a class with a default constructor, one argument constructor and two argument
#constructors. Instantiate the class to call all the constructors of that class from a main class
class MyClass:
    # Constructor with default arguments
    def __init__(self, arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            print("Default constructor called.")
        elif arg2 is None:
            print(f"One-argument constructor called: arg1 = {arg1}")
        else:
            print(f"Two-argument constructor called: arg1 = {arg1}, arg2 = {arg2}")

# Main class to instantiate objects and call constructors
if __name__ == "__main__":
    obj1 = MyClass()         # Calls default constructor
    obj2 = MyClass(10)       # Calls one-argument constructor
    obj3 = MyClass(10, 20)   # Calls two-argument constructor

#Call the constructors(both default and argument constructors) of super class from a child class
# Superclass (Parent)
class Parent:
    def __init__(self, arg1=None):
        if arg1 is None:
            print("Parent Default Constructor Called")
        else:
            print(f"Parent One-Argument Constructor Called: arg1 = {arg1}")

# Subclass (Child)
class Child(Parent):
    def __init__(self, arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            super().__init__()  # Calls Parent's default constructor
            print("Child Default Constructor Called")
        elif arg2 is None:
            super().__init__(arg1)  # Calls Parent's one-argument constructor
            print(f"Child One-Argument Constructor Called: arg1 = {arg1}")
        else:
            super().__init__(arg1)  # Calls Parent's one-argument constructor
            print(f"Child Two-Argument Constructor Called: arg1 = {arg1}, arg2 = {arg2}")

# Main Class to Instantiate Objects
if __name__ == "__main__":
    obj1 = Child()          # Calls Parent default and Child default constructor
    obj2 = Child(10)        # Calls Parent one-argument and Child one-argument constructor
    obj3 = Child(10, 20)    # Calls Parent one-argument and Child two-argument constructor

#Apply private, public, protected and default access modifiers to the constructor
class Example:
    # Public Constructor
    def __init__(self):
        print("Public Constructor Called")

    # Protected Constructor (not enforced but indicated for internal use)
    def _protected_constructor(self):
        print("Protected Constructor Called")

    # Private Constructor (name mangled)
    def __private_constructor(self):
        print("Private Constructor Called")

    # Public method to call private constructor
    def access_private(self):
        self.__private_constructor()  # Allowed inside the class

# Public Constructor: Direct Access
obj = Example()

# Protected Constructor: Can be accessed, but not recommended
obj._protected_constructor()

# Private Constructor: Cannot be accessed directly
try:
    obj.__private_constructor()  # Will raise an AttributeError
except AttributeError:
    print("Cannot access private constructor directly!")

# Accessing Private Constructor through a Public Method
obj.access_private()

#Write a program which illustrates the concept of attributes of a constructor.
class Person:
    # Constructor with attributes
    def __init__(self, name, age, city="Unknown"):
        self.name = name      # Public Attribute
        self.age = age        # Public Attribute
        self.city = city      # Default argument (optional)

    # Method to display attributes
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, City: {self.city}")

# Creating objects with different attribute values
person1 = Person("Alice", 25, "New York")  # Passing all arguments
person2 = Person("Bob", 30)                # Uses default value for 'city'

# Accessing attributes and displaying information
person1.display_info()
person2.display_info()

# Modifying attributes
person2.city = "Los Angeles"
print(f"Updated City for Bob: {person2.city}")

#13-METHOD OVERLOADING
#Write two methods with the same name but different number of parameters of same type
#and call the methods
class Calculator:
    # Method with different number of parameters using default values
    def add(self, a, b=0, c=0):
        return a + b + c

# Creating object
calc = Calculator()

# Calling the overloaded method with different number of arguments
print(calc.add(10))       # Calls add(10, 0, 0) → Output: 10
print(calc.add(10, 20))   # Calls add(10, 20, 0) → Output: 30
print(calc.add(10, 20, 30)) # Calls add(10, 20, 30) → Output: 60

#Write two methods with the same name but different number of parameters of different
#data type and call the methods
class Demo:
    def show(self, a, b=None):
        if b is None:  # Single parameter
            print(f"Single argument: {a} (Type: {type(a).__name__})")
        else:  # Two parameters
            print(f"Two arguments: {a} (Type: {type(a).__name__}), {b} (Type: {type(b).__name__})")

# Creating object
obj = Demo()

# Calling method with different parameter types
obj.show(10)        # Integer
obj.show("Hello")   # String
obj.show(10, "Hi")  # Integer and String
obj.show(5.5, 20)   # Float and Integer

#Write two methods with the same name and same number of parameters of same type
class Demo:
    def show(self, a, b):
        print(f"Method 1: Sum = {a + b}")

    def show(self, a, b):  # This method overrides the previous one
        print(f"Method 2: Product = {a * b}")

# Creating object
obj = Demo()

# Calling the method
obj.show(5, 3)  # Calls the last defined method

#14-EXCEPTIONS
#Write a program to generate Arithmetic Exception without exception handling
# Attempting to divide by zero (causes ZeroDivisionError)
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero! Handling exception.")

#Handle the Arithmetic exception using try-catch block
try:
    # Attempting division by zero
    result = 10 / 0
    print("Result:", result)  # This line will not execute
except ZeroDivisionError:
    print("Error: Cannot divide by zero! Exception handled.")

print("Program continues after handling the exception.")

#Write a method which throws exception, Call that method in main class without try block
# Example of an exception
n = 10
try:
    res = n / 0  # This will raise a ZeroDivisionError

except ZeroDivisionError:
    print("Can't be divided by zero!")
#Write a program with multiple catch blocks
try:
    a = int(input("Enter numerator: "))  # May raise ValueError
    b = int(input("Enter denominator: "))  # May raise ValueError
    result = a / b  # May raise ZeroDivisionError
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input! Please enter numbers only.")
except Exception as e:  # Generic exception handler
    print("An unexpected error occurred:", e)

print("Program continues after handling exceptions.")

#Write a program to throw exception with your own message
class MyCustomError(Exception):
    """Exception raised for custom error scenarios.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

#Write a program to create your own exception
class InsufficientBalanceError(Exception):
    def __init__(self, balance, withdraw_amount):
        super().__init__(f"Insufficient Balance! Available: {balance}, Requested: {withdraw_amount}")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError(balance, amount)
    else:
        print(f"Withdrawal Successful! New Balance: {balance - amount}")

try:
    withdraw(500, 1000)  # Trying to withdraw more than available balance
except InsufficientBalanceError as e:
    print("Custom Exception Caught:", e)

#Write a program with finally block
try:
    file = open("example.txt", "r")  # Open a file for reading
    content = file.read()
    print(content)

except FileNotFoundError:
    print("Error: File not found!")

finally:
    print("Closing the file.")
    file.close()  # Ensuring the file is closed

#. Write a program to generate Arithmetic Exception
try:
    num1 = 10
    num2 = 0
    result = num1 / num2  # Causes ZeroDivisionError
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

#Write a program to generate FileNotFoundException

# Attempting to open a non-existing file
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: The file does not exist!")

#Write a program to generate ClassNotFoundException
try:
    # Trying to import a class that does not exist
    from nonexistent_module import NonExistentClass
except ImportError:
    print("Error: The class could not be found!")

#Write a program to generate IOException
try:
    # Trying to open a non-existing file to generate an IOException (OSError in Python)
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except OSError as e:
    print(f"Error: {e}")

#Write a program to generate NoSuchFieldException
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

try:
    person = Person("Alice", 30)
    # Trying to access a field that does not exist
    print(person.address)  # This will generate an AttributeError
except AttributeError as e:
    print(f"Error: {e}")

#15-DICTIONARY


#Create a Dictionary with at least 5 key value pairs of the Student ID and Name
#1.1. Adding the values in dictionary
#1.2. Updating the values in dictionary
#1.3. Accessing the value in dictionary
#1.4. Create a nested loop dictionary
#1.5. Access the values of nested loop dictionary
#1.6. Print the keys present in a particular dictionary
#1.7. Delete a value from a dictionary

# Step 1.1: Create a Dictionary
students = {
    101: "Alice",
    102: "Bob",
    103: "Charlie",
    104: "David",
    105: "Eva"
}

# Step 1.2: Add a New Student
students[106] = "Frank"
print("Dictionary after adding a new student:", students)

# Step 1.3: Update a Student's Name
students[103] = "Charlotte"
print("Dictionary after updating a student's name:", students)

# Step 1.4: Access a Student's Name
student_name = students[102]
print("The name of the student with ID 102 is:", student_name)

# Step 1.5: Create a Nested Dictionary
nested_students = {
    101: {"name": "Alice", "age": 20, "major": "Computer Science"},
    102: {"name": "Bob", "age": 22, "major": "Mathematics"},
    103: {"name": "Charlie", "age": 21, "major": "Physics"}
}

# Step 1.6: Access Nested Dictionary Values
charlie_major = nested_students[103]["major"]
print("Charlie's major is:", charlie_major)

# Step 1.7: Print the Keys
print("Keys in the students dictionary:", students.keys())
print("Keys in the nested students dictionary:", nested_students.keys())

# Step 1.8: Delete a Value
del students[105]
print("Dictionary after deleting student with ID 105:", students)
