# program to read a numeric file, and compute mean of the contents
# Prototype functions:

def readAfile(filename,inputlist): # arguments are WhatToRead,WhereToPut 
    externalfile = open(filename,'r') # create connection to file, set to read (r), file must exist
    how_many_lines = 0
    for line in externalfile: # parse each line, append to xlist
        inputlist.append(line)
        how_many_lines += 1
    externalfile.close() # close the file connection
    return()

def average(inputlist):
# inputlist should be a list of values
    howlong = len(inputlist) # len is a built-in function that returns how many items in a list
    accumulator = 0 # a variable to accumulate the sum
    for i in range(howlong):
        accumulator = accumulator + float(inputlist[i])
    result = (accumulator/howlong)
    return(result)

xlist=[] # list (null) is a type of data structure
readAfile("data.txt",xlist) # read the file , put into the list
print("arithmetic mean = ",round(average(xlist),2)) # compute and print the mean