#no input, no return 
def my_first_function():
    a = 10
    b = 12
    print(a + b)

my_first_function()

#input, no return
def add_two_numbers(a,b): #a and b are parameters, they are placeholders for the values that will be passed to the function when we call it.
    print(a + b)
add_two_numbers(5, 10) # 5 and 10 are arguments, they are passed to the function when we call it. We can also pass variables as arguments instead of hardcoding values.
add_two_numbers(5, 10)

#input, return
def multiply_two_numbers(a,b):
    return a * b
result = multiply_two_numbers(5, 10) # return value has to be stored in a variable
print(result) 


#multiple arguments
def adddtion(*args): # *args allows us to pass a variable number of arguments to the function. It collects all the arguments passed to the function into a tuple.
    return sum(args) # sum() is a built-in function that takes an iterable (like a list or tuple) and returns the sum of its elements.
result = adddtion(1, 2, 3, 4, 5) # we can pass as many arguments as we want to the function when we call it.

print(result)   


# keyword arguments
def my_function(f_name, l_name, age):
    print(f"Hello, my name is {f_name} {l_name} and I am {age} years old.")

my_function("John", "Doe", 30)

my_function(f_name="John", l_name="Doe", age=30) # when we use keyword arguments, we can specify the values for the parameters by their names, which allows us to pass the arguments in any order. This can make our code more readable and less error-prone, especially when we have functions with many parameters.


def my_function(**kwargs): # **kwargs allows us to pass a variable number of keyword arguments to the function. It collects all the keyword arguments passed to the function into a dictionary.
    print(f"Hello, my name is {kwargs['f_name']} {kwargs['l_name']} and I am {kwargs['age']} years old.")

my_function("John", "Doe", 30)

my_function(f_name="John", l_name="Doe", age=30)