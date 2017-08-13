#tic tac toe
import random
board = [0, 1, 2,
         3, 4, 5,
         6, 7, 8]


def format_board():
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])


def get_user_input():
    taken = True
    while taken:
        user_input = input("\nEnter a spot >>> ")
        spot = int(user_input)
        if board[spot] != 'x' and board[spot] != 'o':
            board[spot] = 'x'
            taken = False
        else:
            print("That spot is taken")
            taken = True


def get_random_input():
    taken = True
    while taken:
        random.seed()  # #gives a random generator
        opponent = random.randint(0,8)
        if board[opponent] != 'o' and board[opponent] != 'x':
            board[opponent] = "o"
            taken = False
        else:
            taken = True


def check_line(char, spot1, spot2, spot3):  # #check if a given line has all he same chars
    if board[spot1] == char and board[spot2] == char and board[spot3] == char:
        return True


def check_all(char):
    # check horizontal
    if check_line(char, 0, 1, 2):
        return True
    if check_line(char, 3, 4, 5):
        return True
    if check_line(char, 6, 7, 8):
        return True

    # check vertical
    if check_line(char, 0, 3, 6):
        return True
    if check_line(char, 1, 4, 7):
        return True
    if check_line(char, 2, 5, 8):
        return True
    # check diagonal
    if check_line(char, 0, 4, 8):
        return True
    if check_line(char, 2, 4, 6):
        return True


if __name__ == "__main__":
    counter = 0
    while True:
        format_board()
        get_user_input()
        counter += 1
        if check_all('x') is True:  # #if the user has won
            print("You have won the game!")
            format_board()
            break
        elif counter >= 9:
            print("The game is TIED")
            format_board()
            break
        else:
            get_random_input()
            counter += 1
            if check_all('o') is True:
                print("Your opponent has won :(")
                format_board()
                break
