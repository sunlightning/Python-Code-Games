#Tic Tac Toe Game
#Made by Victor Ricardo

#Functions
def displayBoard(instructionsBoard, gameBoard):
    #displays positions example for player input.
    print(':INSTRUCTIONS BOARD:')

    for line in range(len(instructionsBoard)):

        for column in range(len(instructionsBoard[line])):

            if column < 2:
                print('[' + str(instructionsBoard[line][column]) + ']', end='')

            else:
                print('[' + str(instructionsBoard[line][column]) + ']')


    #displays actual game's board
    print('')
    print('======================')
    print('')
    print(":GAME'S BOARD:")

    for line in range(len(gameBoard)):

        for column in range(len(gameBoard)):

            if column < 2:
                print('[' + str(gameBoard[line][column]) + ']', end='')

            else:
                print('[' + str(gameBoard[line][column]) + ']')



#Variables
instructionsBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
gameBoard = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

displayBoard(instructionsBoard, gameBoard)
