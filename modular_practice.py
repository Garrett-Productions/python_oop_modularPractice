import parent

#LINE 34 AND ON IS LINE FOR LINE WHAT IS WRITTEN IN MY PARENT FILE, commented out
#it's only written here so I can upload only 1 file.

#You should see a directory called __pycache__ which contains a .pyc file. 
# This file contains Python bytecode - the language the Python interpreter speaks. 
# Since these files are in a language Python knows so we can run them like any other 
# Python file: (e.g., python __pycache__/parent.cpython-36.pyc).

#this happens when a module is imported... the .pyc thing
#Once a .pyc file is generated, as long as we don't change that file, 
#Python will not have to re-compile your code to bytecode, which may save processing time when working with large code bases.

#__name__    #NAMESPACE

#Namespace is important because we have to know what variables we have access to. 
#To see what variables are available in any given place, add the line print(locals())   #LOCALS() IS A BUILT IN FUNCTION
#and see what variables are in your current namespace. 
#The object that prints will be a dictionary where the variable names are keys and the objects they reference are the values. 
#Understanding namespace will help you understand the next portion, where we will use namespace to control the functionality that is imported with our document.

#How is this useful? We can use this conditional to prevent blocks of code from executing unless the file is being run directly. 
# Why would we want to do this? Consider a situation where one class depends on another, as in the Users with Bank Accounts assignment. 
# In our product document we might create a lot of test code to make sure we can create new products and execute methods. 
# When we import products to the store file as a module, we don’t want to see all of those tests run every time we execute the store file, 
# so inside of our product document, we might have something like below:

# if __name__ == "__main__":
#     product = Product([args])
#     print(product)
#     print(product.add_tax(0.18))

# local_val = "magical unicorns"
# def square(x):
#     return x * x
# class User:
#     def __init__(self, name):
#         self.name = name
#     def say_hello(self):
#         return "hello"

# # in the same file, add the following below the User class
# print(square(5))
# user = User("Anna")
# print(user.name)
# print(user.say_hello())

# print(__name__)
# print(locals())

# if __name__ == "__main__":
#     print("the file is being executed directly")
# else:
#     print("The file is being executed because it is imported by another file. The file is called: ", __name__)

