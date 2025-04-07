# flashcards/data.py

flashcards = [
    { "question": "What symbol is used to assign a value to a variable in Python?", "answer": "=" },  # = assignment
    { "question": "What operator checks if two values are equal?", "answer": "==" },  # == comparison
    { "question": "What operator checks if two values are not equal?", "answer": "!=" },  # != not equal
    { "question": "What operator checks if one value is greater than another?", "answer": ">" },  # >
    { "question": "What operator checks if one value is less than another?", "answer": "<" },  # <
    { "question": "What operator checks if one value is greater than or equal to another?", "answer": ">=" },  # >=
    { "question": "What operator checks if one value is less than or equal to another?", "answer": "<=" },  # <=
    { "question": "What operator adds numbers or joins strings?", "answer": "+" },  # +
    { "question": "What operator subtracts numbers?", "answer": "-" },  # -
    { "question": "What operator multiplies numbers?", "answer": "*" },  # *
    { "question": "What operator divides and returns float?", "answer": "/" },  # /
    { "question": "What operator does floor division?", "answer": "//" },  # //
    { "question": "What operator gives remainder?", "answer": "%" },  # %
    { "question": "What operator does exponentiation?", "answer": "**" },  # **
    { "question": "What does += mean?", "answer": "+=" },  # add and assign
    { "question": "What does -= mean?", "answer": "-=" },  # subtract and assign
    { "question": "What does *= mean?", "answer": "*=" },  # multiply and assign
    { "question": "What does /= mean?", "answer": "/=" },  # divide and assign
    { "question": "What symbol starts a comment?", "answer": "#" },  # comment
    { "question": "What keyword defines a function?", "answer": "def" },  # def
    { "question": "What keyword returns from a function?", "answer": "return" },  # return
    { "question": "What keyword starts a condition?", "answer": "if" },  # if
    { "question": "What keyword checks another condition?", "answer": "elif" },  # elif
    { "question": "What keyword runs if all others fail?", "answer": "else" },  # else
    { "question": "What loop runs while a condition is true?", "answer": "while" },  # while
    { "question": "What loop runs over a sequence?", "answer": "for" },  # for
    { "question": "What checks if something is in a list?", "answer": "in" },  # in
    { "question": "What stops a loop early?", "answer": "break" },  # break
    { "question": "What skips to the next loop iteration?", "answer": "continue" },  # continue
    { "question": "What does nothing and acts as a placeholder?", "answer": "pass" },  # pass
    { "question": "What value means true?", "answer": "True" },  # True
    { "question": "What value means false?", "answer": "False" },  # False
    { "question": "What keyword means 'no value'?", "answer": "None" },  # None
    { "question": "What logical operator means both must be true?", "answer": "and" },  # and
    { "question": "What logical operator means either can be true?", "answer": "or" },  # or
    { "question": "What logical operator inverts a value?", "answer": "not" },  # not
    { "question": "What symbols are used for functions and grouping?", "answer": "()" },  # ()
    { "question": "What symbols are used for lists and indexes?", "answer": "[]" },  # []
    { "question": "What symbols are used for dicts or sets?", "answer": "{}" },  # {}
    { "question": "What symbol starts a code block?", "answer": ":" },  # colon
    { "question": "What separates arguments or items?", "answer": "," },  # comma
    { "question": "What symbols wrap string values (double)?", "answer": "\"\"" },  # double quotes
    { "question": "What symbols wrap string values (single)?", "answer": "''" },  # single quotes
    { "question": "What function gets user input?", "answer": "input()" },  # input()
    { "question": "What function shows output?", "answer": "print()" },  # print()
    { "question": "What function gives the length of an object?", "answer": "len()" },  # len()
    { "question": "What function creates a number sequence?", "answer": "range()" },  # range()
    { "question": "What converts a value to string?", "answer": "str()" },  # str()
    { "question": "What converts a value to integer?", "answer": "int()" },  # int()
    { "question": "What converts a value to float?", "answer": "float()" },  # float()
    {"question": "What data type is used to store True or False?", "answer": "bool"},
    {"question": "What method would you use to add an item to the end of a list?", "answer": "append()"},
    {"question": "What method removes and returns the last item in a list?", "answer": "pop()"},
    {"question": "What Python keyword is used to start a class definition?", "answer": "class"},
    {"question": "How do you create a comment that spans multiple lines?", "answer": "''' or \"\"\""},
    {"question": "How do you check the type of a variable?", "answer": "type()"},
    {"question": "What method would you use to convert a string to uppercase?", "answer": "upper()"},
    {"question": "What operator is used to raise a number to a power?", "answer": "**"},
    {"question": "What keyword is used to import a module?", "answer": "import"},
    {"question": "What function is used to get the absolute value?", "answer": "abs()"},
    {"question": "What built-in function returns the max value from a list?", "answer": "max()"},
    {"question": "What built-in function returns the min value from a list?", "answer": "min()"},
    {"question": "What function converts an iterable into a list?", "answer": "list()"},
    {"question": "How do you handle exceptions in Python?", "answer": "try/except"},
    {"question": "What keyword is used to define a generator function?", "answer": "yield"},
    {"question": "What function combines two lists into a tuple-pair?", "answer": "zip()"},
    {"question": "What keyword is used to delete a variable?", "answer": "del"},
    {"question": "How do you get keys from a dictionary?", "answer": "dict.keys()"},
    {"question": "How do you get values from a dictionary?", "answer": "dict.values()"},
    {"question": "How do you get items from a dictionary?", "answer": "dict.items()"},
    {"question": "How do you open a file in write mode?", "answer": "open('file.txt', 'w')"},
    {"question": "What method reads an entire file as a string?", "answer": "read()"},
    {"question": "What method reads a file line by line?", "answer": "readlines()"},
    {"question": "What function is used to round a float?", "answer": "round()"},
    {"question": "How do you join a list into a single string?", "answer": "'separator'.join(list)"},
    {"question": "What does the 'with' keyword do in file operations?", "answer": "Automatically closes file"},
    {"question": "What keyword is used to raise an exception?", "answer": "raise"},
    {"question": "What function returns a sorted version of a list?", "answer": "sorted()"},
    {"question": "How do you create a list of numbers from 0 to 9?", "answer": "list(range(10))"},
    {"question": "What Python function returns a unique set from a list?", "answer": "set()"},
    {"question": "How do you define a dictionary?", "answer": "{} or dict()"},
    {"question": "How do you access the first character of a string?", "answer": "string[0]"},
    {"question": "What method removes whitespace from both ends of a string?", "answer": "strip()"},
    {"question": "What function is used to evaluate a string as Python code?", "answer": "eval()"},
    {"question": "What operator is used to concatenate strings?", "answer": "+"},
    {"question": "How do you create a new line in a string?", "answer": "\\n"},
    {"question": "How do you escape quotes in a string?", "answer": "\\\""},
    {"question": "What method replaces a part of a string?", "answer": "replace()"},
    {"question": "How do you format strings using f-strings?", "answer": "f'Hello {name}'"},
    {"question": "What function pauses the program for input?", "answer": "input()"},
    {"question": "How do you define a dictionary?", "answer": "{} or dict()"},
    {"question": "How do you access the first character of a string?", "answer": "string[0]"},
    {"question": "What method removes whitespace from both ends of a string?", "answer": "strip()"},
    {"question": "What function is used to evaluate a string as Python code?", "answer": "eval()"},
    {"question": "What operator is used to concatenate strings?", "answer": "+"},
    {"question": "How do you create a new line in a string?", "answer": "\\n"},
    {"question": "How do you escape quotes in a string?", "answer": "\\\""},
    {"question": "What method replaces a part of a string?", "answer": "replace()"},
    {"question": "How do you format strings using f-strings?", "answer": "f'Hello {name}'"},
    {"question": "What function pauses the program for input?", "answer": "input()"},
    {"question": "What is this called? def example_4u():", "answer": "function definition"},
    {"question": "What is a named block of code that runs when called?", "answer": "function"},
    {"question": "What keyword is used to define a function?", "answer": "def"},
    {"question": "What do we call values passed into a function?", "answer": "arguments"},
    {"question": "What are variables inside parentheses of a function definition?", "answer": "parameters"},
    {"question": "What does a function return if it has no return statement?", "answer": "None"},
    {"question": "What Python keyword exits a function and sends back a value?", "answer": "return"},
    {"question": "What keyword is used to include external Python code?", "answer": "import"},
    {"question": "What do you call code that runs only if a condition is true?", "answer": "if statement"},
    {"question": "What keyword runs if the 'if' is false but a new condition is true?", "answer": "elif"},
    {"question": "What do we call the last fallback condition in if/else logic?", "answer": "else"},
    {"question": "What loop continues as long as a condition is true?", "answer": "while loop"},
    {"question": "What loop runs a fixed number of times over a sequence?", "answer": "for loop"},
    {"question": "What keyword skips the rest of the current loop iteration?", "answer": "continue"},
    {"question": "What keyword exits the entire loop?", "answer": "break"},
    {"question": "What keyword does nothing — it's just a placeholder?", "answer": "pass"},
    {"question": "What do you call the collection of items in square brackets?", "answer": "list"},
    {"question": "What do you call a key-value pair collection?", "answer": "dictionary"},
    {"question": "What is the term for a sequence of characters?", "answer": "string"},
    {"question": "What data type is used for whole numbers?", "answer": "int"},
    {"question": "What data type stores decimal numbers?", "answer": "float"},
    {"question": "What type stores True or False?", "answer": "boolean"},
    {"question": "What data structure uses () and is immutable?", "answer": "tuple"},
    {"question": "What structure uses {} and only keeps unique values?", "answer": "set"},
    {"question": "What built-in function shows output?", "answer": "print()"},
    {"question": "What built-in function gets input from a user?", "answer": "input()"},
    {"question": "What built-in function returns the type of a variable?", "answer": "type()"},
    {"question": "What function gets the length of a list or string?", "answer": "len()"},
    {"question": "What Python feature lets you reuse code?", "answer": "function"},
    {"question": "What do you call an error that stops your code?", "answer": "exception"},
    {"question": "What keyword starts error handling code?", "answer": "try"},
    {"question": "What keyword catches the error in error handling?", "answer": "except"},
    {"question": "What keyword is used to force an error?", "answer": "raise"},
    {"question": "What clause runs no matter what in try/except?", "answer": "finally"},
    {"question": "What symbol accesses a value in a dictionary by key?", "answer": "[]"},
    {"question": "What is used to loop over items with index?", "answer": "enumerate()"},
    {"question": "What function pairs elements from two lists?", "answer": "zip()"},
    {"question": "What is the Python keyword for defining a class?", "answer": "class"},
    {"question": "What special method runs when an object is created?", "answer": "__init__"},
    {"question": "What is the term for combining strings with f-strings?", "answer": "string interpolation"},
    {"question": "What is it called when a function calls itself?", "answer": "recursion"},
    {"question": "What do we call functions inside a class?", "answer": "methods"},
    {"question": "What symbol accesses methods from objects?", "answer": "."},
    {"question": "What do you call variables that belong to objects?", "answer": "attributes"},
    {"question": "What is used to convert other types into strings?", "answer": "str()"},
    {"question": "What Python feature lets you handle file reading?", "answer": "with statement"},
    {"question": "What method splits a string into a list?", "answer": "split()"},
    {"question": "What method removes characters from a string’s ends?", "answer": "strip()"},
    {"question": "What is the built-in function to create a list of numbers?", "answer": "range()"},
    {"question": "What operator is used to check membership?", "answer": "in"},
    {"question": "What is the result of 3 == '3' in Python?", "answer": "False"},
    {"question": "What keyword is used to create an anonymous function?", "answer": "lambda"},
    {"question": "What built-in function helps to loop with counters?", "answer": "enumerate()"},
    {"question": "What type of loop is best when you know how many times to iterate?", "answer": "for loop"},
    {"question": "What type of loop is best when you don't know how many times to iterate?", "answer": "while loop"},
    {"question": "What built-in function shows all available attributes and methods of an object?", "answer": "dir()"},
    {"question": "What function helps you inspect object details at runtime?", "answer": "help()"},
    {"question": "What keyword is used to inherit from a parent class?", "answer": "super"},
    {"question": "What do we call code that is easy to understand and modify?", "answer": "readable"},
    {"question": "What practice means writing code others can understand and reuse?", "answer": "clean code"},
    {"question": "What is a loop inside another loop called?", "answer": "nested loop"},
    {"question": "What do we call creating multiple variables at once from a tuple?", "answer": "unpacking"},
    {"question": "What Python function gets user input as a string?", "answer": "input()"},
    {"question": "What keyword checks if a value is not part of a collection?", "answer": "not in"},
    {"question": "What type of error occurs when a variable is not defined?", "answer": "NameError"},
    {"question": "What type of error occurs when dividing by zero?", "answer": "ZeroDivisionError"},
    {"question": "What function converts a number to binary string?", "answer": "bin()"},
    {"question": "What function converts a number to hexadecimal?", "answer": "hex()"},
    {"question": "What function converts a number to octal?", "answer": "oct()"},
    {"question": "What operator is used for integer division?", "answer": "//"},
    {"question": "What function reverses the order of elements in a list?", "answer": "reverse() or reversed()"},
    {"question": "What function returns the ASCII value of a character?", "answer": "ord()"},
    {"question": "What function returns character from ASCII value?", "answer": "chr()"},
    {"question": "What do you call a block of code that handles errors?", "answer": "try-except block"},
    {"question": "What string method checks if all characters are digits?", "answer": "isdigit()"},
    {"question": "What string method checks if all characters are alphabetic?", "answer": "isalpha()"},
    {"question": "What string method checks if all letters are lowercase?", "answer": "islower()"},
    {"question": "What string method checks if all letters are uppercase?", "answer": "isupper()"},
    {"question": "What method checks if a string starts with a specific value?", "answer": "startswith()"},
    {"question": "What method checks if a string ends with a specific value?", "answer": "endswith()"},
    {"question": "What string method checks if all characters are whitespace?", "answer": "isspace()"},
    {"question": "What data type holds multiple values and is mutable?", "answer": "list"},
    {"question": "What type is used for mapping keys to values?", "answer": "dictionary"},
    {"question": "What is the term for dividing a string or list into parts?", "answer": "slicing"},
    {"question": "What operator is used to assign a value to a variable?", "answer": "="},
    {"question": "What is the opposite of equality operator (==)?", "answer": "!="},
    {"question": "What Python feature allows storing functions as variables?", "answer": "first-class functions"},
    {"question": "What allows a function to accept any number of arguments?", "answer": "*args"},
    {"question": "What allows a function to accept any number of keyword arguments?", "answer": "**kwargs"},
    {"question": "What keyword is used to define an asynchronous function?", "answer": "async"},
    {"question": "What keyword is used to wait for an async call to finish?", "answer": "await"},
    {"question": "What are comments for in code?", "answer": "explanations or notes for developers"},
    {"question": "What is the name for a code mistake that causes a crash?", "answer": "bug"},
    {"question": "What do we call fixing a bug?", "answer": "debugging"},
    {"question": "What tool lets you run code line-by-line to debug?", "answer": "debugger"},
    {"question": "What symbol is used to write a comment in Python?", "answer": "#"},
    {"question": "What method do you use to copy a list?", "answer": "copy() or list()"},
    {"question": "What keyword refers to the instance inside a class method?", "answer": "self"},
    {"question": "What is the term for hiding internal details from users?", "answer": "encapsulation"},
    {"question": "What is the term for reusing code from a parent class?", "answer": "inheritance"},
]
