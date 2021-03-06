# -*- coding: utf-8 -*-
"""PythonFinalProject2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EdWOwFpc1mFQFv_xJII26Q3T6NKfksoV
"""

# 2
# Make Tic Tac Toe Game with the help of python

print("-------Project 2-------")

print("\n\n\n                                                                TIC-TAC-TOE GAME\n\n")

game = {
    '1': ' ', '2': ' ', '3': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '7': ' ', '8': ' ', '9': ' '
}

gamer = 1          # ----- to initialise first player
moves = 0     # ---- to count the number of moves
end_check = 0
Player1=input("Enter player one name : ")
Player2=input("Enter player second name : ")

def check():
    # checking the moves of player one
    # for horizontal(start)
    if game['1'] == 'X' and game['2'] == 'X' and game['3'] == 'X':
        print('Congratulation ..')
        print('Player ' + Player1 + ' Won!!')

        return 1
    if game['4'] == 'X' and game['5'] == 'X' and game['6'] == 'X':
        print('Congratulation ..')
        print('Player ' + Player1 + ' Won!!')

        return 1
    if game['7'] == 'X' and game['8'] == 'X' and game['9'] == 'X':
        print('Congratulation ..')
        print('Player '+ Player1 +' Won!!')

        return 1
    # for horizontal(end)
    # for diagonal(start)
    if game['1'] == 'X' and game['5'] == 'X' and game['9'] == 'X':
        print('Congratulation ..')
        print('Player ' + Player1 + ' Won!!')

        return 1
    # for diagonal(end)
    # for vertical(start)
    if game['1'] == 'X' and game['4'] == 'X' and game['7'] == 'X':
        print('Congratulation ..')
        print('Player ' + Player1 + ' Won!!')

        return 1
    if game['2'] == 'X' and game['5'] == 'X' and game['8'] == 'X':
        print('Congratulation ..')
        print('Player ' + Player1 + ' Won!!')

        return 1
    if game['3'] == 'X' and game['6'] == 'X' and game['9'] == 'X':
        print('Congratulation ..')
        print('Player ' + Player1 + ' Won!!')

        return 1
    # for vertical(end)

    # checking the moves of player two
    if game['1'] == 'O' and game['2'] == 'O' and game['3'] == 'O':
        print('Congratulation ..')
        print('Player ' + Player2 + ' Won!!')

        return 1  # used to end the game
    if game['4'] == 'O' and game['5'] == 'O' and game['6'] == 'O':
        print('Congratulation ..')
        print('Player ' + Player2 + ' Won!!')

        return 1
    if game['7'] == 'O' and game['8'] == 'O' and game['9'] == 'O':
        print('Congratulation ..')
        print('Player ' + Player2 + ' Won!!')

        return 1
    if game['1'] == 'O' and game['5'] == 'O' and game['9'] == 'O':
        print('Congratulation ..)')
        print('Player ' + Player2 + ' Won!!')

        return 1
    if game['1'] == 'O' and game['4'] == 'O' and game['7'] == 'O':
        print('Congratulation ..')
        print('Player ' + Player2 + ' Won!!')

        return 1
    if game['2'] == 'O' and game['5'] == 'O' and game['8'] == 'O':
        print('Congratulation ..)')
        print('Player ' + Player2 + ' Won!!')

        return 1
    if game['3'] == 'O' and game['6'] == 'O' and game['9'] == 'O':
        print('Congratulation ..')
        print('Player ' + Player2 + ' Won!!')

        return 1
    return 0



print('                                                               ------------------')
print('                                                                | 1  |  2 |  3 |')
print('                                                                |----|----|----|')
print('                                                                | 4  |  5 |  6 |')
print('                                                                |----|----|----|')
print('                                                                | 7  |  8 |  9 |')
print('                                                               -----------------')

print('This is game pattern\n\n')
print('\n')
print('\n')
print("Enter a number from 1 to 9 to give O/X on the board ")
while True:
    print('                                                            ----------------')
    print('                                                            | '+game['1'] + '  | ' + game['2'] + '  |  ' + game['3']+' |')
    print('                                                            |----|----|----|')
    print('                                                            | '+game['4'] + '  | ' + game['5'] + '  |  ' + game['6']+' |')
    print('                                                            |----|----|----|')
    print('                                                            | '+game['7'] + '  | ' + game['8'] + '  |  ' + game['9']+' |')
    print('                                                            ----------------')
    end_check = check()
    if moves == 9 or end_check == 1:
        break
    while True:     # input from players
        if gamer == 1:  # choose player
            p1_input = input('player '+Player1 +' turn : ')
            if p1_input.upper() in game and game[p1_input.upper()] == ' ':
                game[p1_input.upper()] = 'X'
                gamer = 2
                break
            # on wrong input
            else:
                print('Invalid input, please try again')
                continue
        else:
            p2_input = input('player '+Player2+' turn : ')
            if p2_input.upper() in game and game[p2_input.upper()] == ' ':
                game[p2_input.upper()] = 'O'
                gamer = 1
                break
            else:  # on wrong input
                print('Invalid input, please try again')
                continue
    moves += 1
    print('---------------------')
    print()