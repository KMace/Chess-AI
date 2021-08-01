import pygame
from constants import ROWS, COLS, BLACK, WHITE, SQUARE_SIZE
from piece import Piece

class Board:

    def __init__(self):
        self.board = []
        self.white_king = True
        self.black_king = True
        self.create_board()
        self.white_left = self.black_left = 16

    # Can probably do more efficiently
    def create_board(self):
        self.board.append([])
        self.board[0].append(Piece('Rook', 0, 0, BLACK))
        self.board[0].append(Piece('Knight', 0, 1, BLACK))
        self.board[0].append(Piece('Bishop', 0, 2, BLACK))
        self.board[0].append(Piece('Queen', 0, 3, BLACK))
        self.board[0].append(Piece('King', 0, 4, BLACK))
        self.board[0].append(Piece('Bishop', 0, 5, BLACK))
        self.board[0].append(Piece('Knight', 0, 6, BLACK))
        self.board[0].append(Piece('Rook', 0, 7, BLACK))

        self.board.append([])
        for i in range(ROWS):
            self.board[1].append(Piece('Pawn', 1, i, BLACK))
        
        for row in range(2,6):
            self.board.append([])
            for column in range(COLS):
                self.board[row].append(0)
        
        self.board.append([])
        for i in range(ROWS):
            self.board[6].append(Piece('Pawn', 6, i, WHITE))
        
        self.board.append([])
        self.board[7].append(Piece('Rook', 7, 0, WHITE))
        self.board[7].append(Piece('Knight', 7, 1, WHITE))
        self.board[7].append(Piece('Bishop', 7, 2, WHITE))
        self.board[7].append(Piece('Queen', 7, 3, WHITE))
        self.board[7].append(Piece('King', 7, 4, WHITE))
        self.board[7].append(Piece('Bishop', 7, 5, WHITE))
        self.board[7].append(Piece('Knight', 7, 6, WHITE))
        self.board[7].append(Piece('Rook', 7, 7, WHITE))
 
    def draw_squares(self, win):
        win.fill(WHITE)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, BLACK, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def evaluate(self):
        # Let no. pawns = v, no. knights = w, no. bishops = x, no. rooks = y, no. queens = z
        # Therefore return v + 3w + 3x + 5y + 9z
        evaluation = 0
        black_pieces, white_pieces = self.piece_quantities(BLACK), self.piece_quantities(WHITE)
        
        black_evaluation = ((black_pieces['Pawn']) + (3 * black_pieces['Bishop']) + (3 * black_pieces['Knight']) + (5 * black_pieces['Rook']) + (9 * black_pieces['Queen']) + (100000000 * black_pieces['King'])) 
        
        white_evaluation = ((white_pieces['Pawn']) + (3 * white_pieces['Bishop']) + (3 * white_pieces['Knight']) + (5 * white_pieces['Rook']) + (9 * white_pieces['Queen']) + (100000000 * white_pieces['King']))

        evaluation = black_evaluation - white_evaluation

        return evaluation
    
    def get_all_pieces(self, colour):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.colour == colour:
                    pieces.append(piece)
        return pieces
        
    def piece_quantities(self, colour):
        colour_pieces = {'Pawn' : 0, 'Knight' : 0, 'Bishop' : 0, 'Rook' : 0, 'Queen' : 0, 'King' : 0}
        
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.colour == colour:
                    if piece.name == 'Pawn':
                        current_amount = colour_pieces['Pawn']
                        current_amount += 1
                        colour_pieces['Pawn'] = current_amount
                    elif piece.name == 'Knight':
                        current_amount = colour_pieces['Knight']
                        current_amount += 1
                        colour_pieces['Knight'] = current_amount
                    elif piece.name == 'Bishop':
                        current_amount = colour_pieces['Bishop']
                        current_amount += 1
                        colour_pieces['Bishop'] = current_amount
                    elif piece.name == 'Rook':
                        current_amount = colour_pieces['Rook']
                        current_amount += 1
                        colour_pieces['Rook'] = current_amount
                    elif piece.name == 'Queen':
                        current_amount = colour_pieces['Queen']
                        current_amount += 1
                        colour_pieces['Queen'] = current_amount
                    elif piece.name == 'King':
                        current_amount = colour_pieces['King']
                        current_amount += 1
                        colour_pieces['King'] = current_amount
        
        return colour_pieces
    
    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def remove(self, piece):
        if isinstance(piece, tuple):
            row, col = piece
            self.board[row][col] = 0
        else:
            self.board[piece.row][piece.col] = 0
            if piece != 0 and piece.name == 'King':
                if piece.colour == BLACK:
                    self.black_king = False
                else:
                    self.white_king = False
        
        if piece.colour == WHITE:
            self.white_left -= 1
        else:
            self.black_left -= 1
    
    def winner(self):
        if self.black_king == False:
            return WHITE
        elif self.white_king == False:
            return BLACK
            
        return None
    
    def get_piece(self, row, col):
        return self.board[row][col]

    def move(self, piece, row, col):
        #print(piece)
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

    def get_valid_moves(self, piece):
        moves = {}
    
        if piece.name == 'Pawn':
            moves.update(self._pawn_moves(piece))
        
        elif piece.name == 'Rook':
            moves.update(self._rook_moves(piece))

        elif piece.name == 'King':
            moves.update(self._king_moves(piece))

        elif piece.name == 'Bishop':
            moves.update(self._bishop_moves(piece))

        elif piece.name == 'Queen':
            moves.update(self._queen_moves(piece))
        
        elif piece.name == 'Knight':
            moves.update(self._knight_moves(piece))

        return moves

    def _pawn_moves(self, piece):
        moves = {}
        contact = []
        
        if piece.colour == BLACK:
            # Checking if can currently take a piece
            if piece.col != 0:
                if self.get_piece(piece.row + 1, piece.col - 1) != 0:
                    if self.get_piece(piece.row + 1, piece.col - 1).colour == WHITE:
                        moves[(piece.row + 1, piece.col - 1)] = [(piece.row + 1, piece.col - 1)]
            if piece.col != COLS - 1:
                if self.get_piece(piece.row + 1, piece.col + 1) != 0:
                    if self.get_piece(piece.row + 1, piece.col + 1).colour == WHITE:
                        moves[(piece.row + 1, piece.col + 1)] = [(piece.row + 1, piece.col + 1)]

            # Checking movement forward
            if self.get_piece(piece.row + 1, piece.col) == 0:
                moves[(piece.row + 1, piece.col)] = contact
                if self.get_piece(piece.row + 2, piece.col) == 0 and piece.pawn_first_move == True:
                    moves[(piece.row + 2, piece.col)] = contact

        else:
            # Checking if can currently take a piece
            if piece.col != 0:
                if self.get_piece(piece.row - 1, piece.col - 1) != 0:
                    if self.get_piece(piece.row - 1, piece.col - 1).colour == BLACK:
                        moves[(piece.row - 1, piece.col - 1)] = [(piece.row - 1, piece.col - 1)]
            if piece.col != COLS - 1:
                if self.get_piece(piece.row - 1, piece.col + 1) != 0:
                    if self.get_piece(piece.row - 1, piece.col + 1).colour == BLACK:
                        moves[(piece.row - 1, piece.col + 1)] = [(piece.row - 1, piece.col + 1)]

            # Checking movement forward
            if self.get_piece(piece.row - 1, piece.col) == 0:
                moves[(piece.row - 1, piece.col)] = contact
                if self.get_piece(piece.row - 2, piece.col) == 0 and piece.pawn_first_move == True:
                    moves[(piece.row - 2, piece.col)] = contact
        
        return moves

    def _rook_moves(self, piece):
        moves = {}

        if piece.row != 0:
            moves.update(piece.north_attack(piece.row, moves, self.board))
        
        if piece.col != COLS - 1:
            moves.update(piece.east_attack(COLS - piece.col - 1, moves, self.board))

        if piece.row != ROWS - 1:
            moves.update(piece.south_attack(ROWS - piece.row - 1, moves, self.board))

        if piece.col != 0:
            moves.update(piece.west_attack(piece.col, moves, self.board))

        return moves
                
    def _king_moves(self, piece):
        moves = {}
        
        if piece.row != 0:
            moves.update(piece.north_attack(1, moves, self.board))
        
        if piece.row != 0 and piece.col != COLS - 1:
            moves.update(piece.north_east_attack(1, moves, self.board))
        
        if piece.col != COLS - 1:
            moves.update(piece.east_attack(1, moves, self.board))
        
        if piece.row != ROWS - 1 and piece.col != COLS - 1:
            moves.update(piece.south_east_attack(1, moves, self.board))
        
        if piece.row != ROWS - 1:
            moves.update(piece.south_attack(1, moves, self.board))
        
        if piece.row != ROWS - 1 and piece.col != 0:
            moves.update(piece.south_west_attack(1, moves, self.board))
        
        if piece.col != 0:
            moves.update(piece.west_attack(1, moves, self.board))

        if piece.row != 0 and piece.col != 0:
            moves.update(piece.north_west_attack(1, moves, self.board))
            
        return moves
    
    def _bishop_moves(self, piece):
        moves = {}

        if piece.row + piece.col >= ROWS:
            moves.update(piece.north_east_attack(-(piece.col) + (ROWS - 1), moves, self.board))
        else:
            moves.update(piece.north_east_attack(piece.row, moves, self.board))

        if piece.row != ROWS - 1 and piece.col != COLS - 1:
            moves.update(piece.south_east_attack(COLS - max(piece.col, piece.row) - 1, moves, self.board))

        if piece.row + piece.col >= ROWS - 1:
            moves.update(piece.south_west_attack(-(piece.row) + (ROWS - 1), moves, self.board))
        else:
            moves.update(piece.south_west_attack(piece.col, moves, self.board))
        
        if piece.row != 0 and piece.col != 0:
            moves.update(piece.north_west_attack(min(piece.row, piece.col), moves, self.board))

        return moves
                        
    def _queen_moves(self, piece):
        moves = {}
        
        if piece.row != 0:
            moves.update(piece.north_attack(piece.row, moves, self.board))
        
        if piece.row + piece.col >= ROWS:
            moves.update(piece.north_east_attack(-(piece.col) + (ROWS - 1), moves, self.board))
        else:
            moves.update(piece.north_east_attack(piece.row, moves, self.board))

        if piece.col != COLS - 1:
            moves.update(piece.east_attack(COLS - piece.col - 1, moves, self.board))
        
        if piece.row != ROWS - 1 and piece.col != COLS - 1:
            moves.update(piece.south_east_attack(COLS - max(piece.col, piece.row) - 1, moves, self.board))

        if piece.row != ROWS - 1:
            moves.update(piece.south_attack(ROWS - piece.row - 1, moves, self.board))
        
        if piece.row + piece.col >= ROWS - 1:
            moves.update(piece.south_west_attack(-(piece.row) + (ROWS - 1), moves, self.board))
        else:
            moves.update(piece.south_west_attack(piece.col, moves, self.board))

        if piece.col != 0:
            moves.update(piece.west_attack(piece.col, moves, self.board))
        
        if piece.row != 0 and piece.col != 0:
            moves.update(piece.north_west_attack(min(piece.row, piece.col), moves, self.board))

        return moves

    def _knight_moves(self, piece):
        moves = {}

        # 2 north, 1 left
        if piece.col > 0 and piece.row > 1:
            moves.update(piece.knight_north_west(moves, self.board))
        
        # 2 north, 1 right
        if piece.col < COLS - 1 and piece.row > 1:
            moves.update(piece.knight_north_east(moves, self.board))
        
        # 2 east, 1 north
        if piece.row > 0 and piece.col < COLS - 2:
            moves.update(piece.knight_east_north(moves, self.board))

        # 2 east, 1 south
        if piece.row < ROWS - 1 and piece.col < COLS - 2:
            moves.update(piece.knight_east_south(moves, self.board))
            
        # 2 south, 1 east
        if piece.row < ROWS - 2 and piece.col < COLS - 1:
            moves.update(piece.knight_south_east(moves, self.board))

        # 2 south, 1 west
        if piece.row < ROWS - 2 and piece.col > 0:
            moves.update(piece.knight_south_west(moves, self.board))

        # 2 west, 1 south
        if piece.row < ROWS - 1 and piece.col > 1:
            moves.update(piece.knight_west_south(moves, self.board))

        # 2 west, 1 north
        if piece.row > 0 and piece.col > 1:
            moves.update(piece.knight_west_north(moves, self.board))
        
        return moves
