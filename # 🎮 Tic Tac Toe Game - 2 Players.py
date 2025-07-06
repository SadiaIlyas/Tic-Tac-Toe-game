print("welcome to sadia Tic Tac Toe game")
board=[" "," "," "," "," "," "," "," "," "]
def print_board():
    print()
    print(f"{board[0]} | {board[1]} | {board[2]} ")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]} ")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]} ")
    print()
def win(player):
    conditions=[[0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]]   #diagonals
    for i in conditions:
         if board[i[0]] == board[i[1]] == board[i[2]] == player:
             return True
    return False
def play_game():
    current_player="X"
    turns=0
    while True:
        print_board()
        try:
            move=int(input(f"player{current_player} enter position(1-9):"))- 1
        except ValueError:
            print("❌ please enter a number batween 1 and 9")
            continue
        if(move<0 or move>8):
            print("❌ Invalid position! Try again")
            continue
        if(board[move]!=" "):
            print("❌ That spot is already taken!")
            continue
        board[move]=current_player
        turns+=1
        if(win(current_player)):
            print_board()
            print(f"🏆 Player {current_player} wins!")
            break
        if(turns==9):
            print_board()
            print("its a draw")
            break
        current_player="O" if(current_player=="X") else "X"
play_game()


