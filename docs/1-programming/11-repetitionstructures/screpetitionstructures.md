# Sentinel-controlled repetition.

When loop control is based on the value of what we are processing, sentinel-controlled repetition is used. 
Sentinel-controlled repetition is also called indefinite repetition because it is not known in advance how many times the loop will be executed. 
It is a repetition procedure for solving a problem by using a sentinel value (also called a signal value, a dummy value or a flag value) to indicate "end of process". 
The sentinel value itself need not be a part of the processed data.

One common example of using sentinel-controlled repetition is when we are processing data from a file and we do not know in advance when we would reach the end of the file. 

We can use both `for` and `while` loops, for __Sentinel__ controlled repetition, but the `while` loop is more common.

### Structured `WHILE` loop
The `while` loop repeats a block of instructions inside the loop while a condition remainsvtrue.

First a generic syntax

    while condition is true:
        execute a
        execute b
    ....

Notice our friends the colon `:` and the indentation again.

# Example `while` loops


```python
# sum numbers from 1 to n
howmany = int(input('Enter N'))
accumulator = 0.0
counter = 1
while counter <= howmany:
    accumulator = accumulator + float(counter)
    counter += 1
print( 'Sum from 1 to ',howmany, 'is %.3f' % accumulator  )
```

    Enter N 9


    Sum from 1 to  9 is 45.000



```python
# sum even numbers from 1 to n
howmany = int(input('Enter N'))
accumulator = 0.0
counter = 1
while counter <= howmany:
    if counter%2 == 0:
        accumulator = accumulator + float(counter)
    counter += 1
print( 'Sum of Evens 1 to ',howmany, 'is %.3f' % accumulator  )
```

    Enter N 9


    Sum of Evens 1 to  9 is 20.000



```python
howmany = int(input('Enter N'))
linetoprint=''
counter = 1
while counter <= howmany:
    linetoprint=linetoprint + '*'
    counter += 1
    print(linetoprint)
```

    Enter N 9


    *
    **
    ***
    ****
    *****
    ******
    *******
    ********
    *********


## Nested Repetition

Nested repetition is when a control structure is placed inside of the body or main part of another control structure.

#### `break` to exit out of a loop

Sometimes you may want to exit the loop when a certain condition different from the counting
condition is met. Perhaps you are looping through a list and want to exit when you find the
first element in the list that matches some criterion. The break keyword is useful for such
an operation.

For example run the following program:


```python
#
i = 0
j = 0
while i < 9:
    j += 2
    print ("i = ",i,"j = ",j)
    if j == 6:
        break   
    i = i + 1
```

    i =  0 j =  2
    i =  1 j =  4
    i =  2 j =  6



```python
i = 0
j = 0
while i <5 :
    j += 2
    print( "i = ",i,"j = ",j)
    if j == 7:
        break
    i = i + 1
```

    i =  0 j =  2
    i =  1 j =  4
    i =  2 j =  6
    i =  3 j =  8
    i =  4 j =  10


In the first case, the `while` loop only executes 3 times before the condition j == 6 is TRUE and the loop is exited. 
In the second case, j == 7 never happens so the loop completes all its anticipated traverses.

In both cases an `if` statement was used within a for loop. Such "mixed" control structures
are quite common (and pretty necessary). 
A `while` loop contained within a `for` loop, with several `if` statements would be very common and such a structure is called __nested control.__
There is typically an upper limit to nesting but the limit is pretty large - easily in the
hundreds. It depends on the language and the system architecture ; suffice to say it is not
a practical limit except possibly for general-domain AI applications.
<hr>

We can also do mundane activities and leverage loops, arithmetic, and format codes to make useful tables like



