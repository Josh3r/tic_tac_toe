import collections

class TicTacToe:
    # Initiliaser method
    def __init__(self):
        self.board = [["" for j in range(3)] for i in range(3)]
        self.box_indexes = collections.defaultdict(tuple) # Initialise a dictionary that stores box numbers as their actual positions, ie: 1 : (0,0)
        self.vacancies = 9 # Init 9 open slots in our board
        self.winner = None # Init no winner
        # Annotate the board
        num = 1
        for i in range(len(self.board)):
            # self.board[i] corresponds to a row in the board
            for j in range(len(self.board[0])):
                # self.board[j] corresponds to a column in the current row
                self.board[i][j] = str(num)
                self.box_indexes[num] = (i,j) # Store box number's real matrix position as a tuple
                num += 1
        
                
        self.vacancies = 9

    # Method to display board to players
    def display_board(self):
         for row in self.board:
             print(row) # Print row by row for better visibility than simply printing self.board

    # Method to place player marking on desired box_number
    def place(self,box_number, player):
        row_idx = self.box_indexes[box_number][0] # Retrive row index of box_number
        col_idx = self.box_indexes[box_number][1] # Retrieve column index of box_number
        if self.board[row_idx][col_idx] == "X" or self.board[row_idx][col_idx] == "O":
            # If the current box is already filled, we cannot place a mark here, and must alert the player
            return False 
        if player.number == 1:
            # If it is player 1
            self.board[row_idx][col_idx] = "X" # mark
            self.vacancies -= 1 # Decrement a slot vacancy
        else:
            # If it is player 2
            self.board[row_idx][col_idx] = "O" # mark
            self.vacancies -= 1 # Decrement a slot vacancy
            
        return True # Alert the player that placement has been successful

    # Method to check if game over conditions have been fufilled
    def isGameOver(self):
        
        # Checking row victory
        for row in self.board:
            # Check one row per iteration
            if row == ["X","X","X"]:
                # Implies a row victory
                self.winner = 1
                return True
            elif row == ["O","O","O"]:
                # Implies a row victory
                self.winner = 2
                return True

        # Checking column victory
        for j in range(len(self.board[0])):
            # Check one column per iteration
            column = self.board[0][j] + self.board[1][j] + self.board[2][j]
            if column == "XXX":
                # Implies a row victory
                self.winner = 1
                return True
            elif column == "OOO":
                # Implies a row victory
                self.winner = 2
                return True
            
        # Checking diagonal victory
        diagonal = self.board[0][0] + self.board[1][1] + self.board[2][2]
        if diagonal == "XXX":
            # Implies a row victory
            self.winner = 1
            return True
        elif diagonal == "OOO":
            # Implies a row victory
            self.winner = 1
            return True

        # Check stalemate
        if self.vacancies == 0:
            # If no win conditions but all vacanies filled, it is a stalemate
            return True
        
        # Else, this indicates match can carry on until win conditions or stalemate conditons
        return False

    # Method to get winner of the game
    def get_winner(self):
        return self.winner

class Player:
    # Initialiser method
    def __init__(self,name,number):
        self.name = name # Player name
        self.number = number # Player number (1 or 2)

    # Get method to receive player_name, better than simply accessing via player.name in main()
    def get_player_name(self):
        return self.name


def main():
    my_board = TicTacToe() # Init the board
    print("Enter name for Player 1:")
    p1_input_name = input()
    player1 = Player(p1_input_name, 1) # Init player 1
    print("Enter name for Player 2:")
    p2_input_name = input()
    player2 = Player(p2_input_name, 2) # Init player 2
    player1_name = player1.get_player_name() # Get and store player 1 name for easy reference in print()
    player2_name = player2.get_player_name() # Get and store player 2 name for easy reference in print()
    my_board.display_board() # display board
    isPlayer1Turn = True # We begin with player1
    # We continue receiving player inputs and displaying the board while game over conditions are not yet fufilled
    while not my_board.isGameOver():
        if isPlayer1Turn:
            print("%s, choose a box to place an 'x' into:" % player1_name)
            input_box_number1 = int(input()) # We received the player's desired slot as a string, turning it into an int
            # Attempt to place on box in board, repeatedly asking and allowing player to re-attempt placement if selected box is no longer vacant
            while my_board.place(input_box_number1, player1) == False:
                print("Sorry, the box has already been filled, please select another:")
                input_box_number1 = int(input())
        
            isPlayer1Turn = False # Set turn to player 2
            my_board.display_board() # Display changes
        else:
            print("%s, please input your desired column:" % player2_name)
            input_box_number2 = int(input()) # We received the player's desired slot as a string, turning it into an int
            # Attempt to place on box in board, repeatedly asking and allowing player to re-attempt placement if selected box is no longer vacant
            while my_board.place(input_box_number2, player2) == False:
                print("Sorry, the box has already been filled, please select another:")
                input_box_number2 = int(input())
                
            isPlayer1Turn = True # Set turn to player 1
            my_board.display_board() # Display changes
            
    winner_number = my_board.get_winner() # Obtain winner number
    if winner_number == 1:
        # Player 1 has won
        print("Congratulations %s! You have won." %player1_name)
    elif winner_number == 2:
        # Player 2 has won
        print("Congratulations %s! You have won." %player2_name)
    else:
        # Stalemate
        print("Game is over, thank you for playing!")
    
        
main()
