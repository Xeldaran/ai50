"""
Tic Tac Toe Player
"""

import math
import copy




X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX = 0
    countO = 0



    for list in board:
        for value in list:
            if value == 'X':
                countX = countX + 1
            elif value == 'O':
                countO = countO + 1

    if countX == countO:
        return 'X'
    elif countX > countO:
        return 'O'
    #print('i Should never reach this line of code. countX: ' + str(countX) + ' CountO: ' + str(countO))            #testcode

    raise NotImplementedError   #what do i have to do here?


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    actions (i, j) have to be a tuple!
    """
    
    """
    nested loop, with a counter for each loop. if neither X nor O is on a board position, the variable empty is true.
    If empty is true, the touple is added to the set. at the end the set is returned

    This probably isn't ideal, but i somehow only got it to work like that :/
    """


    returnvalue = set()         #set that will be filled with tuples and returned in the end
    counter=0                   #outer counter == row for the tuple.

    for list in board:
        innerCounter=0          #inner counter == cell for the tuple
        for value in list:
            empty = True
            #print('counter: ' + str(counter) + ' innterocunter: ' + str(innerCounter))         # test, can be ignored
            if value == 'X':
                empty = False
            elif value == 'O':
                empty = False
                
            if empty == True:
                returnvalue.add((counter, innerCounter))
                #print(returnvalue)                                                              #test, can be ignored
                
            innerCounter=innerCounter+1             #counter increments
        counter=counter+1                           #counter increments

    #print('returnvalue actions: ' + str(returnvalue))
    
    return returnvalue

    

    

    raise NotImplementedError           #??? do i have to add sth?!?


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    Ignore comments, i used that to test my code. Sorry.
    """


    result = copy.deepcopy(board)
    #print('These are the actions: ' + str(action[0]) + str(action[1]))
    row = action[0]                     #could be done without defining row & cell. but i think it reads nicely
    cell = action[1]

    result[row][cell] = player(board)
    
    #print('This is the new board state:')
    #print(result[0][0] + result[0][1] + result[0][2])
    #print(result[1][0] + result[1][1] + result[1][2])
    #print(result[2][0] + result[2][1] + result[2][2])

    #for i in result:
    #    print(*i)

    #print('This result is given back from result: ' + str(result[row][cell]))
    return result
    


    

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    """ old attempt for RowWin detect. thought it was buggy. turned out my minimax was buggy :o

    def rowWin(board):

        counter=0                   #outer counter == row for the tuple.

        for list in board:
            innerCounter=0          #inner counter == cell for the tuple
            Xwin = 0
            Owin = 0
            for value in list:
                if value == 'X':
                    Xwin = Xwin + 1
                    if Xwin == 3:
                        return 'x'
                elif value == 'O':
                    Owin = Owin + 1
                    if Owin == 3:
                        return 'O'
                #('Run: ' + str(counter) + ' Xwin: ' + str(Xwin) + ' Owin: ' + str(Owin))          #test line
                innerCounter=innerCounter+1             #counter increments

            counter=counter+1
        if counter == 3:
            return None
    """
    

    
    win = None
    #col1 wincheck
    if board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':
        #print ('X wins:11 ' + board[0][0] +board[1][0] + board[2][0])
        win = 'X'
    elif board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O':
        #print ('O wins:12 ' + board[0][0] +board[1][0] + board[2][0])
        win = 'O'

    #col2 wincheck
    if board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
        #print ('X wins:21 ' + board[0][1] +board[1][1] + board[2][1])
        win = 'X'
    elif board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O':
        #print ('O wins:22 ' + board[0][1] +board[1][1] + board[2][1])
        win = 'O'

    #col3 wincheck
    if board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
        #print ('X wins:31 ' + board[0][2] +board[1][2] + board[2][2])
        win = 'X'
    elif board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':
        #print ('O wins:32 ' + board[0][2] +board[1][2] + board[2][2])
        win = 'O'

    #row1 wincheck
    if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X':
        #print ('X wins:r11 ' + board[0][0] +board[0][1] + board[0][2])
        win = 'X'
    elif board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O':
        #print ('O wins:r12 ' + board[0][0] +board[0][1] + board[0][2])
        win = 'O'

    #row2 wincheck
    if board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':
        #print ('X wins:r21 ' + board[1][0] +board[1][1] + board[1][2])
        win = 'X'
    elif board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O':
        #print ('O wins:r22 ' + board[1][0] +board[1][1] + board[1][2])
        win = 'O'

    #row3 wincheck
    if board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
        #print ('X wins:r31 ' + board[2][0] +board[2][1] + board[2][2])
        win = 'X'
    elif board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O':
        #print ('O wins:r32 ' + board[2][0] +board[2][1] + board[2][2])
        win = 'O'

    #diag1 top left to bottom right wincheck
    if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        #print ('X wins:31 ' + board[0][0] +board[1][1] + board[2][2])
        win = 'X'
    elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
        #print ('O wins:32 ' + board[0][0] +board[1][1] + board[2][2])
        win = 'O'

    #diag2 top right to bottom left wincheck
    if board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        #print ('X wins:diag21 ' + board[0][2] +board[1][1] + board[2][0])
        win = 'X'
    elif board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
        #print ('O wins:diag22 ' + board[0][2] +board[1][1] + board[2][0])
        win = 'O'

    return win  

    raise NotImplementedError       #i don't know what to do here. i need to read up on exception handling i guess.


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    
    win = ' '
    win = winner(board)                  # this is 'X' if x won, 'O' if o won, otherwise None
    if win == 'X' or win == 'O':
        return True
    movesPossible = actions(board)       # is an empty set, if the board is full
    if len(movesPossible) == 0:
        return True
    else:
        return False
    

    raise NotImplementedError




def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 for a tie.
    """
    
    util = winner(board)
    if util == 'X':
        return 1
    elif util == '0':
        return -1
    else:
        return 0

    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    

    """
    1. return a value if a terminal state is found (+1, 0, -1)
    2. figure out available actions on the board
    3. call the max / min value function on each available action
    4. asses returnvalue 
    5. return result AIMove
    """


    cur_player = player(board)

    if cur_player == 'X':
        v = -100
        for action in actions(board):
            k = min_value(result(board, action))
            if k > v:
                v = k
                AIMove = action
    elif cur_player == 'O':
        v = 100
        for action in actions(board):
            k = max_value(result(board, action))
            if k < v:
                v = k
                AIMove = action
    return AIMove


  
def max_value(board):
    if terminal(board):
        return utility(board)
    v = -100
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v   

def min_value(board):
    if terminal(board):
        return utility(board)
    v = 100
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v    