```python
import math # package that contains cosine
print("     Cosines     ")
print("   x   ","|"," cos(x) ")
print("--------|--------")
i = 0
while i < 157:
    x = float(i)*0.1
    print("%.3f" % x, "  |", " %.4f "  % math.cos(x)) # note the format code and the placeholder % and syntax 
    i = i + 1
```

         Cosines     
       x    |  cos(x) 
    --------|--------
    0.000   |  1.0000 
    0.100   |  0.9950 
    0.200   |  0.9801 
    0.300   |  0.9553 
    0.400   |  0.9211 
    0.500   |  0.8776 
    0.600   |  0.8253 
    0.700   |  0.7648 
    0.800   |  0.6967 
    0.900   |  0.6216 
    1.000   |  0.5403 
    1.100   |  0.4536 
    1.200   |  0.3624 
    1.300   |  0.2675 
    1.400   |  0.1700 
    1.500   |  0.0707 
    1.600   |  -0.0292 
    1.700   |  -0.1288 
    1.800   |  -0.2272 
    1.900   |  -0.3233 
    2.000   |  -0.4161 
    2.100   |  -0.5048 
    2.200   |  -0.5885 
    2.300   |  -0.6663 
    2.400   |  -0.7374 
    2.500   |  -0.8011 
    2.600   |  -0.8569 
    2.700   |  -0.9041 
    2.800   |  -0.9422 
    2.900   |  -0.9710 
    3.000   |  -0.9900 
    3.100   |  -0.9991 
    3.200   |  -0.9983 
    3.300   |  -0.9875 
    3.400   |  -0.9668 
    3.500   |  -0.9365 
    3.600   |  -0.8968 
    3.700   |  -0.8481 
    3.800   |  -0.7910 
    3.900   |  -0.7259 
    4.000   |  -0.6536 
    4.100   |  -0.5748 
    4.200   |  -0.4903 
    4.300   |  -0.4008 
    4.400   |  -0.3073 
    4.500   |  -0.2108 
    4.600   |  -0.1122 
    4.700   |  -0.0124 
    4.800   |  0.0875 
    4.900   |  0.1865 
    5.000   |  0.2837 
    5.100   |  0.3780 
    5.200   |  0.4685 
    5.300   |  0.5544 
    5.400   |  0.6347 
    5.500   |  0.7087 
    5.600   |  0.7756 
    5.700   |  0.8347 
    5.800   |  0.8855 
    5.900   |  0.9275 
    6.000   |  0.9602 
    6.100   |  0.9833 
    6.200   |  0.9965 
    6.300   |  0.9999 
    6.400   |  0.9932 
    6.500   |  0.9766 
    6.600   |  0.9502 
    6.700   |  0.9144 
    6.800   |  0.8694 
    6.900   |  0.8157 
    7.000   |  0.7539 
    7.100   |  0.6845 
    7.200   |  0.6084 
    7.300   |  0.5261 
    7.400   |  0.4385 
    7.500   |  0.3466 
    7.600   |  0.2513 
    7.700   |  0.1534 
    7.800   |  0.0540 
    7.900   |  -0.0460 
    8.000   |  -0.1455 
    8.100   |  -0.2435 
    8.200   |  -0.3392 
    8.300   |  -0.4314 
    8.400   |  -0.5193 
    8.500   |  -0.6020 
    8.600   |  -0.6787 
    8.700   |  -0.7486 
    8.800   |  -0.8111 
    8.900   |  -0.8654 
    9.000   |  -0.9111 
    9.100   |  -0.9477 
    9.200   |  -0.9748 
    9.300   |  -0.9922 
    9.400   |  -0.9997 
    9.500   |  -0.9972 
    9.600   |  -0.9847 
    9.700   |  -0.9624 
    9.800   |  -0.9304 
    9.900   |  -0.8892 
    10.000   |  -0.8391 
    10.100   |  -0.7806 
    10.200   |  -0.7143 
    10.300   |  -0.6408 
    10.400   |  -0.5610 
    10.500   |  -0.4755 
    10.600   |  -0.3853 
    10.700   |  -0.2913 
    10.800   |  -0.1943 
    10.900   |  -0.0954 
    11.000   |  0.0044 
    11.100   |  0.1042 
    11.200   |  0.2030 
    11.300   |  0.2997 
    11.400   |  0.3935 
    11.500   |  0.4833 
    11.600   |  0.5683 
    11.700   |  0.6476 
    11.800   |  0.7204 
    11.900   |  0.7861 
    12.000   |  0.8439 
    12.100   |  0.8932 
    12.200   |  0.9336 
    12.300   |  0.9647 
    12.400   |  0.9862 
    12.500   |  0.9978 
    12.600   |  0.9994 
    12.700   |  0.9911 
    12.800   |  0.9728 
    12.900   |  0.9449 
    13.000   |  0.9074 
    13.100   |  0.8610 
    13.200   |  0.8059 
    13.300   |  0.7427 
    13.400   |  0.6722 
    13.500   |  0.5949 
    13.600   |  0.5117 
    13.700   |  0.4234 
    13.800   |  0.3308 
    13.900   |  0.2349 
    14.000   |  0.1367 
    14.100   |  0.0372 
    14.200   |  -0.0628 
    14.300   |  -0.1621 
    14.400   |  -0.2598 
    14.500   |  -0.3549 
    14.600   |  -0.4465 
    14.700   |  -0.5336 
    14.800   |  -0.6154 
    14.900   |  -0.6910 
    15.000   |  -0.7597 
    15.100   |  -0.8208 
    15.200   |  -0.8737 
    15.300   |  -0.9179 
    15.400   |  -0.9530 
    15.500   |  -0.9785 
    15.600   |  -0.9942 


