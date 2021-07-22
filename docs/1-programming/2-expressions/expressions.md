# expressions

- fundamental operators
- arithmetic expressions
- simple output: print()

Download this page as a jupyter notebook from [http://54.243.252.9/p4e/1-programming/2-expressions/expressions.ipynb](http://54.243.252.9/p4e/1-programming/2-expressions/expressions.ipynb)

Consider the relativistic equation relating energy, mass, and the speed of light 

$$ e = m \cdot c^2 $$

In this equation the symbols $e$,$m$,$c$,$=$,$\cdot$, and the structure is parsed from left to right. The entire equation is an statement that instructs: place into the container named $e$ the result of the product of the contents of containers $m$ and $c^2$.  

In the above statement the symbols $e$,$m$,$c$ are names for things that can have values -- we will call these containers (or variables, or named constants).  The symbols $=$,$\cdot$, and $~^2$ are instructions for various arithmetic operations -- we will call these operators.  

The part of the statement to the right of the $=$ symbol is an arithmetic expression.

When we attempt to write and execute python scripts - we will make various mistakes; these will generate warnings and errors, which we will repair to make a working program.

Consider our statement with the container names spelled out:




```python
# Example 
Energy = Mass * SpeedOfLight**2 
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-4-1c1f1fa5363a> in <module>
          1 #clear all variables# Example
    ----> 2 Energy = Mass * SpeedOfLight**2
    

    NameError: name 'Mass' is not defined


Notice how the interpreter tells us that Mass is undefined - so a simple fix is to define it and try again


```python
# Example 
Mass = 1000000
Energy = Mass * SpeedOfLight**2 
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-5-a4a52966e6df> in <module>
          1 # Example
          2 Mass = 1000000
    ----> 3 Energy = Mass * SpeedOfLight**2
    

    NameError: name 'SpeedOfLight' is not defined


Notice how the interpreter now tells us that SpeedOfLight is undefined - so a simple fix is to define it and try again


```python
# Example 
Mass = 1000000  #kilograms
SpeedOfLight = 299792458  #meters per second
Energy = Mass * SpeedOfLight**2 
```

Now the script ran without any reported errors, but we have not instructed the program on how to produce output.  To keep the example simple we will just add a generic print statement.


```python
# Example 
Mass = 1000000  #kilograms
SpeedOfLight = 299792458  #meters per second
Energy = Mass * SpeedOfLight**2 
print("Energy is:", Energy, "Newton meters")
```

    Energy is: 89875517873681764000000 Newton meters


## Fundamental Operators

### Assignment Operator

The `=` sign used in a statement is called an assignment operator (or assignment sign). 
The symbol means that the expression to the right of the symbol is to be evaluated and the result placed into the variable on the left side of the symbol.  The "operation" is assignment, the "=" symbol is the operator name.

Consider the script below


```python
x = 5  # assign constant 5 into a container named x 
y = 10 # assign constant 10 into a containernamed x
print (x,y) # print the contents of containers x and y
x=y # put contents of y into x
print (x,y) # print the contents of containers x and y
```

    5 10
    10 10


### Arithmetic Operators

In addition to assignment we can also perform arithmetic operations on containers. The
fundamental arithmetic operators are:

| Symbol | Meaning | Example |
|:---|:---|:---|
| = |Assignment| x=3 Assigns value of 3 to x.|
| + |Addition| x+y Adds values in x and y.|
| - |Subtraction| x-y Subtracts values in y from x.|
| * |Multiplication| x*y Multiplies values in x and y.|
| / |Division| x/y Divides value in x by value in y.|
| // |Floor division| x//y Divide x by y, truncate result to whole number.|
| % |Modulus| x%y Returns remainder when x is divided by y.|
| ** |Exponentation| x ** y Raises value in x by value in y. ( e.g. x ** y)|
| += |Additive assignment| x+=2 Equivalent to x = x+2.|
| -= |Subtractive assignment| x-=2 Equivalent to x = x-2.|
| *= |Multiplicative assignment| x\*=3 Equivalent to x = x\*3.|
| /= |Divide assignment| x/3 Equivalent to x = x/3.|

Run the script in the next cell for some illustrative results

## arithmetic expressions


```python
# Uniary Arithmetic Operators
x = 10
y = 5
print(x, y)
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print((x+1)//y)
print((x+1)%y)
print(x**y)
```

    10 5
    15
    5
    50
    2.0
    2
    1
    100000



```python
# Arithmetic assignment operators
x = 1
x += 2
print(type(x),x)
x = 1
x -= 2
print(type(x),x)
x = 1
x *=3
print(type(x),x)
x = 10
x /= 2
print(type(x),x)  # Interesting what division does to variable type
```

    <class 'int'> 3
    <class 'int'> -1
    <class 'int'> 3
    <class 'float'> 5.0


## simple output: print()

## Readings

Learn Python in One Day and Learn It Well. Python for Beginners with Hands-on Project. (Learn Coding Fast with Hands-On Project Book -- Kindle Edition by LCF Publishing (Author), Jamie Chan [https://www.amazon.com/Python-2nd-Beginners-Hands-Project-ebook/dp/B071Z2Q6TQ/ref=sr_1_3?dchild=1&keywords=learn+python+in+a+day&qid=1611108340&sr=8-3](https://www.amazon.com/Python-2nd-Beginners-Hands-Project-ebook/dp/B071Z2Q6TQ/ref=sr_1_3?dchild=1&keywords=learn+python+in+a+day&qid=1611108340&sr=8-3)




```python

```
