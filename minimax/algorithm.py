from copy import deepcopy
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def minimax(position, depth, max_player, game, alpha, beta):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position
    
    if max_player:
        best_move = None
        for move in get_all_moves(position, BLACK, game):
            evaluation = minimax(move, depth - 1, False, game, alpha, beta)[0]
            if evaluation > alpha:
                alpha = evaluation
                best_move = move
                if alpha >= beta:
                    break
        
        return alpha, best_move
        
    else:
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth - 1, True, game, alpha, beta)[0]
            if evaluation < beta:
                beta = evaluation
                best_move = move
                if alpha >= beta:
                    break

        return beta, best_move

def simulate_move(piece, move, board, game, skip):
    if piece != 0:
        if skip != []:
            piece_to_remove = board.get_piece(move[0], move[1])
            board.remove(piece_to_remove)
            
        board.move(piece, move[0], move[1])
    
    return board

def get_all_moves(board, colour, game):
    moves = []

    for piece in board.get_all_pieces(colour):        
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():

            # If you un-hash the subsequent code, you can see a 
            # visual representation of what the AI is calculating

            #draw_moves(game, board, piece)
            
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)

    return moves

def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0, 255, 0), (piece.x, piece.y), 25, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
