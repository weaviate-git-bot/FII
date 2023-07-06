import os
import random
import chess
import chess.engine
import threading
from stockfish import Stockfish

from lib.board import ChessBoard

STOCKFISH_PATH = "/usr/local/bin/stockfish"

class Game:
    _inst = None
    _inited = False

    def __new__(cls):
        if cls._inst is None:
            cls._inst = super().__new__(cls)
        return cls._inst

    def __init__(self):
        if type(self)._inited:
            return
        
        
        self.board = ChessBoard()
        self.lock = threading.Lock()
        self.best_move_used_stockfish = False
        self.stockfish_lock = threading.Lock()
        type(self)._inited = True

    def push_chess_move(self, move: chess.Move):
        with self.lock:
            self.board.push(move)

    def push_move(self, move: str):
        with self.lock:
            self.board.push(chess.Move.from_uci(move))

    def get_stockfish_move(self, timeLimit=0.1):
        if self.board.is_checkmate():
            raise Exception('Game is over')

        self.engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)
        stockfish_move = self.engine.analyse(chess.Board(self.board.fen()), chess.engine.Limit(time=timeLimit))
        self.engine.close()
        return stockfish_move["pv"][0]  #stockfish's first choice

        # print('stockfish_move', stockfish_move)
        # m_len = len(stockfish_move["pv"])
        # if m_len < 2:
        #     return stockfish_move["pv"][0]

        # if not self.best_move_used_stockfish:
        #     self.best_move_used_stockfish = True
        #     return stockfish_move["pv"][0]
        # m_len = m_len - random.randint(1, m_len // 2)
        # stockfish_m_poz = m_len - (m_len % 2 == 1)


    def get_board(self):
        return self.board

    def print_board(self):  #for debugging
        print(self.board, "\n")

    def get_move_history(self):
        move_history = []
        for move in self.board.move_stack:
            move_history.append(move.uci())
        return move_history

    def result(self):
        return self.board.result()

    def end(self):
        pass

