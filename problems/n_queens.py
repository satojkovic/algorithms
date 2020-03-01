class Board:
    def __init__(self, board_size) -> None:
        self.n_queens = 0
        self.max_queens = board_size
        self.board_size = board_size
        self.grid = [self.board_size * [0] for _ in range(self.board_size)]
        self.queen = {}

    def print_queen(self):
        for k in self.queen.keys():
            print(k, self.queen[k])

    def has_max_queens(self):
        return self.n_queens == self.max_queens

    def unattacked_positions(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.grid[row][col] != 0:
                    continue
                yield row, col

    def place_queen(self, pos):
        row, col = pos[0], pos[1]
        self.queen[row] = col
        self.grid[row][col] -= 1
        self._update_grid(pos, -1)
        self.n_queens += 1

    def remove_queen(self, pos):
        row, col = pos[0], pos[1]
        del self.queen[row]
        self.grid[row][col] += 1
        self._update_grid(pos, 1)
        self.n_queens -= 1

    def _update_grid(self, pos, update_val):
        row, col = pos[0], pos[1]
        for c in range(self.board_size):
            if c != col:
                self.grid[row][c] += update_val
        for r in range(self.board_size):
            if r != row:
                self.grid[r][col] += update_val
        for r in range(self.board_size):
            for c in range(self.board_size):
                if r == row and c == col:
                    continue
                if r - c - (row - col) == 0 or r + c - (row + col) == 0:
                    self.grid[r][c] += update_val

    def queens(self):
        if self.has_max_queens():
            return True
        for pos in self.unattacked_positions():
            self.place_queen(pos)
            solution = self.queens()
            if solution:
                return solution
            self.remove_queen(pos)
        return False

if __name__ == "__main__":
    board = Board(4)
    board.queens()
    board.print_queen()