#### The `continue` statement
The continue instruction skips the block of code after it is executed for that iteration. 
It is
best illustrated by an example.


```python
i = 0
j = 0
while i < 5:
    j += 2
    print ("\n i = ", i , ", j = ", j) #here the \n is a newline command
    if j == 6:
        continue
    print(" this message will be skipped over if j = 6 ") # still within the loop, so the skip is implemented
    i = i + 1
```

    
     i =  0 , j =  2
     this message will be skipped over if j = 6 
    
     i =  1 , j =  4
     this message will be skipped over if j = 6 
    
     i =  2 , j =  6
    
     i =  2 , j =  8
     this message will be skipped over if j = 6 
    
     i =  3 , j =  10
     this message will be skipped over if j = 6 
    
     i =  4 , j =  12
     this message will be skipped over if j = 6 


#### The `try`, `except` structure

An important control structure (and a pretty cool one for error trapping) is the `try`, `except`
statement.

The statement controls how the program proceeds when an error occurs in an instruction.
The structure is really useful to trap likely errors (divide by zero, wrong kind of input) 
yet let the program keep running or at least issue a meaningful message to the user.

The syntax is:

    try:
    do something
    except:
    do something else if ``do something'' returns an error

Here is a really simple, but hugely important example:


```python
#MyErrorTrap.py
x = 12.
y = 12.
while y >= -12.: # sentinel controlled repetition
    try:         
        print ("x = ", x, "y = ", y, "x/y = ", x/y)
    except:
        print ("error divide by zero")
    y -= 1
```

    x =  12.0 y =  12.0 x/y =  1.0
    x =  12.0 y =  11.0 x/y =  1.0909090909090908
    x =  12.0 y =  10.0 x/y =  1.2
    x =  12.0 y =  9.0 x/y =  1.3333333333333333
    x =  12.0 y =  8.0 x/y =  1.5
    x =  12.0 y =  7.0 x/y =  1.7142857142857142
    x =  12.0 y =  6.0 x/y =  2.0
    x =  12.0 y =  5.0 x/y =  2.4
    x =  12.0 y =  4.0 x/y =  3.0
    x =  12.0 y =  3.0 x/y =  4.0
    x =  12.0 y =  2.0 x/y =  6.0
    x =  12.0 y =  1.0 x/y =  12.0
    error divide by zero
    x =  12.0 y =  -1.0 x/y =  -12.0
    x =  12.0 y =  -2.0 x/y =  -6.0
    x =  12.0 y =  -3.0 x/y =  -4.0
    x =  12.0 y =  -4.0 x/y =  -3.0
    x =  12.0 y =  -5.0 x/y =  -2.4
    x =  12.0 y =  -6.0 x/y =  -2.0
    x =  12.0 y =  -7.0 x/y =  -1.7142857142857142
    x =  12.0 y =  -8.0 x/y =  -1.5
    x =  12.0 y =  -9.0 x/y =  -1.3333333333333333
    x =  12.0 y =  -10.0 x/y =  -1.2
    x =  12.0 y =  -11.0 x/y =  -1.0909090909090908
    x =  12.0 y =  -12.0 x/y =  -1.0


