import pygame
from constants import SQUARE_SIZE, WIN, BLACK, WHITE, W_KING, B_PAWN, B_ROOK, B_KNIGHT, B_BISHOP, B_QUEEN, B_KING, W_PAWN, W_ROOK, W_KNIGHT, W_BISHOP, W_QUEEN, CONTACT

class Piece:

    def __init__(self, name, row, col, colour):
        self.name = name
        self.row = row
        self.col = col
        self.colour = colour
        self.enemy_colour = self.get_enemy_colour(colour)
        if name == 'Pawn':
            self.pawn_first_move = True
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE / 5.3
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE / 3

    def move(self, row, col):
        self.row = row
        self.col = col
        self.pawn_first_move = False
        self.calc_pos()    

    def get_enemy_colour(self, colour):
        if colour == WHITE:
            return BLACK
        return WHITE

    def draw(self, win):
        if self.name == 'Pawn':
            if self.colour == BLACK:
                WIN.blit(B_PAWN, (self.x, self.y))
            else:
                WIN.blit(W_PAWN, (self.x, self.y))
        elif self.name == 'Rook':
            if self.colour == BLACK:
                WIN.blit(B_ROOK, (self.x, self.y))
            else:
                WIN.blit(W_ROOK, (self.x, self.y))
        elif self.name == 'Knight':
            if self.colour == BLACK:
                WIN.blit(B_KNIGHT, (self.x, self.y))
            else:
                WIN.blit(W_KNIGHT, (self.x, self.y))
        elif self.name == 'Bishop':
            if self.colour == BLACK:
                WIN.blit(B_BISHOP, (self.x, self.y))
            else:
                WIN.blit(W_BISHOP, (self.x, self.y))
        elif self.name == 'Queen':
            if self.colour == BLACK:
                WIN.blit(B_QUEEN, (self.x, self.y))
            else:
                WIN.blit(W_QUEEN, (self.x, self.y))
        elif self.name == 'King':
            if self.colour == BLACK:
                WIN.blit(B_KING, (self.x, self.y))
            else:
                WIN.blit(W_KING, (self.x, self.y))

    def north_attack(self, stop, moves, board):
        row = self.row
        col = self.col

        for i in range(stop):
            if board[row - 1][col] != 0: 
                if board[row - 1][col].colour == self.colour:
                    break
                else:
                    moves[(row - 1, col)] = [(row - 1, col)]
                    break
                        
            if board[row - 1][col] == 0:
                moves[(row - 1, col)] = CONTACT
            row -= 1

        return moves
    
    def north_east_attack(self, stop, moves, board):
        row = self.row
        col = self.col

        for i in range(stop):
            if board[row - 1][col + 1] != 0:
                if board[row - 1][col + 1].colour == self.colour:
                    break
                else:
                    moves[(row - 1, col + 1)] = [(row - 1, col + 1)]
                    break

            if board[row - 1][col + 1] == 0:
                moves[(row - 1, col + 1)] = CONTACT
            row -= 1
            col += 1
        return moves

    def east_attack(self, stop, moves, board):
        row = self.row
        col = self.col

        for i in range(stop):
            if board[row][col + 1] != 0: 
                if board[row][col + 1].colour == self.colour:
                    break
                else:
                    moves[(row, col + 1)] = [(row, col + 1)]
                    break
                    
            if board[row][col + 1] == 0:
                moves[(row, col + 1)] = CONTACT
            col += 1
        return moves
    
    def south_east_attack(self, stop, moves, board):
        row = self.row
        col = self.col

        for i in range(stop):
            if board[row + 1][col + 1] != 0: 
                if board[row + 1][col + 1].colour == self.colour:
                    break
                else:
                    moves[(row + 1, col + 1)] = [(row + 1, col + 1)]
                    break
            if board[row + 1][col + 1] == 0:
                moves[(row + 1, col + 1)] = CONTACT
            row += 1
            col += 1
        return moves
    
    def south_attack(self, stop, moves, board):
        row = self.row
        col = self.col

        for i in range(stop):
            if board[row + 1][col] != 0: 
                if board[row + 1][col].colour == self.colour:
                    break
                else:
                    moves[(row + 1, col)] = [(row + 1, col)]
                    break
            if board[row + 1][col] == 0:
                moves[(row + 1, col)] = CONTACT
            row += 1
        return moves
    
    def south_west_attack(self, stop, moves, board):
        row = self.row
        col = self.col

        for i in range(stop):
            if board[row + 1][col - 1] != 0: 
                if board[row + 1][col - 1].colour == self.colour:
                    break
                else:
                    moves[(row + 1, col - 1)] = [(row + 1, col - 1)]
                    break
            if board[row + 1][col - 1] == 0:
                moves[(row + 1, col - 1)] = CONTACT
            row += 1
            col -= 1
        return moves

    def west_attack(self, stop, moves, board):
        row = self.row
        col = self.col

        for i in range(stop):
            if board[row][col - 1] != 0: 
                if board[row][col - 1].colour == self.colour:
                    break
                else:
                    moves[(row, col - 1)] = [(row, col - 1)]
                    break
            if board[row][col - 1] == 0:
                moves[(row, col - 1)] = CONTACT
            col -= 1
        return moves

    def north_west_attack(self, stop, moves, board):
        row = self.row
        col = self.col

        for i in range(stop):
            if board[row - 1][col - 1] != 0: 
                if board[row - 1][col - 1].colour == self.colour:
                    break
                else:
                    moves[(row - 1, col - 1)] = [(row - 1, col - 1)]
                    break
            if board[row - 1][col - 1] == 0:
                moves[(row - 1, col - 1)] = CONTACT
            row -= 1
            col -= 1
        return moves
    
    def knight_north_west(self, moves, board):
        row = self.row
        col = self.col

        if board[row - 2][col - 1] != 0:
            if board[row - 2][col - 1].colour == self.enemy_colour:
                moves[(row - 2, col - 1)] = [(row - 2, col - 1)]
        else:
            moves[(row - 2, col - 1)] = CONTACT

        return moves
    
    def knight_north_east(self, moves, board):
        row = self.row
        col = self.col

        if board[row - 2][col + 1] != 0:
            if board[row - 2][col + 1].colour == self.enemy_colour:
                moves[(row - 2, col + 1)] = [(row - 2, col + 1)]
        else:
            moves[(row - 2, col + 1)] = CONTACT

        return moves
    
    def knight_east_north(self, moves, board):
        row = self.row
        col = self.col

        if board[row - 1][col + 2] != 0:
            if board[row - 1][col + 2].colour == self.enemy_colour:
                moves[(row - 1, col + 2)] = [(row - 1, col + 2)]
        else:
            moves[(row - 1, col + 2)] = CONTACT

        return moves
    
    def knight_east_south(self, moves, board):
        row = self.row
        col = self.col

        if board[row + 1][col + 2] != 0:
            if board[row + 1][col + 2].colour == self.enemy_colour:
                moves[(row + 1, col + 2)] = [(row + 1, col + 2)]
        else:
            moves[(row + 1, col + 2)] = CONTACT

        return moves
    
    def knight_south_east(self, moves, board):
        row = self.row
        col = self.col

        if board[row + 2][col + 1] != 0:
            if board[row + 2][col + 1].colour == self.enemy_colour:
                moves[(row + 2, col + 1)] = [(row + 2, col + 1)]
        else:
            moves[(row + 2, col + 1)] = CONTACT

        return moves
    
    def knight_south_west(self, moves, board):
        row = self.row
        col = self.col

        if board[row + 2][col - 1] != 0:
            if board[row + 2][col - 1].colour == self.enemy_colour:
                moves[(row + 2, col - 1)] = [(row + 2, col - 1)]
        else:
            moves[(row + 2, col - 1)] = CONTACT

        return moves

    def knight_west_south(self, moves, board):
        row = self.row
        col = self.col

        if board[row + 1][col - 2] != 0:
            if board[row + 1][col - 2].colour == self.enemy_colour:
                moves[(row + 1, col - 2)] = [(row + 1, col - 2)]
        else:
            moves[(row + 1, col - 2)] = CONTACT

        return moves

    def knight_west_north(self, moves, board):
        row = self.row
        col = self.col

        if board[row - 1][col - 2] != 0:
            if board[row - 1][col - 2].colour == self.enemy_colour:
                moves[(row - 1, col - 2)] = [(row - 1, col - 2)]
        else:
            moves[(row - 1, col - 2)] = CONTACT

        return moves
