# Data Types
In the computer data are all binary digits (actually 0 and +5 volts). 
At a higher level of **abstraction** data are typed into integers, real, or alphanumeric representation. 
The type affects the kind of arithmetic operations that are allowed (as well as the kind of arithmetic - integer versus real arithmetic; lexicographical ordering of alphanumeric , etc.)
In scientific programming, a common (and really difficult to detect) source of slight inaccuracies (that tend to snowball as the program runs) is mixed mode arithmetic required because two numeric values are of different types (integer and real).

Learn more from the textbook https://www.inferentialthinking.com/chapters/04/Data_Types.html


## Integer
Integers are numbers without any fractional portion (nothing after the decimal point { which
is not used in integers). Numbers like -3, -2, -1, 0, 1, 2, 200 are integers. A number like 1.1
is not an integer, and 1.0 is also not an integer (the presence of the decimal point makes the
number a real).

To declare an integer in Python, just assign the value to a container name as an integer.   


```python
MyPhoneNumber = 14158576309
type(MyPhoneNumber) # intrinsic type function to return data type in container
```




    int



## Real (Float)
A real or float is a number that has (or can have) a fractional portion - the number has
decimal parts. The numbers 3.14159, -0.001, 11.11, 1., are all floats. 
The last one is especially tricky, if you don't notice the decimal point you might think it is an integer but the
inclusion of the decimal point in Python tells the program that the value is to be treated as a 
float.
To declare a float in Python, just assign a number with the radix (decimal point) to a container name.


```python
MyMassInKilos = 74.8427
type(MyMassInKilos) # intrinsic type function to return data type in container
```




    float



## String(Alphanumeric)
A string is a data type that is treated as text elements. The usual letters are strings, but
numbers can be included. The numbers in a string are simply characters and cannot be
directly used in arithmetic. 
There are some kinds of arithmetic that can be performed on strings but generally we process string variables to capture the text nature of their contents. 
To declare a string in Python, just assign the variable name to a string value - the trick is the value is enclosed in quotes. 
The quotes are delimiters that tell the program that the characters between the quotes are characters and are to be treated as literal representation.


```python
MyName = 'Theodore'
MyCatName = "Dusty"
DustyMassInKilos = "7.48427"
print("MyName is type :",type(MyName))
print("MyCatName is type :",type(MyCatName))
print("DustyMassInKilos is type :",type(DustyMassInKilos))
```

    MyName is type : <class 'str'>
    MyCatName is type : <class 'str'>
    DustyMassInKilos is type : <class 'str'>


For example MyName, MyCatName, and DustyMassInKilos, are all string variables. 
The last assignment is made into a string by enclosing the number in the quotes. 
String variables can be combined using an operation called concatenation. 
The symbol for concatenation is the plus symbol `+`.

Strings can also be converted to all upper case using the `upper()` function. The syntax for
the `upper()` function is `'string to be upper case'.upper()`. 
Notice the "dot" in the syntax. 
The operation passes everything to the left of the dot to the function which then
operates on that content and returns the result all upper case (or an error if the input stream
is not a string).


```python
# Variable Types Example
MyPhoneNumber = 14158576309
MyMassInKilos = 74.8427
MyName = 'Theodore'
MyCatName = "Dusty"
DustyMassInKilos = "7.48427"
print("All about me")
print("Name: ",MyName, " Mass :",MyMassInKilos,"Kg" )
print('Phone : ',MyPhoneNumber)
print('My cat\'s name :', MyCatName)  # the \ escape character is used to get the ' into the literal
print("All about concatenation!")
print("A Silly String : ",MyCatName+MyName+DustyMassInKilos)
print("A SILLY STRING :  ", (MyCatName+MyName+DustyMassInKilos).upper())
```

    All about me
    Name:  Theodore  Mass : 74.8427 Kg
    Phone :  14158576309
    My cat's name : Dusty
    All about concatenation!
    A Silly String :  DustyTheodore7.48427
    A SILLY STRING :   DUSTYTHEODORE7.48427


Strings can be formatted using the `%` operator or the `format()` function. The concepts will
be introduced later on as needed, you can Google search for examples of
how to do such formatting.

## Changing Types
A data type can be changed. 
This activity is called type casting. 
Three functions allow
type casting: `int()`, `float()`, and `str()`. 
The function names indicate the result of using
the function, hence `int()` returns an integer, `float()` returns a 
oat, and `str()` returns a
string.

There is also the useful function `type()` which returns the type of variable.

The easiest way to understand is to see an example. 


```python
# Type Casting Examples
MyInteger = 234
MyFloat = 876.543
MyString = 'What is your name?'
print(MyInteger,MyFloat,MyString)
print('Integer as float',float(MyInteger))
print('Float as integer',int(MyFloat))
print('Integer as string',str(MyInteger))
print('Integer as hexadecimal',hex(MyInteger))
print('Integer Type',type((MyInteger)))  # insert the hex conversion and see what happens!
```

    234 876.543 What is your name?
    Integer as float 234.0
    Float as integer 876
    Integer as string 234
    Integer as hexadecimal 0xea
    Integer Type <class 'int'>


## Other Types

Core python also has a `complex()` numeric type.

There are useful methods that can convert to different representations for numeric types for example


```python
myint = 1234
hex(myint)
```




    '0x4d2'




```python
bin(myint)
```




    '0b10011010010'



## Readings

1. Learn Python in One Day and Learn It Well. Python for Beginners with Hands-on Project. (Learn Coding Fast with Hands-On Project Book -- Kindle Edition by LCF Publishing (Author), Jamie Chan [https://www.amazon.com/Python-2nd-Beginners-Hands-Project-ebook/dp/B071Z2Q6TQ/ref=sr_1_3?dchild=1&keywords=learn+python+in+a+day&qid=1611108340&sr=8-3](https://www.amazon.com/Python-2nd-Beginners-Hands-Project-ebook/dp/B071Z2Q6TQ/ref=sr_1_3?dchild=1&keywords=learn+python+in+a+day&qid=1611108340&sr=8-3)

2. Learn Python the Hard Way (Online Book) (https://learnpythonthehardway.org/book/)  Recommended for beginners who want a complete course in programming with Python.

3. LearnPython.org (Interactive Tutorial) (https://www.learnpython.org/)  Short, interactive tutorial for those who just need a quick way to pick up Python syntax.

4. How to Think Like a Computer Scientist (Interactive Book) (https://runestone.academy/runestone/books/published/thinkcspy/index.html) Interactive "CS 101" course taught in Python that really focuses on the art of problem solving. 

5. How to Learn Python for Data Science, The Self-Starter Way (https://elitedatascience.com/learn-python-for-data-science) 



```python

```