So this silly code starts with x fixed at a value of 12, and y starting at 12 and decreasing by
1 until y equals -1. The code returns the ratio of x to y and at one point y is equal to zero
and the division would be undefined. By trapping the error the code can issue us a measure
and keep running.

Modify the script as shown below,Run, and see what happens


```python
#NoErrorTrap.py
x = 12.
y = 12.
while y >= -12.: # sentinel controlled repetition
    print ("x = ", x, "y = ", y, "x/y = ", x/y)
    y -= 1
```

    x =  12.0 y =  12.0 x/y =  1.0
    x =  12.0 y =  11.0 x/y =  1.0909090909090908
    x =  12.0 y =  10.0 x/y =  1.2
    x =  12.0 y =  9.0 x/y =  1.3333333333333333
    x =  12.0 y =  8.0 x/y =  1.5
    x =  12.0 y =  7.0 x/y =  1.7142857142857142
    x =  12.0 y =  6.0 x/y =  2.0
    x =  12.0 y =  5.0 x/y =  2.4
    x =  12.0 y =  4.0 x/y =  3.0
    x =  12.0 y =  3.0 x/y =  4.0
    x =  12.0 y =  2.0 x/y =  6.0
    x =  12.0 y =  1.0 x/y =  12.0



    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-5-82eeaceb9a12> in <module>
          3 y = 12.
          4 while y >= -12.: # sentinel controlled repetition
    ----> 5     print ("x = ", x, "y = ", y, "x/y = ", x/y)
          6     y -= 1


    ZeroDivisionError: float division by zero


## Readings

1. Learn Python in One Day and Learn It Well. Python for Beginners with Hands-on Project. (Learn Coding Fast with Hands-On Project Book -- Kindle Edition by LCF Publishing (Author), Jamie Chan [https://www.amazon.com/Python-2nd-Beginners-Hands-Project-ebook/dp/B071Z2Q6TQ/ref=sr_1_3?dchild=1&keywords=learn+python+in+a+day&qid=1611108340&sr=8-3](https://www.amazon.com/Python-2nd-Beginners-Hands-Project-ebook/dp/B071Z2Q6TQ/ref=sr_1_3?dchild=1&keywords=learn+python+in+a+day&qid=1611108340&sr=8-3)

2. Learn Python the Hard Way (Online Book) (https://learnpythonthehardway.org/book/)  Recommended for beginners who want a complete course in programming with Python.

3. How to Learn Python for Data Science, The Self-Starter Way (https://elitedatascience.com/learn-python-for-data-science) 

4. Flowcharts (QA/QC Perspective) [https://asq.org/quality-resources/flowchart](https://asq.org/quality-resources/flowchart)

5. Flowcharts - Wikipedia [https://en.wikipedia.org/wiki/Flowchart](https://en.wikipedia.org/wiki/Flowchart)

6. Psuedocode - Wikipedia [https://en.wikipedia.org/wiki/Pseudocode](https://en.wikipedia.org/wiki/Pseudocode)


```python

```
