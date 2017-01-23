"""
    Reducer Code
    Date: 2017-01-23

    Example output of mapper:
        <key>   <data>
        Miami   12.34
        Miami   99.07
        Miami   3.14
        NYC     99.77
        NYC     88.99
"""

import sys

def reducer():

    salesTotal = 0
    oldKey = None

    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 2:
            continue

        thisKey, thisSale = data

        if oldKey and oldKey != thisKey:
            print("{}\t{}".format(oldKey, salesTotal))

            salesTotal = 0

        oldKey = thisKey
        salesTotal += float(thisSale)

    # Process the last key ! IMPORTANT !
    if oldKey != None:
        print("{}\t{}".format(oldKey, salesTotal))


if __name__ == '__main__':
    # test
    reducer()

