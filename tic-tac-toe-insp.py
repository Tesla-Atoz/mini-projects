# A basic inspiration program design for tic-tac-toe game.add()
# 22:28 26th july 2020
# dinesh pandikona aka tesla atoz
# it is simple yet unfinished tic-tac-toe game without validation

# future option : Improve this program by making it user-friendly and other features.add()


# Here, I am storing the position. (dicitonary datastruture.)
theBoard = {
    'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
    'low-L': ' ', 'low-M': ' ', 'low-R': ' ',

}

# function to print the board with postions.


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


turn = 'X'

# logic to fill positions upon every move.
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'o'
    else:
        turn = 'X'


# Use cases of this program

# 1. To create board games with cool improvements.add()

# like fully high quality game.
