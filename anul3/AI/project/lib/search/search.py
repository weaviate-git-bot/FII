import time
import chess

from lib.board import ChessBoard
from lib.evaluate import CheckBoard

from .transposition import Transposition, Flags
from .score_move import ScoreClassicMove

class Search:
    # max int16
    INFINITY = 32001
    MAX_DEPTH = 60

    def __init__(self, board: ChessBoard):
        self.board = board

        self.nodes = 0 

        self.best_move = None
        self.best_moves = {}
        
        self.pvLength = [0] * self.MAX_DEPTH
        self.pvTable = [[chess.Move.null()] * self.MAX_DEPTH for _ in range(self.MAX_DEPTH)]

        self.transposition = Transposition()
        self.score_move = ScoreClassicMove()

        self.start_time = time.time()
        self.max_time_per_move = 360 # 6 minutes in seconds

        self.hash_history = []

    def should_stop(self):
        return time.time() - self.start_time > self.max_time_per_move

    def get_best_move(self, maxDepth: int, show_debug: bool = False):
        self.start_time = time.time()
        best_move = self.iterative_deepening(maxDepth, -self.INFINITY, self.INFINITY)
        if show_debug:
            print('Nodes searched:', self.nodes, 'Best move:', self.best_move, 'Time:', time.time() - self.start_time)

        return best_move


    def iterative_deepening(self, depth: int, alpha: int, beta: int):
        self.nodes = 0

        score = -self.INFINITY
        best_move = chess.Move.null()

        start_time = time.time()

        # ID loop
        for d in range(1, depth + 1):
            score = self.__absearch(d, alpha, beta)

            best_move = self.pvTable[0][0]

            it_time = max(0.1, time.time() - start_time)
            
            print(f'depth: {d} | score cp: {score:<5} | nodes: {self.nodes:<8} | nps: {self.nodes / it_time:4f} | time: {it_time:2f} | moves: ', end='')
            self.print_list_of_moves()
            print()
            

        if best_move == chess.Move.null():
            best_move = self.pvTable[0][0]
            
        return best_move        

    def __quiescence_search(self, alpha: int, beta: int, ply: int):
        if ply >= self.MAX_DEPTH or self.should_stop():
            return CheckBoard.check_board(self.board)

        current_score = CheckBoard.check_board(self.board)

        if current_score >= beta:
            return current_score
        
        if alpha > current_score:
            alpha = current_score

        moves = sorted(
            self.board.generate_legal_captures(),
            key=lambda move: self.score_move.score_quiescence(self.board, move),
            reverse=True
        )

        for move in moves:
            self.nodes += 1

            self.board.push(move)

            score = -self.__quiescence_search(-beta, -alpha, ply + 1)

            self.board.pop()

            if score <= current_score:
                continue
            
            current_score = score

            if score <= alpha:
                continue
            
            alpha = score
                
            if score >= beta:
                break

        return current_score

    def __mate_distance_rep(self, how_many: int):
        count = 0
        hashed_board = hash(self.board)
        hh_size = len(self.hash_history)

        for i in range(hh_size - 1, -1, 2):
            if i >= hh_size - self.board.halfmove_clock:
                if self.hash_history[i] == hashed_board:
                    count += 1
                
                if count == how_many:
                    return True

        return False

    def __check_mated_in(self, ply: int):
        return ply - (self.INFINITY - 1)
    
    def __check_mate_in(self, ply: int):
        return (self.INFINITY - 1) - ply

    def __absearch(self, depth: int, alpha: int, beta: int, ply: int = 0):
        if ply >= self.MAX_DEPTH or self.should_stop():
            return CheckBoard.check_board(self.board)

        self.pvLength[ply] = ply

        is_start_node = (ply == 0)
        board_hash = hash(self.board)

        if not is_start_node:
            if self.__mate_distance_rep(1):
                return -50

            if self.board.halfmove_clock >= 100:
                return 0

            # mate distance prunning
            alpha = max(alpha, self.__check_mated_in(ply))
            beta = min(beta, self.__check_mate_in(ply + 1))

            if alpha >= beta:
                return alpha

        # quiescence search check
        if depth <= 0:
            return self.__quiescence_search(alpha, beta, ply)

        # TODO: add TT lookup
        tte = self.transposition.probeEntry(board_hash)
        ttHit = board_hash == tte.key
        ttMove = tte.move if ttHit else chess.Move.null()

        ttScore = (
            self.transposition.scoreFromTT(tte.score, ply)
            if ttHit
            else self.INFINITY + 1
        )

        if not is_start_node and tte.depth >= depth and ttHit:
            if tte.flag == Flags.EXACT:
                return ttScore
            elif tte.flag == Flags.LOWER:
                alpha = max(alpha, ttScore)
            elif tte.flag == Flags.UPPER:
                beta = min(beta, ttScore)

            if alpha >= beta:
                return ttScore

        # null move pruning
        if depth >=3 and not self.board.is_check():
            self.board.push(chess.Move.null())

            score = -self.__absearch(depth - 2, -beta, -beta + 1, ply + 1)

            self.board.pop()

            if score >= beta:
                if beta >= self.INFINITY - 1 - 2 * self.MAX_DEPTH:
                    score = beta

                return score

        oldAlpha = alpha
        finished_moves = 0
        best_score = -self.INFINITY

        moves = sorted(
            self.board.legal_moves,
            key=lambda move: self.score_move.score(self.board, move, ttMove),
            reverse=True,
        )

        for move in moves:
            finished_moves += 1
            self.nodes += 1

            self.board.push(move)
            self.hash_history.append(hash(self.board))

            score = -self.__absearch(depth - 1, -beta, -alpha, ply + 1)

            self.board.pop()
            self.hash_history.pop()
            if score <= best_score:
                continue

            best_score = score

            # updating the PV table
            self.pvTable[ply][ply] = move
            for i in range(ply + 1, self.pvLength[ply + 1]):
                self.pvTable[ply][i] = self.pvTable[ply + 1][i]
            
            self.pvLength[ply] = self.pvLength[ply + 1]

            if score <= alpha:
                continue

            alpha = score

            if score >= beta:        
                self.score_move.update(self.board, move, depth)
                break


        if finished_moves == 0:
            if self.board.is_check():
                return ply -self.INFINITY
            else:
                return 0
        
        # compute tt bound and add it to the TT
        bound = Flags.NONE
        if best_score >= beta:
            bound = Flags.LOWER
        else:
            if alpha != oldAlpha:
                bound = Flags.EXACT
            else:
                bound = Flags.UPPER

        if not self.should_stop():
            self.transposition.add_board(self.board, depth, bound, move, best_score, ply)

        return best_score

    def print_list_of_moves(self):
        for i in range(self.pvLength[0]):
            print(self.pvTable[0][i], end=' ')