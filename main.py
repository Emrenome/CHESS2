class ChessGame:
    def __init__(self):
        self.board = self.create_board()
        self.current_player = 'White'

    def create_board(self):
        board = [
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        ]
        return board

    def print_board(self):
        print("   A B C D E F G H")
        for i in range(8):
            print(f"{8 - i}  {' '.join(self.board[i])}  {8 - i}")
        print("   A B C D E F G H")

    def get_move(self):
        move = input(f"{self.current_player}'s turn. Enter your move (e.g., 'e2 e4'): ")
        return move.split()

    def is_valid_move(self, move):
        # Check if the move is in algebraic notation (e.g., 'e2 e4')
        if len(move) != 2:
            return False

        src, dest = move
        return src.isalpha() and src.isnumeric() and dest.isalpha() and dest.isnumeric()

    def make_move(self, move):
        src, dest = move
        x1, y1 = ord(src[0].upper()) - 65, 8 - int(src[1])
        x2, y2 = ord(dest[0].upper()) - 65, 8 - int(dest[1])

        if not (0 <= x1 < 8 and 0 <= y1 < 8 and 0 <= x2 < 8 and 0 <= y2 < 8):
            return False

        piece = self.board[y1][x1]
        if self.current_player == 'White' and not piece.isupper():
            return False
        elif self.current_player == 'Black' and not piece.islower():
            return False

        self.board[y1][x1] = ' '
        self.board[y2][x2] = piece
        self.current_player = 'White' if self.current_player == 'Black' else 'Black'
        return True

    def play(self):
        while True:
            self.print_board()
            move = self.get_move()

            if not self.is_valid_move(move):
                print("Invalid move. Please use algebraic notation (e.g., 'e2 e4').")
                continue

            if self.make_move(move):
                if self.is_checkmate():
                    print(f"Checkmate! {self.current_player} wins!")
                    break
            else:
                print("Invalid move. Try again.")

    def is_checkmate(self):
        # Check if there's a checkmate (not implemented in this simple version)
        return False


if __name__ == "__main__":
    chess_game = ChessGame()
    chess_game.play()
