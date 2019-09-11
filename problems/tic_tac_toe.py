class TicTacToe:
    def __init__(self, n):
        self.state = [n * [0] for _ in range(n)]
        self.n = n

    def update(self, row, col, player):
        self.state[row][col] = player

    def move(self, row, col, player):
        if self.state[row][col] != 0:
            return False
        else:
            self.update(row, col, player)
            if self.check_win_condition(row, col, player):
                return player
            else:
                return 0

    def check_horizontal(self, row, col, player):
        for c in range(0, self.n):
            if self.state[row][c] != player:
                return False
        return True

    def check_vertical(self, row, col, player):
        for r in range(0, self.n):
            if self.state[r][col] != player:
                return False
        return True

    def check_diag_lu(self, row, col, player):
        while row >= 0 and col >= 0:
            if self.state[row][col] != player:
                return False
            row -= 1
            col -= 1
        return True

    def check_diag_rd(self, row, col, player):
        while row < self.n and col < self.n:
            if self.state[row][col] != player:
                return False
            row += 1
            col += 1
        return True

    def check_diag_ld(self, row, col, player):
        while row < self.n and col >= 0:
            if self.state[row][col] != player:
                return False
            row += 1
            col -= 1
        return True

    def check_diag_ru(self, row, col, player):
        while row >= 0 and col < self.n:
            if self.state[row][col] != player:
                return False
            row -= 1
            col += 1
        return True

    def check_diagonal(self, row, col, player):
        if (self.check_diag_ld(row, col, player) and self.check_diag_ru(row, col, player)) and \
            (self.check_diag_rd(row, col, player) and self.check_diag_lu(row, col, player)):
                return True
        else:
            return False

    def check_win_condition(self, row, col, player):
        if self.check_horizontal(row, col, player) or \
            self.check_vertical(row, col, player) or \
                self.check_diagonal(row, col, player):
            return player
        else:
            return 0
