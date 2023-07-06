import chess
import math
import sys

from functools import lru_cache
from time import time

from .chess_board import ChessBoard
from .evaluator import Evaluator

class MoveOrder:
    CHECKMATE = 100_000
    THRESHOLD =  9_990
    MAX_KILLERS = 2
    MVV_LVA_OFFSET = sys.maxsize - 256
    KILLER_VALUE = 10

    def __init__(self, maxDepth = 20, maxTime = -1):
        self.maxDepth = maxDepth
        self.maxTime = maxTime

        self.startTime = -1
        self.nodes = 0
        self.__history = [[[0]*64]*64, [[0]*64]*64]

        self.killer_moves = [[0]*maxDepth, [0]*maxDepth]

        self.cached_score = {}
    
    def next_best_move(self, board: ChessBoard, stockfish: 'Evaluator') -> str:
        start_time = time()
        move, value = self.__start_minimax(board, stockfish)

        print(f'Found best move {move} (score: {value}) in {time() - start_time:.4f} seconds.')
        return move

    def __start_minimax(self, board: ChessBoard, stockfish: 'Evaluator') -> str:
        maximize = board.turn == chess.WHITE
        best_move = maximize and -math.inf or math.inf

        moves = self.__order_moves(board, stockfish)
        best_found = moves[0]

        for move in moves:
            print(f'Started {move}, currently at {self.nodes} nodes and best value: {best_move}.')
            board.push(move)
            value = self.__minimax(board, False, self.maxDepth - 1, -math.inf, math.inf, stockfish)
            board.pop()

            if maximize and value >= best_move:
                best_move, best_found = value, move
            elif not maximize and value <= best_move:
                best_move, best_found = value, move
        
        return best_found, best_move

    def __big_pieces(self, board: ChessBoard) -> list:
        k = len(board.pieces(chess.KING, board.turn) | board.pieces(chess.QUEEN, board.turn))
        q = len(board.pieces(chess.KING, board.turn) | board.pieces(chess.QUEEN, board.turn))

        return (k+q) > 0

    def __minimax(self, board: chess.Board, maximizing_player, depth, alfa, beta, stockfish: 'Evaluator') -> int:
        self.nodes += 1

        if board.is_checkmate():
            return maximizing_player and -self.CHECKMATE or self.CHECKMATE

        if board.is_game_over():
            return maximizing_player and 1e10 or 0

        if depth <= 0:
            # return stockfish.evaluate_board(board)
            return 0

        #  null move pruning
        if depth >= 3 and not maximizing_player and not board.is_check() and self.__big_pieces(board) and board.ply():
            board.push(chess.Move.null())
            _d = 2 if depth <= 6 else 3
            value = -self.__minimax(board, not maximizing_player, depth - _d - 1, -beta, -beta + 1, stockfish)
            board.pop()

            if value >= beta:
                print('null move pruning', value, beta)
                return value

        if maximizing_player:
            bestValue = -math.inf
            for move in self.__order_moves(board, stockfish):
                board.push(move)
                value = self.__minimax(board, not maximizing_player, depth - 1, alfa, beta, stockfish)
                board.pop()
                bestValue = max(bestValue, value + (-1 if value > self.THRESHOLD else 1))
                alfa = max(alfa, bestValue)

                if value >= beta and not board.is_capture(move):
                    self.__history[board.turn == chess.WHITE][move.from_square][move.to_square] += depth * depth

                if value >= beta and stockfish.evaluate_capture(board, move):
                    self.__add_killer(board.ply() - 1, move)

                if beta <= alfa:
                    break

            return bestValue
        
        bestValue = math.inf 
        for move in self.__order_moves(board, stockfish):
            board.push(move)
            value = self.__minimax(board, not maximizing_player, depth - 1, alfa, beta, stockfish)
            bestValue = min(bestValue, value + (-1 if value > self.THRESHOLD else 1))

            beta = min(beta, bestValue)
            board.pop()

            if value >= beta and not board.is_capture(move):
                self.__history[board.turn == chess.WHITE][move.from_square][move.to_square] += depth * depth
    
            if value >= beta and stockfish.evaluate_capture(board, move):
                    self.__add_killer(board.ply() - 1, move)


            if beta <= alfa:
                break           
        
        return bestValue

    def __add_killer(self, ply: int, move: chess.Move):
        first_killer = self.killer_moves[0][ply]
        if first_killer == move:
            return
        
        # shift all the move one index upwards
        for i in range(self.MAX_KILLERS - 1, 0, -1):
            prev = self.killer_moves[i - 1][ply]
            self.killer_moves[i][ply] = prev
        
        self.killer_moves[0][ply] = move

    @lru_cache(maxsize=128)
    def __order_moves(self, board: ChessBoard, stockfish: 'Evaluator') -> list:
        def orderer(move:chess.Move):
            # killer moves
            value = - 1
            for i in range(self.MAX_KILLERS):
                if move == self.killer_moves[i][board.ply()]:
                    value = sys.maxsize - 256 - ((i + 1) * self.KILLER_VALUE)

            if value != -1:
                return value

            return self.__history[board.turn == chess.WHITE][move.from_square][move.to_square] \
            + stockfish.evaluate_move(board, move, board.check_end_game())

        s = sorted(
            board.legal_moves,
            key=orderer,
            reverse=board.turn == chess.WHITE
        )
        return s