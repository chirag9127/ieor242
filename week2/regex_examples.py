import re

STR = "Match either serialise or serialize"

def first_example():
    match = re.findall(r'seriali[sz]e', STR, re.M|re.I)

    if match:
        print "Matches are: ", match

first_example()

