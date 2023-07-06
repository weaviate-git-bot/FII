import chess

from lib.board import ChessBoard

class ScoreClassicMove:
    MVV_LVA = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 105.0, 104.0, 103.0, 102.0, 101.0, 100.0],
        [0, 205.0, 204.0, 203.0, 202.0, 201.0, 200.0],
        [0, 305.0, 304.0, 303.0, 302.0, 301.0, 300.0],
        [0, 405.0, 404.0, 403.0, 402.0, 401.0, 400.0],
        [0, 505.0, 504.0, 503.0, 502.0, 501.0, 500.0],
        [0, 605.0, 604.0, 603.0, 602.0, 601.0, 600.0],
    ]


    def __init__(self):
        self.history_table = [[[0]*64]*64, [[0]*64]*64]

    def mvv_lva(self, board: ChessBoard, move: chess.Move):
        if board.is_en_passant(move):
            return 1
        
        from_piece = board.piece_type_at(move.from_square)
        to_piece = board.piece_type_at(move.to_square)

        return self.MVV_LVA[from_piece][to_piece]

    def score_quiescence(self, board: ChessBoard, move: chess.Move):
        return self.mvv_lva(board, move)

    def score(self, board: ChessBoard, move: chess.Move, tt_move: chess.Move):
        if move == tt_move:
            return 1_000_000

        if board.is_capture(move):
            return 32_000 + self.mvv_lva(board, move)

        return self.history_table[board.turn][move.from_square][move.to_square]

    def update(self, board: ChessBoard, move: chess.Move, depth: int):
        if board.is_capture(move):
            return
        
        bonus = depth * depth
        self.history_table[board.turn][move.from_square][move.to_square] += (
            bonus 
            - self.history_table[board.turn][move.from_square][move.to_square] * abs(bonus) / 16384
        )
