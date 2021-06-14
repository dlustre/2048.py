from utilities import generate_piece, print_board
import copy

DEV_MODE = False


def main(game_board: [[int, ], ]) -> [[int, ], ]:
    """
    2048 main function, runs a game of 2048 in the console.

    Uses the following keys:
    w - shift up
    a - shift left
    s - shift down
    d - shift right
    q - ends the game and returns control of the console
    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: returns the ending game board
    """
    # Initialize board's first cell
    
    # TODO: generate a random piece and location using the generate_piece function
    generated_piece = generate_piece(game_board)
    # TODO: place the piece at the specified location
    game_board[generated_piece['row']][generated_piece['column']] = generated_piece['value']
    # Initialize game state trackers
    # Game Loop
    while True:
        
        # TODO: Reset user input variable
        user_input = ' '
        # TODO: Take computer's turn
        # place a random piece on the board
        random_piece = generate_piece(game_board)
        game_board[random_piece['row']][random_piece['column']] = random_piece['value']

        # check to see if the game is over using the game_over function
        if game_over(game_board):
            print('game over')
            return game_board
        # TODO: Show updated board using the print_board function
        print_board(game_board)
        # TODO: Take user's turn
        
        # create a copy of game_board
        copied_board = copy.deepcopy(game_board)
        while copied_board == game_board:
            
            # Take input until the user's move is a valid key
            user_input = input()
            valid_keys = ['w', 'a', 's', 'd', 'q']
            while user_input not in valid_keys:
                print('invalid input, retry')
                user_input = input()
            # if the user quits the game, print Goodbye and stop the Game Loop
            if user_input == 'q':
                print('Goodbye')
                return game_board
            # Execute the user's move
            
            # if input is a, go LEFT
            if user_input == 'a':
                print('left')

                # merge
                for (row_index, row) in enumerate(game_board):
                    for (col_index, cell) in enumerate(row):
                        # if the cell isn't empty and if it's not at the very left
                        if col_index != 0 and cell != 0:
                            # loop through the cells to the left of the current cell
                            for leftward_cell in range(col_index - 1, -1, -1):
                                # if the cell to the left is a different number, break for-loop
                                if game_board[row_index][leftward_cell] != 0 and game_board[row_index][leftward_cell] != cell:
                                    break
                                # if a cell to the left is the same number, merge and stop looking at leftward cells
                                elif game_board[row_index][leftward_cell] == cell and copied_board[row_index][leftward_cell] == game_board[row_index][leftward_cell]:
                                    game_board[row_index][leftward_cell] += cell
                                    game_board[row_index][col_index] = 0
                                    break
                # slide all elements left
                for (row_index, row) in enumerate(game_board):
                    for (col_index, cell) in enumerate(row):
                        # if the cell is empty and not rightmost, shift the nearest number to its place
                        if cell == 0 and col_index != 3:
                            for rightward_cell in range(col_index + 1, 4):
                                if game_board[row_index][rightward_cell] != 0:
                                    game_board[row_index][col_index] = game_board[row_index][rightward_cell]
                                    game_board[row_index][rightward_cell] = 0
                                    break
            # if input is d, go RIGHT
            elif user_input == 'd':
                print('right')

                # merge
                for (row_index, row) in enumerate(game_board):
                    for (col_index, cell) in enumerate(row):
                        # if the cell isn't empty and if it's not at the very right
                        if (3 - col_index) != 3 and game_board[row_index][3 - col_index] != 0:
                            # loop through the cells to the right of the current cell
                            for rightward_cell in range((3 - col_index) + 1, 4):
                                # if the cell to the right is a different number, break for-loop
                                if game_board[row_index][rightward_cell] != 0 and game_board[row_index][rightward_cell] != game_board[row_index][3 - col_index]:
                                    break
                                # if a cell to the left is the same number, merge
                                elif game_board[row_index][rightward_cell] == game_board[row_index][3 - col_index] and game_board[row_index][rightward_cell] == copied_board[row_index][rightward_cell]:
                                    game_board[row_index][rightward_cell] += game_board[row_index][3 - col_index]
                                    game_board[row_index][3 - col_index] = 0
                                    break
                # slide all elements right
                for (row_index, row) in enumerate(game_board):
                    for (col_index, cell) in enumerate(row):
                        # if the cell is empty and not leftmost, shift the nearest number to its place
                        if game_board[row_index][3 - col_index] == 0 and (3 - col_index) != 0:
                            for leftward_cell in range((3 - col_index) - 1, -1, -1):
                                if game_board[row_index][leftward_cell] != 0:
                                    game_board[row_index][3 - col_index] = game_board[row_index][leftward_cell]
                                    game_board[row_index][leftward_cell] = 0
                                    break
            # if input is w, go UP
            elif user_input == 'w':
                print('up')

                # merge
                for col_index in range(4):
                    for row_index in range(4):
                        # if the cell isn't empty and if it's not at the very top
                        if game_board[row_index][col_index] != 0 and row_index != 0:
                            # loop through the cells above the current cell
                            for upward_cell in range(row_index - 1, -1, -1):
                                # if the cell above it is a different number, break for-loop
                                if game_board[upward_cell][col_index] != 0 and game_board[upward_cell][col_index] != game_board[row_index][col_index]:
                                    break
                                # if a cell above it is the same number, merge and stop looking at above cells
                                elif game_board[upward_cell][col_index] == game_board[row_index][col_index] and game_board[upward_cell][col_index] == copied_board[upward_cell][col_index]:
                                    game_board[upward_cell][col_index] += game_board[row_index][col_index]
                                    game_board[row_index][col_index] = 0
                                    break
                # slide all elements up
                for col_index in range(4):
                    for row_index in range(4):
                        # if the cell is empty and not downmost, shift the nearest number to its place
                        if game_board[row_index][col_index] == 0 and row_index != 3:
                            for downward_cell in range(row_index + 1, 4):
                                if game_board[downward_cell][col_index] != 0:
                                    game_board[row_index][col_index] = game_board[downward_cell][col_index]
                                    game_board[downward_cell][col_index] = 0
                                    break
            # if input is s, go DOWN
            # TO DO
            elif user_input == 's':
                print('down')
           
                # merge
                for col_index in range(4):
                    for row_index in range(3, -1, -1):
                        # if the cell isn't empty and if it's not at the very bottom
                        if game_board[row_index][col_index] != 0 and row_index != 3:
                            # loop through the cells below the current cell
                            for downward_cell in range(row_index + 1, 4):
                                # if the cell below it is a different number, break for-loop
                                if game_board[downward_cell][col_index] != 0 and game_board[downward_cell][col_index] != game_board[row_index][col_index]:
                                    break
                                # if a cell below it is the same number, merge and stop looking at below cells
                                elif game_board[downward_cell][col_index] == game_board[row_index][col_index] and game_board[downward_cell][col_index] == copied_board[downward_cell][col_index]:
                                    game_board[downward_cell][col_index] += game_board[row_index][col_index]
                                    game_board[row_index][col_index] = 0
                                    break
                # slide all elements down
                for col_index in range(4):
                    for row_index in range(3, -1, -1):
                        # if the cell is empty and not at the very top, shift nearest number to its place
                        if game_board[row_index][col_index] == 0 and row_index != 0:
                            for upward_cell in range(row_index - 1, -1, -1):
                                if game_board[upward_cell][col_index] != 0:
                                    game_board[row_index][col_index] = game_board[upward_cell][col_index]
                                    game_board[upward_cell][col_index] = 0
                                    break
            # Check if the user wins
            for row in game_board:
                for cell in row:
                    if cell == 2048:
                        return game_board
    return game_board


def game_over(game_board: [[int, ], ]) -> bool:
    """
    Query the provided board's game state.

    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: Boolean indicating if the game is over (True) or not (False)
    """
    # TODO: Loop over the board and determine if the game is over
    zerocounter = 0
    for row in game_board:
        for cell in row:
            if cell == 0:
                zerocounter += 1
    # if there is at least one zero, return false
    if zerocounter > 0:
        return False
    # else if there aren't any zeros, check if there are any matching pairs
    elif zerocounter == 0:
        for (row_index, row) in enumerate(game_board):
            for (col_index, cell) in enumerate(row):
                # if cell is at the very right and matches with the cell underneath, return false
                if col_index == 3:
                    # skips the bottom right cell since it has already been checked
                    if row_index != 3:
                        if cell == game_board[row_index + 1][col_index]:
                            return False
                # if cell is at the very bottom and matches with the cell to the right, return false
                elif row_index == 3:
                    # skips the bottom right cell since it has already been checked
                    if col_index != 3:
                        if cell == game_board[row_index][col_index + 1]:
                            return False
                else:
                    # if cell matches with a cell to the right or underneath, return false
                    if cell == game_board[row_index][col_index + 1] or cell == game_board[row_index + 1][col_index]:
                        return False
        # return true if the board is full and no matching pairs
        return True
    # TODO: Don't always return false


if __name__ == "__main__":
    main([[2, 2, 4, 0],
          [0, 0, 0, 0],
          [4, 4, 8, 0],
          [0, 0, 0, 0]])

