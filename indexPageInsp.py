# Index page program for contents of a book.
# 22:46 26th july 2020
# dinesh pandikona aka tesla atoz
# basic format which can applied easily freqently.


# future option : Improve this program by making it more user-friendly and validation


# function and logic for printing.
def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth+rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))


# data which needs to be formatted.
picnicItems = {'sandwiches': 4, 'apples': 23, 'cups': 4, 'cookies': 322}

printPicnic(picnicItems, 20, 6)

# Use cases of this program
# 1. table  like formatted data.
