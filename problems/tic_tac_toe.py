class TicTacToe:
    def __init__(self, n):
        self.grid = [n * [0] for _ in range(n)]
        self.n = n

    def move(self, row, col, player):
        if self.grid[row][col] != 0:
            return False

        self.grid[row][col] = player
        if self.check_win_condition(player):
            return player
        else:
            return 0

    def check_win_condition(self, player):
        return self.check_horizontal(player) or self.check_vertical(player) or self.check_diagonal(player)

    def check_horizontal(self, player):
        for r in range(self.n):
            if sum([1 if self.grid[r][c] == player else 0 for c in range(self.n)]) == self.n:
                return True
        return False

    def check_vertical(self, player):
        for c in range(self.n):
            if sum([1 if self.grid[r][c] == player else 0 for r in range(self.n)]) == self.n:
                return True
        return False

    def check_diagonal(self, player):
        if sum([1 if self.grid[i][i] == player else 0 for i in range(self.n)]) == self.n:
            return True
        if sum([1 if self.grid[i][self.n-i-1] == player else 0 for i in range(self.n)]) == self.n:
            return True
        return False