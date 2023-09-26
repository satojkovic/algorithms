def count_num_of_battle_ships(board):
    count = 0
    rows, cols = len(board), len(board[0])
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == "X":
                count = assign_label(board, row, col, count)
            else:
                board[row][col] = "0"
    return count


def assign_label(board, row, col, count):
    left_label = board[row][col - 1] if col - 1 >= 0 else "0"
    upper_label = board[row - 1][col] if row - 1 >= 0 else "0"
    if left_label != "0":
        board[row][col] = left_label
    elif upper_label != "0":
        board[row][col] = upper_label
    else:
        count += 1
        board[row][col] = str(count)
    return count


def test_count_num_of_battle_ships():
    board = [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]
    assert count_num_of_battle_ships(board) == 2

    board = [["."]]
    assert count_num_of_battle_ships(board) == 0
