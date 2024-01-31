class OthelloGame:
    def __init__(self, player_mode="friend"):
        self.board = [[0 for _ in range(8)] for _ in range(8)]
        self.board[3][3] = 1
        self.board[3][4] = -1
        self.board[4][3] = -1
        self.board[4][4] = 1
        self.current_player = 1
        self.player_mode = player_mode

    def is_valid_move(self, row, col):
        if self.board[row][col] != 0:
            return False

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == -self.current_player:
                while 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == -self.current_player:
                    r += dr
                    c += dc
                if 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == self.current_player:
                    return True

        return False

    def flip_disks(self, row, col):
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        for dr, dc in directions:
            r, c = row + dr, col + dc
            flip_list = []
            if 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == -self.current_player:
                while 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == -self.current_player:
                    flip_list.append((r, c))
                    r += dr
                    c += dc
                if 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == self.current_player:
                    for fr, fc in flip_list:
                        self.board[fr][fc] = self.current_player

    def make_move(self, row, col):
        if self.is_valid_move(row, col):
            self.board[row][col] = self.current_player
            self.flip_disks(row, col)
            self.current_player *= -1

    def is_game_over(self):
        return len(self.get_valid_moves()) == 0 or all(all(cell != 0 for cell in row) for row in self.board)

    def get_winner(self):
        black_count = sum(row.count(1) for row in self.board)
        white_count = sum(row.count(-1) for row in self.board)

        if black_count > white_count:
            return 1
        elif black_count < white_count:
            return -1
        else:
            return 0

    def get_valid_moves(self):
        valid_moves = []
        row = 0
        while row < 8:
            col = 0
            while col < 8:
                if self.is_valid_move(row, col):
                    valid_moves.append((row, col))
                col += 1
            row += 1
        return valid_moves