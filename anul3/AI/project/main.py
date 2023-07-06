import http.client
import json
import chess

from lib.utils import get_random_string
from lib.search import Search
from game import Game

SEND_AND_SAVE = True

def send_and_save(board, moves, err):
    data = {
        'board_fen': board.pgn()
        'moves': [f'{move[0]} {move[1]}' for move in moves],
        'total_moves': len(moves),
        'error': str(err)
    }

    msg = json.dumps(data, indent=4)
    with open(f'games/{len(moves)}_{get_random_string(16)}.json', 'w') as f:
        f.write(msg)

    conn = http.client.HTTPSConnection('eolimjef0tjdlts.m.pipedream.net')
    conn.request("POST", f"/game/1", msg, {'Content-Type': 'application/json'})


def game():
    game = Game()

    board = game.get_board()
    game.push_move('e2e4')
    game.push_move('a7a6')
    err = None
    moves = [
        (chess.Move.from_uci('e2e4'), chess.Move.from_uci('a7a6')),
    ]
    
    # best_moves = ['b1c3', 'f1a6', 'g1f3']

    try:
        while not board.is_game_over(claim_draw = True):
            # our move
            # best_move = chess.Move.from_uci(best_moves.pop(0))
            best_move = Search(board).get_best_move(maxDepth = 5, show_debug=False)
            print('Best move is:', best_move)
            game.push_chess_move(best_move)
            
            stockfish_move = game.get_stockfish_move(0.5)
            print('Stockfish move is:', stockfish_move)
            game.push_chess_move(stockfish_move)

            moves.append((best_move, stockfish_move))
    except Exception as e:
        import traceback
        print('Something crashed') 
        print(traceback.format_exc())
        err = e
    finally:
        if SEND_AND_SAVE:
            send_and_save(board, moves, err)

        game.print_board()
        game.end()

if __name__ == '__main__':
    game()