def exist(board: list[list[str]], word: str) -> bool:
    m, n = len(board), len(board[0])

    def search(row, col, depth):
        if depth == len(word):
            return True
        if row < 0 or row >= m or col < 0 or col >= n or board[row][col] != word[depth]:
            return False

        temp = board[row][col]
        board[row][col] = '#' # visited

        found = (search(row - 1, col, depth + 1) or
                 search(row + 1, col, depth + 1) or
                 search(row, col - 1, depth + 1) or
                 search(row, col + 1, depth + 1)
        )

        board[row][col] = temp
        return found

    for r in range(m):
        for c in range(n):
            if search(r, c, 0):
                return True
    return False

def test_wordsearch():
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    assert exist(board, "ABCCED") == True
    assert exist(board, "SEE") == True
    assert exist(board, "BES") == False
