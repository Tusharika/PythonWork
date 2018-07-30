'''
there is a battleship hidden in a grid of 5x5 and user is asked to guess it's location.
'''

# creating 5x5 grid

board = []

for items in range(7):
    board.append(["O"] * 7)
    # return board


# print (board)

def print_board(board_in):
    for row in board_in:
        # custom print list
        print(" ".join(row))


print(print_board(board))


# assigning random location to ship

def random_row(board_in):
    from random import randint
    random_row_index = randint(0, len(board_in))
    return random_row_index


# print (random_row(board))

def random_col(board_in):
    from random import randint
    random_column_index = randint(0, len(board_in))
    return random_column_index


# print (random_col(board))

# assign variables for row and column locations of the hidden ship

ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row)
print(ship_col)

# user's guess

for turn in range(4):

    print('turn = ' + str(turn + 1))

    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))



    if (ship_row == guess_row) and (ship_col == guess_col):
        print("Congratulations! You sank my battleship!")
        break


    elif guess_row not in range(len(board)) or guess_col not in range(len(board)):
        print("Oops, that's not even in the ocean.")

    # X = board[guess_row][guess_col]

    elif board[guess_row][guess_col] == 'X':
        print(" You guessed that one already.")

    else:
        print("You missed my battleship!")
        board[guess_row][guess_col] = 'X'

    print(print_board(board))

print(print_board(board))


