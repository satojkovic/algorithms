def is_valid_row(board):
    rows, cols = len(board), len(board[0])
    for row in range(rows):
        # hash setは行のチェックごとに初期化
        digits = set()
        for col in range(cols):
            # '.'は対象外
            if board[row][col] == '.':
                continue
            elif board[row][col] in digits:
                return False
            else:
                digits.add(board[row][col])
    return True

def is_valid_col(board):
    rows, cols = len(board), len(board[0])
    for col in range(cols):
        # hash setは列のチェックごとに初期化
        digits = set()
        for row in range(rows):
            if board[row][col] == '.':
                continue
            elif board[row][col] in digits:
                return False
            else:
                digits.add(board[row][col])
    return True

def is_valid_subbox(board):
    def is_valid(board, start_row, start_col):
        # hash setはsubboxのチェックごとに初期化
        digits = set()
        for row in range(start_row, start_row + 3):
            for col in range(start_col, start_col + 3):
                if board[row][col] == '.':
                    continue
                elif board[row][col] in digits:
                    return False
                else:
                    digits.add(board[row][col])
        return True

    rows, cols = len(board), len(board[0])
    for row in range(0, rows, 3):
        for col in range(0, cols, 3):
            if not is_valid(board, row, col):
                return False
    return True

def is_valid_sudoku(board):
	# 行方向のチェック、列方向のチェック、sub-boxのチェックがTrueかFalseかで決定
	return is_valid_row(board) and is_valid_col(board) and is_valid_subbox(board)


def test_is_valid_sudoku():
    board = [
        ["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    assert is_valid_sudoku(board) is True

    board = [
        ["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3" ]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    assert is_valid_sudoku(board) is False

from collections import defaultdict
def is_valid_sudoku_simple(board):
    row_digits = defaultdict(set)
    col_digits = defaultdict(set)
    subbox_digits = defaultdict(set)

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == '.':
                continue
            if (board[row][col] in row_digits[row] or
                    board[row][col] in col_digits[col] or
                    board[row][col] in subbox_digits[(row//3, col//3)]):
                    return False
            row_digits[row].add(board[row][col])
            col_digits[col].add(board[row][col])
            subbox_digits[(row//3, col//3)].add(board[row][col])
    return True

def test_is_valid_sudoku_simple():
    board = [
        ["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    assert is_valid_sudoku_simple(board) is True

    board = [
        ["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3" ]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    assert is_valid_sudoku_simple(board) is False
