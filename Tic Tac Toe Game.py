#The index of outer list represents the rows
#The index of inner list represents the columns
board = [['-','-','-'],
         ['-','-','-'],
         ['-','-','-']]
#function for displaying the board
def display_board():
    for i in range(len(board)):
        print(board[i][0]+' | '+board[i][1]+' | '+board[i][2])
#check for the win
def has_player_won():
    for i in range(0,3):                                                            #check rows
        if board[i][0]== board[i][1]==board[i][2] and board[i][0]!='-':
            return True        
    for j in range(0,3):                                                            #check columns
        if board[0][j]==board[1][j]==board[2][j] and board[0][j]!='-':
            return True
    #check diagonals
    if board[0][0]==board[1][1]==board[2][2] and board[0][0]!='-':                  #diagonal 1
        return True
    elif board[0][2]==board[1][1]==board[2][0] and board[0][2]!='-':                #diagonal 2
        return True
    return False
    
#check for a tie
def is_tie():
    for i in range(0,3):
        if '-' in board[i]:
            return False
    return not has_player_won()
    
#the players turn and handle players turn
player='Player X'
while (not has_player_won()) and (not is_tie()):                                    #check if game is still going
    display_board()
    print('{0}\'s turn'.format(player))                                             #Check for valid input position
    position=input('Which position from 1-9?: ')
    while position not in ['1','2','3','4','5','6','7','8','9']:
        print('Try again')
        position=input('Which position from 1-9?: ')
    position=int(position)
    (row,column) = ((position-1)//3,(position-1)%3)
    if board[row][column]=='-':                                                     #Check if position is empty
        if player=='Player X':
            board[row][column]='X'
            if has_player_won():
                display_board()
                print('{0} HAS WON!'.format(player))
            player='Player O'
        else:
            board[row][column]='O'
            if has_player_won():
                display_board()
                print('{0} HAS WON!'.format(player))
            player='Player X'
    else:                                                                           #Give warning if position is not empty
        print('You can\'t go there!'.upper())
        print('Try again')
if is_tie():
    print('IT IS A TIE!')
input('Press Enter to exit')
