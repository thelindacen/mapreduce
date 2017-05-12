#!/usr/bin/env python

# Import the sys library 
# for writing and reading the standard input and output

import sys

# Example Input data (minipurchase.txt)
# Input is tabulator (\t) separated
# New Line (\n) indicates a new record.
# Input will be piped into the standard input (e.g. with cat on the command line)
# Fields (Date, Time, Item, Category, Sales, Payment):
# 2012-12-31	16:26	Anaheim	Men's Clothing		205.96	Visa
# 2012-12-31	16:29	Irvine	Women's Clothing	22.47	Cash
# 2012-12-31	16:30	Laredo	Women's Clothing	444.19	Cash

# The mapper transforms the input into key-value pairs.
#key: category (Exercise 1)
#value: sales
# The values are not yet aggregated! (This is done by the reducer)

# For each new line in the standard input (stdin) 

for line in sys.stdin:

    # split the line at the tabulator ("\t")
    # strip removes whitespaces and new lines at the beginning and end of the line
    # the result is a tuple with 6 elements

    data = line.strip().split("\t")
    	
    # store the 6 elements of the tuple in seperate variables
    date, time, item, category, sales, payment = data

    #Exercise 3: Error is raised when there are not six elements in the tulpe           
    if len(data) != 6:                                                                                                                                                  print("ERROR: not six elements in a tulpe")
        raise ValueError ('Error')
    # Write the key-value combination to standard output (stdout)
    # Key is the category, value is the sales     
    # With a tab (\t) between key and value
    # New line \n means new record

    #Exercise 4: Just map these three categories: computers, cameras and video games
    if category in [ "Computers", "Cameras","Video Games"]:    
    	sys.stdout.write("{0}\t{1}\n".format(category, sales))
