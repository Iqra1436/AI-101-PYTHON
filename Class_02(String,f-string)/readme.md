String Definitions
Single Quotes

You can define a string with single quotes.

my_string: str = 'Hello, World!'

Double Quotes

Alternatively, you can define a string with double quotes.

my_string: str = "Hello, World!"

Triple Single Quotes

Triple single quotes allow for string definitions that span multiple lines.

my_string: str = '''Hello,
World!'''

Triple Double Quotes

Like triple single quotes, triple double quotes also allow for multi-line string definitions.

my_string: str = """Hello,
World!"""

String Formatting
Basic Techniques
Using %s and %d

You can use %s for string and %d for integers.

name: str = "Alice"
age: int = 30
print("My name is %s and I am %d years old." % (name, age))

Using .format()

The .format() method is another way to format your strings.

name: str = "Alice"
age: int = 30
print("My name is {} and I am {} years old.".format(name, age))

Using f-string (Python 3.6+)

f-strings provide a concise and readable way to include the value of Python expressions inside strings.

name: str = "Alice"
age: int = 30
print(f"My name is {name} and I am {age} years old.")

Advanced Techniques
f-string Expressions

You can include Python expressions within f-strings.

x: int = 10
y: int = 20
print(f"The sum of {x} and {y} is {x+y}.")

f-string with Format Specification

You can format numbers using f-strings.

pi: float = 3.14159
print(f"Value of pi to 2 decimal places: {pi:.2f}")

Naming Conventions
Variables

    Use snake_case for variable names.

my_variable: int = 10

Constants

    Use UPPER_SNAKE_CASE for constants.

PI: float = 3.14159