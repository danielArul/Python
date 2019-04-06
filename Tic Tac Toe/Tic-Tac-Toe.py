# The board function is used to layout the design of the board
def theboard(board):
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])

# This function takes 2 parameters and checks if any of the players have won
def win(board, marker):
    if ((board[1] == marker and board[2] == marker and board[3] == marker) or
            (board[4] == marker and board[5] == marker and board[6] == marker) or
            (board[7] == marker and board[8] == marker and board[9] == marker) or
            (board[1] == marker and board[4] == marker and board[7] == marker) or
            (board[2] == marker and board[5] == marker and board[8] == marker) or
            (board[3] == marker and board[6] == marker and board[9] == marker) or
            (board[1] == marker and board[5] == marker and board[9] == marker) or
            (board[3] == marker and board[5] == marker and board[7] == marker)):
        return True


# This function prompts the user for the correct marker
def markersAndNames():
    player1_marker = ''
    player2_marker = ''
    player1_name= input('Player 1, Enter your name!')
    player2_name=input('player 2, Enter your name!')
    while not (player1_marker == 'X' or player1_marker == 'O'):
        player1_marker = input(player1_name+' pick O or X')
    if player1_marker == 'X':
        return (player1_name, player2_name, 'X', 'O')
    else:
        return (player1_name,player2_name,'O', 'X')


# This function is used to check if a spot in the board is empty
def emptyspot(board, position):
    if board[position] == '':
        return True


# This function is used to determine if the board is fully cocupied
def boardfull(board):
    for i in range(1, 10):
        if board[i] == '':
            return False
    return True

#This method checks to see if the input by the player is valid and return the position if it is.
def pspot(board,player):
    position = input('pick a spot ' + player)
    while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', ] or position == '':
        position = input(player+'Pick a valid spot')
    position = int(position)
    while not emptyspot(board, position):
        position = int(input(player +'pick a different spot'))
    return position

turn = 'player1' #initialzing turn
game_board = [''] * 10 #setting up the board
pl1n,pl2n,player1_marker, player2_marker = markersAndNames() #retrieving markers and names of players

while True:
    #Code for player1
    if turn == 'player1':
        pl1 = pspot(game_board,pl1n)
        game_board[pl1] = player1_marker
        theboard(game_board)
        if win(game_board, player1_marker):
            print(pl1n + ', You won!')
            break
        elif boardfull(game_board):
            print('The game is a draw')
            break
        else:
            turn = 'player2'
            
    #Code for player 2
    elif turn == 'player2':
        pl2 = pspot(game_board,pl2n)
        game_board[pl2] = player2_marker
        theboard(game_board)
        if win(game_board, player2_marker):
            print(pl2n+ ', You won!')
            break
        elif boardfull(game_board):
            print('The game is a draw')
            break
        else:
            turn = 'player1'
