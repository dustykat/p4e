# User Interaction

Until this point we have explicitly specified input values for variables (and constants) in a script; now lets leverage intrinsic functions that lets us makes use of variables. We’ll revisit earlier examples, but this time we’ll make them interactive. Instead of just computing and sending output, we want read into variables values that may change from time to time. In order to do that, our script needs to be able to prompt us for information and display them on the screen.

This whole process is the essence of user interaction, and from the simple examples herein, one builds more complex scripts.

## The `input()` method

Consider and run the script below


```python
MyName=input('What is your name ?')
print(MyName)
```

    What is your name ? Jimmy Johns


    Jimmy Johns


The `input` method sent the string 'What is your name ?' to the screen, and then waited for the user to reply.  Upon reply, the input supplied was captured and then placed into the variable named `MyName`. 

Then the next statement, used the `print()` method to print the contents of `MyName` back to the screen.  From this simple structure we can create quite useful input and output. 

As a matter of good practice, we should explicitly type the input variable, as shown below which takes the input stream and converts it into a string.


```python
MyName=str(input('What is your name ?'))
print(MyName)
```

    What is your name ? Taco Bell


    Taco Bell


Below we prompt for a second input, in this case the user's age, which will be put into an integer.  As a sdie note, we are not error checking, so if an input stream that cannot be made into an integer is suppplied we will get an exception warning or an error message.


```python
MyAge=int(input('How old are you ? '))
print(MyAge)
```

    How old are you ?  66


    66


## The `print()` method

The `print()` function is used to display information to users. 
It accepts zero or more expressions as parameters, separated by commas. 

Consider the statement below, how many parameters are in the parameter list?


```python
print ("Hello World, my name is", MyName, "and I am", MyAge, "years old.")
```

    Hello World, my name is Taco Bell and I am 66 years old.


There are five parameters;

1. "Hello World, my name is"
2. MyName
3. "and I am"
4. MyAge
5. "years old"

Three of the parameters are string literals and are enclosed in quote marks, two are variables that are rendered as strings.

## The `%` operator
Strings can be formatted using the `%` operator. This gives you greater control over how you want your string to be displayed and stored. The syntax for using the `%` operator is “string to be formatted” %(values or variables to be inserted into string, separated by commas)

An example using the string constructor (`%`) form using a placeholder in the print function call is:


```python
print ("Hello World, my name is %s and I am %s years old." %(MyName,MyAge))
```

    Hello World, my name is Taco Bell and I am 66 years old.


Notice the syntax above.  The contents of the two variables are placed in the locations within the string indicated by the `%s` symbol, the tuple (MyName,MyAge) is parsed using this placeholder and converted into a string by the trailing `s` in the `%s` indicator.

See what happens if we change the second `%s` into `%f` and run the script:


```python
print ("Hello World, my name is %s and I am %f years old." %(MyName,MyAge))
```

    Hello World, my name is Taco Bell and I am 66.000000 years old.


The change to `%f` turns the rendered tuple value into a float.  Using these structures gives us a lot of output flexibility.

## The `format()` method

Similar to the `%`operator structure there is a `format()` method.  Using the same example, the `%s` symbol is replaced by a pair of curly brackets `{}` playing the same placeholder role, and the `format` keyword precedes the tuple as


```python
print ("Hello World, my name is {} and I am {} years old.".format(MyName,MyAge))
```

    Hello World, my name is Taco Bell and I am 66 years old.


Observe the keyword `format` is joined to the string with a dot notation, because `format` is a formal method associated with all strings, and it attached when the string literal is created.

In this example the arguments to the method are the two variables, but other arguments and decorators are possible allowing for elaborate outputs.

## Triple quotes

If you need to display a long message, you can use the triple-quote symbol (‘’’ or “””) to span the  message over multiple lines. For instance:


```python
print ('''Hello World, my name is {} and I am a resturant
that is over {} years old. We serve sodium chloride infused 
lipids in a variety of shapes'''.format(MyName,MyAge))
```

    Hello World, my name is Taco Bell and I am a resturant
    that is over 66 years old. We serve sodium chloride infused 
    lipids in a variety of shapes


Creating an array that contains signed integer numbers

## Escape Characters

Sometimes we may need to print some special “unprintable” characters such as a tab or a newline. 
In this case, you need to use the `\` (backslash) character to escape characters that otherwise have a different meaning.  For instance to print a tab, we type the backslash character before the letter t, like this `\t` using our same example we have:


```python
print ("Hello\t World, my name is {} and I am {} years old.".format(MyName,MyAge))
```

    Hello	 World, my name is Taco Bell and I am 66 years old.


Here are a few more examples:


```python
#newline after World
print ("Hello World\n, my name is {} and I am {} years old.".format(MyName,MyAge)) 
```

    Hello World
    , my name is Taco Bell and I am 66 years old.



```python
# backslash after World
print ("Hello World\\, my name is {} and I am {} years old.".format(MyName,MyAge)) 
```

    Hello World\, my name is Taco Bell and I am 66 years old.



```python
# embedded quotes in the string literal
print ("I am 5'9\" tall") 
```

    I am 5'9" tall


If you do not want characters preceded by the `\` character to be interpreted as special characters, you can use raw strings by adding an `r` before the first quote. 
For instance, if you do not want `\t` to be interpreted as a tab in the string literal "Hello\tWorld", you would type 


```python
print(r"Hello\tWorld")
```

    Hello\tWorld


## Readings

1. Learn Python in One Day and Learn It Well. Python for Beginners with Hands-on Project. (Learn Coding Fast with Hands-On Project Book -- Kindle Edition by LCF Publishing (Author), Jamie Chan [https://www.amazon.com/Python-2nd-Beginners-Hands-Project-ebook/dp/B071Z2Q6TQ/ref=sr_1_3?dchild=1&keywords=learn+python+in+a+day&qid=1611108340&sr=8-3](https://www.amazon.com/Python-2nd-Beginners-Hands-Project-ebook/dp/B071Z2Q6TQ/ref=sr_1_3?dchild=1&keywords=learn+python+in+a+day&qid=1611108340&sr=8-3)

2. Learn Python the Hard Way (Online Book) (https://learnpythonthehardway.org/book/)  Recommended for beginners who want a complete course in programming with Python.

3. How to Learn Python for Data Science, The Self-Starter Way (https://elitedatascience.com/learn-python-for-data-science) 

4. String Literals [https://bic-berkeley.github.io/psych-214-fall-2016/string_literals.html](https://bic-berkeley.github.io/psych-214-fall-2016/string_literals.html)

5. Tutorial on `input()` and `print()` functions [https://www.programiz.com/python-programming/input-output-import](https://www.programiz.com/python-programming/input-output-import)


```python

```
