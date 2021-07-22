# Sequential Structures

Sequential processing are steps performed in sequence, one after another.  A spreadsheet computation from top-to-bottom is a sequential process.

**Reliability Example**
Suppose we wish to estimate the reliability of a system comprised of many indetical parts iused in multiple places in a design, for instance rivets on an airplane wing. Using a Bernoulli model (which you will see in your statistics class) we can estimate the collective reliability of the system (all the parts work as desired).  The reliability is expressed as the fraction of time that no parts have failed, if the fraction is small we would want to either improve part reliability, or ensure redundancy so the system can function with broken parts.

Let $p$ be the probability a single component is good and $N$ be the total number of components in the system that work together in a "series" context.  The reliability, or the percentage of time that none of the components have failed is given by the Bernoulli equation:

$$\% = (\frac{p}{100.0})^N \cdot 100.0 $$

Suppose we want a script to read in a component probability and count, and estimate system reliability -- we can apply our problem solving protocol and JupyterLab to do so, and the task will be mostly sequential

**Step 1 Problem Statement** Estimate the reliability of a component in an instrument relative to a group of components using a Bernoulli approximation.

**Step 2 Input/Output Decomposition** Inputs are the reliability of a single component and the number of components working together in a system, output is estimate of system reliability, governing principle is the Bernoulli equation above.

**Step 3 By-Hand Example**
SUppose the system is a small FPGA with 20 transistors, each with reliability of 96-percent. The entire array reliability is

$$\text{percentage} = (\frac{96.0}{100.0})^{20} \cdot 100.0 = 44.2\%$$

**Step 4 Algorithm Development**
Decompose the computation problem as:

1. Read reliability of a single component
2. Read how many components
3. Compute reliability  by bernoulli model
4. Report result

**Step 5 Scripting**
Written as a sequence we can have


```python
component = float(input('Component Reliability (percentage-numeric)?'))
howmany = int(input('Number of Components (integer-numeric)?'))
reliability = 100.0*(component/100.0)**howmany
print('Component Reliability: ',round(component,1))
print('Number of Components : ',howmany)
print('System Relability is : ',round(reliability,1),'%')
```

    Component Reliability (percentage-numeric)? 96
    Number of Components (integer-numeric)? 20


    Component Reliability:  96.0
    Number of Components :  20
    System Relability is :  44.2 %


**Step 6 Refinement**
We have tested the script with the by-hand example, no refinement really needed here, but lets apply to new conditions


```python
component = float(input('Component Reliability (percentage-numeric)?'))
howmany = int(input('Number of Components (integer-numeric)?'))
reliability = 100.0*(component/100.0)**howmany
print('Component Reliability: ',round(component,1))
print('Number of Components : ',howmany)
print('System Relability is : ',round(reliability,1),'%')
```

    Component Reliability (percentage-numeric)? 99
    Number of Components (integer-numeric)? 20


    Component Reliability:  99.0
    Number of Components :  20
    System Relability is :  81.8 %


### References

1. Computational and Inferential Thinking Ani Adhikari and John DeNero, Computational and Inferential Thinking, The Foundations of Data Science, Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND) Chapters 3-6 https://www.inferentialthinking.com/chapters/03/programming-in-python.html

2. Learn Python the Hard Way (Online Book) (https://learnpythonthehardway.org/book/)  Recommended for beginners who want a complete course in programming with Python.

3. LearnPython.org (Interactive Tutorial) (https://www.learnpython.org/)  Short, interactive tutorial for those who just need a quick way to pick up Python syntax.

4. Brian Christian and Tom Griffiths (2016) ALGORITHMS TO LIVE BY: The Computer Science of Human Decisions Henry Holt and Co. (https://www.amazon.com/Algorithms-Live-Computer-Science-Decisions/dp/1627790365)

4. Theodore G. Cleveland, Farhang Forghanparast, Dinesh Sundaravadivelu Devarajan, Turgut Batuhan Baturalp (Batu), Tanja Karp, Long Nguyen, and Mona Rizvi. (2021) Computational Thinking and Data Science: A WebBook to Accompany ENGR 1330 at TTU, Whitacre College of Engineering, DOI (pending)[https://3.137.111.182/engr-1330-webroot/engr-1330-webbook/ctds-psuedocourse/site/](https://3.137.111.182/engr-1330-webroot/engr-1330-webbook/ctds-psuedocourse/site/)


## Readings

1. Learn Python in One Day and Learn It Well. Python for Beginners with Hands-on Project. (Learn Coding Fast with Hands-On Project Book -- Kindle Edition by LCF Publishing (Author), Jamie Chan [https://www.amazon.com/Python-2nd-Beginners-Hands-Project-ebook/dp/B071Z2Q6TQ/ref=sr_1_3?dchild=1&keywords=learn+python+in+a+day&qid=1611108340&sr=8-3](https://www.amazon.com/Python-2nd-Beginners-Hands-Project-ebook/dp/B071Z2Q6TQ/ref=sr_1_3?dchild=1&keywords=learn+python+in+a+day&qid=1611108340&sr=8-3)

2. Learn Python the Hard Way (Online Book) (https://learnpythonthehardway.org/book/)  Recommended for beginners who want a complete course in programming with Python.

3. How to Learn Python for Data Science, The Self-Starter Way (https://elitedatascience.com/learn-python-for-data-science) 

4. Flowcharts (QA/QC Perspective) [https://asq.org/quality-resources/flowchart](https://asq.org/quality-resources/flowchart)

5. Flowcharts - Wikipedia [https://en.wikipedia.org/wiki/Flowchart](https://en.wikipedia.org/wiki/Flowchart)

6. Psuedocode - Wikipedia [https://en.wikipedia.org/wiki/Pseudocode](https://en.wikipedia.org/wiki/Pseudocode)


```python

```
