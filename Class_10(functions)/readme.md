Python Functions Guide

Python functions are a cornerstone of the language, providing modularity and code reusability.

    Pre-defined Functions: Python comes with a variety of built-in functions like len() that are ready to use without any additional imports.
    User-defined Functions: Users can define their own functions using the def keyword, allowing for customized functionality tailored to specific needs.
    Arguments and Parameters: Functions can accept inputs in the form of arguments, and these inputs are defined in the function signature as parameters.
    Default Functions: Parameters can be given default values, making them optional when the function is called.
    Optional, Positional, and Keyword Arguments: Functions can accept different types of arguments, including optional arguments with default values, positional arguments that depend on order, and keyword arguments that are specified by name.
    Lambda Functions: Anonymous functions can be defined on-the-fly using the lambda keyword.
    Recursive Functions: Functions can call themselves to solve problems in a recursive manner.
    Decorators: Functions can be wrapped by other functions to extend their behavior without modifying their code.
    Functions with Unlimited Arguments: Functions can be designed to accept an arbitrary number of arguments, either as positional arguments or keyword arguments.

By understanding and utilizing these different aspects of Python functions, developers can write cleaner, more efficient, and more maintainable code.
Table of Contents

    Pre-defined Functions
    User-defined Functions
    Arguments and Parameters
    Default Functions
    Optional, Positional, and Keyword Arguments
    Lambda Functions
    Recursive Functions
    Decorators
    Functions with Unlimited Arguments

YouTube link

2 hour live session
Pre-defined Functions

Python provides several built-in functions that are readily available for use.

# Example of a pre-defined function
result: int = len("Hello, World!")
print(result)  # Output: 12

User-defined Functions

You can define your own functions in Python using the def keyword.

def greet(name: str) -> None:
    print(f"Hello, {name}!")

greet("John")  # Output: Hello, John!

Arguments and Parameters

Parameters are the variables listed inside the parentheses in the function definition, whereas arguments are the values passed to the function when it is called.

def add(a: int, b: int) -> int:
    return a + b

result: int = add(5, 3)
print(result)  # Output: 8

Default Functions

You can assign default values to parameters, making them optional during a function call.

def power(base: int, exponent: int = 2) -> int:
    return base ** exponent

print(power(3))        # Output: 9
print(power(3, 3))     # Output: 27

Optional, Positional, and Keyword Arguments
Optional Arguments

Optional arguments are those that have a default value.

def greet(name: str = "Guest") -> None:
    print(f"Hello, {name}!")

greet()            # Output: Hello, Guest!
greet("John")      # Output: Hello, John!

Positional Arguments

Positional arguments are arguments that need to be included in the proper position or order.

def subtract(a: int, b: int) -> int:
    return a - b

result: int = subtract(10, 5)
print(result)  # Output: 5

Keyword Arguments

Keyword arguments are arguments passed to a function by explicitly specifying the name of the parameter.

def divide(dividend: int, divisor: int) -> float:
    return dividend / divisor

result: float = divide(divisor=5, dividend=25)
print(result)  # Output: 5.0

Lambda Functions

Lambda functions are anonymous functions defined using the lambda keyword.

square: callable = lambda x: x * x
print(square(4))  # Output: 16

Recursive Functions

A recursive function is a function that calls itself.

def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result: int = factorial(5)
print(result)  # Output: 120

Decorators

Decorators are a way to modify or extend the behavior of a function.

def my_decorator(func: callable) -> callable:
    def wrapper(*args, **kwargs) -> None:
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello(name: str) -> None:
    print(f"Hello {name}!")

say_hello("John")

Functions with Unlimited Arguments

You can define functions that accept an arbitrary number of arguments.
Unlimited Positional Arguments

def add(*numbers: int) -> int:
    return sum(numbers)

result: int = add(1, 2, 3, 4, 5)
print(result)  # Output: 15

Unlimited Keyword Arguments

def print_key_values(**kwargs: str) -> None:
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_key_values(name="John", age="30", country="USA")

