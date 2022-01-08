class WordSearch:
    def exist(self, board, word):
        self.nrows, self.ncols = len(board), len(board[0])
        self.board = board
        for row in range(self.nrows):
            for col in range(self.ncols):
                if self.backtrack(row, col, word, 0):
                    return True
        return False

    def backtrack(self, row, col, word, idx):
        if row < 0 or row == self.nrows or col < 0 or col == self.ncols or word[idx] != self.board[row][col]:
            return False
        if idx == len(word) - 1 and word[idx] == self.board[row][col]:
            return True
        self.board[row][col] = '*'
        for row_delta, col_delta in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            ret = self.backtrack(row + row_delta, col +
                                 col_delta, word, idx + 1)
            if ret:
                break
        self.board[row][col] = word[idx]
        return ret


def test_wordsearch():
    ws = WordSearch()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    assert ws.exist(board, "ABCCED") == True
    assert ws.exist(board, "SEE") == True
    assert ws.exist(board, "BES") == False
