import chess

from chess.polyglot import zobrist_hash

class ChessBoard(chess.Board):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__hash__ = zobrist_hash

    def __hash__(self):
        return self.__hash__(self)

    def check_end_game(self):
        queens = self.pieces(chess.QUEEN, chess.WHITE) | self.pieces(chess.QUEEN, chess.BLACK)
        bishops = self.pieces(chess.BISHOP, chess.WHITE) | self.pieces(chess.BISHOP, chess.BLACK)
        knights = self.pieces(chess.KNIGHT, chess.WHITE) | self.pieces(chess.KNIGHT, chess.BLACK)

        if (queens == 0) or (queens == 2 and bishops + knights <= 1):
            return True
        return False