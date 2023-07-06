import sys
import math
import chess

from time import time
from stockfish import Stockfish

from .chess_board import ChessBoard

STOCKFISH_PATH = '/usr/local/bin/stockfish'

class Evaluator:
    piece_value = {
        chess.PAWN: 10,
        chess.ROOK: 50,
        chess.KNIGHT: 32,
        chess.BISHOP: 33,
        chess.QUEEN: 90,
        chess.KING: 2_000
    }

    TTMOVE_SORT_VALUE = 60;
    MVV_LVA_OFFSET = sys.maxsize - 256

    MVV_LVA = [
        [0, 0, 0, 0, 0, 0, 0],       # victim K, attacker K, Q, R, B, N, P, None
        [50, 51, 52, 53, 54, 55, 0], # victim Q, attacker K, Q, R, B, N, P, None
        [40, 41, 42, 43, 44, 45, 0], # victim R, attacker K, Q, R, B, N, P, None
        [30, 31, 32, 33, 34, 35, 0], # victim B, attacker K, Q, R, B, N, P, None
        [20, 21, 22, 23, 24, 25, 0], # victim N, attacker K, Q, R, B, N, P, None
        [10, 11, 12, 13, 14, 15, 0], # victim P, attacker K, Q, R, B, N, P, None
        [0, 0, 0, 0, 0, 0, 0],       # victim None, attacker K, Q, R, B, N, P, None
    ];

    piece_positions = {
        chess.PAWN: (
            0,  0,  0,  0,  0,  0,  0,  0,
            5, 10, 10, -20, -20, 10, 10,  5,
            5, -5, -10,  0,  0, -10, -5,  5,
            0,  0,  0, 20, 20,  0,  0,  0,
            5,  5, 10, 25, 25, 10,  5,  5,
            10, 10, 20, 30, 30, 20, 10, 10,
            50, 50, 50, 50, 50, 50, 50, 50,
            0, 0, 0, 0, 0, 0, 0, 0
        ),

        chess.KNIGHT: (
            -50, -40, -30, -30, -30, -30, -40, -50,
            -40, -20, 0, 0, 0, 0, -20, -40,
            -30, 0, 10, 15, 15, 10, 0, -30,
            -30, 5, 15, 20, 20, 15, 5, -30,
            -30, 0, 15, 20, 20, 15, 0, -30,
            -30, 5, 10, 15, 15, 10, 5, -30,
            -40, -20, 0, 5, 5, 0, -20, -40,
            -50, -40, -30, -30, -30, -30, -40, -50
        ),

        chess.BISHOP: (
            -20, -10, -10, -10, -10, -10, -10, -20,
            -10, 5, 0, 0, 0, 0, 5, -10,
            -10, 10, 10, 10, 10, 10, 10, -10,
            -10, 0, 10, 10, 10, 10, 0, -10,
            -10, 5, 5, 10, 10, 5, 5, -10,
            -10, 0, 5, 10, 10, 5, 0, -10,
            -10, 0, 0, 0, 0, 0, 0, -10,
            -20, -10, -10, -10, -10, -10, -10, -20
        ),

        chess.ROOK: (
            0, 0, 0, 5, 5, 0, 0, 0,
            -5, 0, 0, 0, 0, 0, 0, -5,
            -5, 0, 0, 0, 0, 0, 0, -5,
            -5, 0, 0, 0, 0, 0, 0, -5,
            -5, 0, 0, 0, 0, 0, 0, -5,
            -5, 0, 0, 0, 0, 0, 0, -5,
            5, 10, 10, 10, 10, 10, 10, 5,
            0, 0, 0, 0, 0, 0, 0, 0
        ),

        chess.QUEEN: (
            -20, -10, -10, -5, -5, -10, -10, -20,
            -10, 0, 0, 0, 0, 0, 0, -10,
            -10, 0, 5, 5, 5, 5, 0, -10,
            -5, 0, 5, 5, 5, 5, 0, -5,
            0, 0, 5, 5, 5, 5, 0, -5,
            -10, 5, 5, 5, 5, 5, 0, -10,
            -10, 0, 5, 0, 0, 0, 0, -10,
            -20, -10, -10, -5, -5, -10, -10, -20
        ),

        chess.KING: (
            20, 30, 10, 0, 0, 10, 30, 20,
            20, 20, 0, 0, 0, 0, 20, 20,
            -10, -20, -20, -20, -20, -20, -20, -10,
            20, -30, -30, -40, -40, -30, -30, -20,
            -30, -40, -40, -50, -50, -40, -40, -30,
            -30, -40, -40, -50, -50, -40, -40, -30,
            -30, -40, -40, -50, -50, -40, -40, -30,
            -30, -40, -40, -50, -50, -40, -40, -30
        ),

        (chess.KING + 1): (
        32,  42,  32,  51, 63,  9,  31,  43,
        27,  32,  58,  62, 80, 67,  26,  44,
        -5,  19,  26,  36, 17, 45,  61,  16,
        -24, -11,   7,  26, 24, 35,  -8, -20,
        -36, -26, -12,  -1,  9, -7,   6, -23,
        -45, -25, -16, -17,  3,  0,  -5, -33,
        -44, -16, -20,  -9, -1, 11,  -6, -71,
        -19, -13,   1,  17, 16,  7, -37, -26,
        ),
    }

    def __init__(self) -> None:
        self.stockfish = Stockfish(STOCKFISH_PATH)
        self.stockfish.set_depth(1)

    def evaluate_board(self, board: ChessBoard) -> None:
        self.stockfish.set_fen_position(board.fen())
        return self.stockfish.get_evaluation().get('value', 0)

    def evaluate_move(self, board: ChessBoard, move: chess.Move, endgame: bool = False) -> float:
        if move.promotion:
            return math.inf * (board.turn == chess.WHITE and 1 or -1)

        piece = board.piece_at(move.from_square)
        if not piece:
            raise Exception('Something went wrong')
        
        from_value = self.__get_piece_value(piece, move.from_square, endgame)
        to_value = self.__get_piece_value(piece, move.to_square, endgame)

        new_pos = to_value - from_value

        capture_value = 0.0
        if board.is_capture(move):
            capture_value = self.evaluate_capture(board, move)
        
        current_move_value = capture_value + new_pos

        return board.turn == chess.BLACK and -current_move_value or current_move_value

    def evaluate_capture(self, board: ChessBoard, move: chess.Move) -> float:
        if board.is_en_passant(move):
            return self.piece_value[chess.PAWN]
        
        from_piece = board.piece_at(move.from_square)
        from_piece = from_piece.piece_type if from_piece else -1
        
        to_piece = board.piece_at(move.to_square)
        to_piece = to_piece.piece_type if to_piece else -1

        return self.piece_value.get(to_piece, 0) - self.piece_value.get(from_piece, 0) + self.MVV_LVA[from_piece][to_piece]

    def __get_piece_value(self, piece: chess.Piece, square: chess.Square, endgame: bool) -> float:
        piece_v = int(piece.piece_type)
        if piece == chess.KING:
            piece_v += int(endgame)

        square_v = square ^ 56 if piece.color == chess.BLACK else square
        return self.piece_positions[piece_v][square_v]
