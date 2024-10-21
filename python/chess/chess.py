# Initialize the board with ranks and files properly organized
empty_square = " " * 12
rank_1 = {"h": empty_square, "g": empty_square, "f": empty_square, "e": empty_square, "d": empty_square, "c": empty_square, "b": empty_square, "a": empty_square}
rank_2 = {"h": empty_square, "g": empty_square, "f": empty_square, "e": empty_square, "d": empty_square, "c": empty_square, "b": empty_square, "a": empty_square}
rank_3 = {"h": empty_square, "g": empty_square, "f": empty_square, "e": empty_square, "d": empty_square, "c": empty_square, "b": empty_square, "a": empty_square}
rank_4 = {"h": empty_square, "g": empty_square, "f": empty_square, "e": empty_square, "d": empty_square, "c": empty_square, "b": empty_square, "a": empty_square}
rank_5 = {"h": empty_square, "g": empty_square, "f": empty_square, "e": empty_square, "d": empty_square, "c": empty_square, "b": empty_square, "a": empty_square}
rank_6 = {"h": empty_square, "g": empty_square, "f": empty_square, "e": empty_square, "d": empty_square, "c": empty_square, "b": empty_square, "a": empty_square}
rank_7 = {"h": empty_square, "g": empty_square, "f": empty_square, "e": empty_square, "d": empty_square, "c": empty_square, "b": empty_square, "a": empty_square}
rank_8 = {"h": empty_square, "g": empty_square, "f": empty_square, "e": empty_square, "d": empty_square, "c": empty_square, "b": empty_square, "a": empty_square}


# Outer dictionary to represent ranks (1-8)
board = {"1": rank_1, "2": rank_2, "3": rank_3, "4": rank_4, "5": rank_5, "6": rank_6, "7": rank_7, "8": rank_8}

# Place pieces
white_pieces = ["white_pawn  ", "white_bishop", "white_knight", "white_king  ", "white_queen ", "white_rook  "]
black_pieces = ["black_pawn  ", "black_bishop", "black_knight", "black_king  ", "black_queen ", "black_rook  "]

# Place white pieces
board["1"]["a"], board["1"]["h"] = white_pieces[-1], white_pieces[-1]  # rooks
board["1"]["b"], board["1"]["g"] = white_pieces[2], white_pieces[2]    # knights
board["1"]["c"], board["1"]["f"] = white_pieces[1], white_pieces[1]    # bishops
board["1"]["d"] = white_pieces[-2]                                     # queen
board["1"]["e"] = white_pieces[-3]                                     # king
for file in "abcdefgh":
    board["2"][file] = white_pieces[0]                                 # pawns

# Place black pieces
board["8"]["a"], board["8"]["h"] = black_pieces[-1], black_pieces[-1]  # rooks
board["8"]["b"], board["8"]["g"] = black_pieces[2], black_pieces[2]    # knights
board["8"]["c"], board["8"]["f"] = black_pieces[1], black_pieces[1]    # bishops
board["8"]["d"] = black_pieces[-2]                                     # queen
board["8"]["e"] = black_pieces[-3]                                     # king
for file in "abcdefgh":
    board["7"][file] = black_pieces[0]                                 # pawns

# Display the board dictionary to check placement
def check_white_space(piece):
    num_white_spaces = 13-(len(piece))
    whitespace = num_white_spaces * " "
    return whitespace

def display_board(board):
    for rank, file_dict in board.items():
        print(f"{rank}: {file_dict}")
display_board(board)


# take input rank # and file letter and destination square
while True:

    start_sq = input("Square of piece you want to move: ")
    rank_start = start_sq[-1]
    file_start = start_sq[0]

    end_sq = input("Square to move to or capture on:  ")
    file_end = end_sq[0]
    rank_end = end_sq[-1]

    board[rank_end][file_end] = board[rank_start][file_start]
    board[rank_start][file_start] = empty_square  # if legal?

    display_board(board)


# take inputs as starting square end square, ex d2 d4
