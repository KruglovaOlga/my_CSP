import pathlib
from typing import List
import re
from math import ceil

#The code reads a file of numbers and returns a list of (count, number) pairs.
 # starts by creating an input_text variable with the path to the file as its value.
 #Then it reads each line in the text file into a list of numbers using re.findall().

def get_data(infile:str)->List[float]:
    """ Reads a file of numbers and returns a list of (count, number) pairs."""
    _p = pathlib.Path(infile)
    #input_text = _p.read_text()
    numbers = [ceil(float(n)) for n in re.findall(r'[0-9.]+', _p.read_text())]
    #It then creates two lists: one for counting how many times each number appears in the list,
    # and another for keeping track of which numbers are not 0 or greater than 9.
    #The first line is "1 2 3 4 5 6 7 8 9".
    quan = []
    nr = []
    for n in numbers:
        # So 1 will be counted twice because there are two occurrences of 1 in that string,
        # while 2 will be counted once because there is only one occurrence of 2 in that string.
        if n not in nr and n != 0:
            quan.append(numbers.count(n))
            nr.append(n)
    return list(zip(quan,nr)) #The code would read the input file and return a list of (count, number) pairs.
