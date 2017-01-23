"""
Lesson 3.5: Defensive Mapper Code
Date: 2017-01-23

Example log line:
    2012-01-01  12:01   San Jose    Music   12.99   Amex
    2012-01-02  There was an error connecting to database. Please try again
"""

import sys

def mapper():
    for line in sys.stdin:
        data = line.strip().split('\n')

        if len(data) == 6:
            date, time, store, item, cost, payment = date
            print("{}\t{}".format(store, cost))


if __name__ == '__main__':
    # test
    mapper()
