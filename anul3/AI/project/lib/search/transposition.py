import chess

from lib.board import ChessBoard

VALUE_INFINITE = 32001
VALUE_NONE = 32002
VALUE_MATE = 32000
MAX_PLY = 64

VALUE_MATE_IN_PLY = VALUE_MATE - MAX_PLY
VALUE_MATED_IN_PLY = -VALUE_MATE_IN_PLY

# Theres no TB support but it useful for other people who port this to another language to respect the TB value ranges
VALUE_TB_WIN = VALUE_MATE_IN_PLY
VALUE_TB_LOSS = -VALUE_TB_WIN
VALUE_TB_WIN_IN_MAX_PLY = VALUE_TB_WIN - MAX_PLY
VALUE_TB_LOSS_IN_MAX_PLY = -VALUE_TB_WIN_IN_MAX_PLY

class Flags:
    NONE    = 0
    EXACT   = 1
    LOWER   = 2
    UPPER   = 3

class Entry:
    def __init__(self, key = 0, depth = 0, flag = 0, score = 0, move = chess.Move.null()):
        self.key = key
        self.depth = depth
        self.flag = flag
        self.score = score
        self.move = move

class Transposition:
    def __init__(self):
        self.tt_size = 2**19 - 1
        self.transposition_table = [Entry() for _ in range(self.tt_size)]


    def add_board(self, board: 'ChessBoard', depth: int, flag: Flags, move: chess.Move, score: int, ply: int):
        key = hash(board)

        index = self.ttIndex(key)
        entry = self.transposition_table[index]

        # Replacement schema
        if entry.key != key or entry.move != move:
            entry.move = move

        if entry.key != key or flag == Flags.EXACT or depth + 4 > entry.depth:
            entry.depth = depth
            entry.score = self.scoreToTT(score, ply)
            entry.key = key
            entry.flag = flag

    def ttIndex(self, key: int) -> int:
        return key % self.tt_size

    def probeEntry(self, key: int) -> Entry:
        index = self.ttIndex(key)
        entry = self.transposition_table[index]

        return entry

    # if we want to save correct mate scores we have to adjust the distance
    def scoreToTT(self, s: int, plies: int) -> int:
        if s >= VALUE_TB_WIN_IN_MAX_PLY:
            return s + plies
        else:
            if s <= VALUE_TB_LOSS_IN_MAX_PLY:
                return s - plies
            else:
                return s

    # undo the previous adjustment
    def scoreFromTT(self, s: int, plies: int) -> int:
        if s >= VALUE_TB_WIN_IN_MAX_PLY:
            return s - plies
        else:
            if s <= VALUE_TB_LOSS_IN_MAX_PLY:
                return s + plies
            else:
                return s