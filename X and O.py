#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Gameboard():
    def __init__(self):
        # Initialize a 3x3 empty board represented by numbers 1-9
        self.gameBoard = [' '] * 9

    def printBoard(self, board):
        # Prints the game board in a 3x3 grid format
        print(f'{board[0]} | {board[1]} | {board[2]}')
        print('--+---+--')
        print(f'{board[3]} | {board[4]} | {board[5]}')
        print('--+---+--')
        print(f'{board[6]} | {board[7]} | {board[8]}')

    def set_items(self, item, position, board):
        # Place 'X' or 'O' on the game board at the given position (0-based index)
        if board[position - 1] == ' ':
            board[position - 1] = item
        else:
            print("Position already taken! Choose another.")

    def is_game_won(self, board):
        # Check all winning combinations
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for combo in win_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
                return True
        return False

    def is_board_full(self, board):
        # Check if the board is full (i.e., no more empty spaces)
        return ' ' not in board


class Game:
    def game_start(self):
        # Initialize the game board and players
        self.controlBoard = Gameboard()  # Control Board object of type Gameboard
        self.game_board = self.controlBoard.gameBoard  # Store the game board from the Gameboard object
        self.playerOne = "O"  # Assign 'O' to Player 1
        self.playerTwo = 'X'  # Assign 'X' to Player 2
        print("Welcome to X-O game")
        
        # Get player names
        print("Please enter player one's name:")
        self.player_one = input(' : ')  # Accept Player 1's name
        print("Please enter player two's name:")
        self.player_two = input(' : ')  # Accept Player 2's name

        self.controlBoard.printBoard(self.game_board)  # Print the initial game board
        self.turn = 1  # Start the turn counter

    def game_end(self):
        # Check if the game has ended
        replay = input("Press 0 to quit or 1 to play again: ")
        try:
            if int(replay):  # If replay is 1, start a new game
                self.game_running = True
                self.game_start()
            else:
                print("Thanks for playing!")
                self.game_running = False
        except:
            print("A number must be entered")
            self.game_end()

    def take_turn(self, user, item):
        print(f"{user}, choose a place between 1 and 9")
        try:
            position = int(input(': '))  # Get input position for placing 'X' or 'O'
            if position > 9 or position < 1:
                raise Exception  # Raise exception if input is out of range
        except:
            print("Pick a number between 1 and 9")
            return self.take_turn(user, item)  # Retry the turn if an invalid input
        
        self.controlBoard.set_items(item, position, self.game_board)  # Set the position on the board
        self.controlBoard.printBoard(self.game_board)  # Print the updated board
        
        if self.controlBoard.is_game_won(self.game_board):  # Check if the game is won
            print(f"{user} wins!")
            self.game_running = False

    def main(self):
        self.game_running = True
        self.game_start()
        
        # Loop to manage turns while the game is running
        while self.game_running:
            if self.turn % 2 != 0:  # Player one's turn (odd turns)
                self.take_turn(self.player_one, 'O')
            else:  # Player two's turn (even turns)
                self.take_turn(self.player_two, 'X')
            
            # Check if the board is full for a draw
            if self.controlBoard.is_board_full(self.game_board):
                print("It's a draw!")
                self.game_running = False
            
            # Increment the turn counter after each turn
            self.turn += 1
            if not self.game_running:  # If game has ended, ask for replay
                self.game_end()

if __name__ == '__main__':  # Main entry point
    Game().main()  # Start the game

    
    


# In[2]:




