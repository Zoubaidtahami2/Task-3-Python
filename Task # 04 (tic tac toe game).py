import random
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    return False
def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True
def player_move(board, player):
    while True:
        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
            if row in range(3) and col in range(3) and board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("Invalid move! Try again.")
        except ValueError:
            print("Invalid input! Please enter a number.")
def computer_move(board, player):
    print("Computer's turn:")
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            board[row][col] = player
            break
def play_game():
    board = [[" "]*3 for _ in range(3)]
    players = ["X", "O"]
    random.shuffle(players)
    current_player = players[0]
    print_board(board)
    while True:
        if current_player == "X":
            player_move(board, current_player)
        else:
            computer_move(board, current_player)

        print_board(board)
        if check_winner(board, current_player):
            print(f"{current_player} wins!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        current_player = "X" if current_player == "O" else "O"
if __name__ == "__main__":
    play_game()