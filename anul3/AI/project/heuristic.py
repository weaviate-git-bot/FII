import chess 

from galapagus import ChessBoard, Evaluator, MoveOrder

class Heuristic:
    def __init__(self, maxDepth = 20, maxTime = -1):
        self.maxDepth = maxDepth
        self.maxTime = maxTime

        self.startTime = -1

    def get_best_move(self, _board: chess.Board):
        board = ChessBoard(fen = _board.fen())
        stockfish = Evaluator()

        print('Starting to find next best move...')
        move_order = MoveOrder(6)
        best_move = move_order.next_best_move(board, stockfish)
        print('Finally, best move is:', best_move, ' with score: ', stockfish.evaluate_board(board), 'after', move_order.nodes, 'nodes')
        return best_move

if __name__ == '__main__':
    board = chess.Board()
    heuristic = Heuristic(5)
    best_move = heuristic.get_best_move(board)