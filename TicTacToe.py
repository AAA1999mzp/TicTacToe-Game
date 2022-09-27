board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}
player = 'X'
bot = 'O'

def printboard(board):
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("\n")

printboard(board)
print ("Positions are as Follows: ")
print ("1, 2, 3 ")
print ("4, 5, 6 ")
print ("7, 8, 9 ")
print ("\n")
print ("player = X ")
print ("bot = O ")
print ("\n")
print ("Wait for computer take Time ")

def emptyspace(position):
    if board[position] == ' ':
        return True 
    return False 

def insert(letter, position):
    if emptyspace(position):
        board[position] = letter 
        printboard(board)
        if checkdraw():
            print("Draw!")
            exit() 
        if checkwin():
            if letter == 'O':
                print("Computer wins!")
                exit()
            else:
                print("Player wins!")
                exit()
        return 
    else:
        print("Invalid position")
        position = int(input("Please enter a new position: "))
        insert(letter, position)
        return    

def checkwin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False

def checkmark(mark):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False

def checkdraw():
    for key in board.keys():
        if board[key] == ' ':
            return False 
    return True 

def playermove():
    position = int(input("Enter a position: "))
    insert(player, position)
    return 

def compmove():
    bestScore = -800
    bestMove = 0
    depth=1
    for key in board.keys():
        if board[key] == ' ':
            board[key] = bot
            score = minimax(board, depth + 1, False)
            board[key] = ' '
            if score > bestScore:
                bestScore = score 
                bestMove = key
    insert(bot, bestMove)
    return 
def minimax(board,depth,ismax):
    if checkmark(bot):
        return 1 
    elif checkmark(player):
        return -1 
    elif checkdraw():
        return 0
        
    if ismax:
        bestScore = -800 
        for key in board.keys():
            if board[key] == ' ':
                board[key] = bot 
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if score > bestScore:
                    bestScore = score
        return bestScore 
    else:
        bestScore = 800 
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player 
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if score < bestScore:
                    bestScore = score 
        return bestScore


while not checkwin():
    compmove()
    playermove()
