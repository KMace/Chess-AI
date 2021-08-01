import pygame

WIDTH, HEIGHT = 700, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS
PIECE_SIZE = (int(SQUARE_SIZE / 1.5), int(SQUARE_SIZE / 1.5))

BLACK, WHITE = (0, 0, 0), (255, 255, 255)
BLUE = (0, 0, 255)
ORANGE = (255, 128, 0)

CONTACT = []

W_PAWN = pygame.transform.scale(pygame.image.load('Assets/white_pawn.png'), (PIECE_SIZE))
W_ROOK = pygame.transform.scale(pygame.image.load('Assets/white_rook.png'), (PIECE_SIZE))
W_KNIGHT = pygame.transform.scale(pygame.image.load('Assets/white_knight.png'), (PIECE_SIZE))
W_BISHOP = pygame.transform.scale(pygame.image.load('Assets/white_bishop.png'), (PIECE_SIZE))
W_QUEEN = pygame.transform.scale(pygame.image.load('Assets/white_queen.png'), (PIECE_SIZE))
W_KING = pygame.transform.scale(pygame.image.load('Assets/white_king.png'), (PIECE_SIZE))

B_PAWN = pygame.transform.scale(pygame.image.load('Assets/black_pawn.png'), (PIECE_SIZE))
B_ROOK = pygame.transform.scale(pygame.image.load('Assets/black_rook.png'), (PIECE_SIZE))
B_KNIGHT = pygame.transform.scale(pygame.image.load('Assets/black_knight.png'), (PIECE_SIZE))
B_BISHOP = pygame.transform.scale(pygame.image.load('Assets/black_bishop.png'), (PIECE_SIZE))
B_QUEEN = pygame.transform.scale(pygame.image.load('Assets/black_queen.png'), (PIECE_SIZE))
B_KING = pygame.transform.scale(pygame.image.load('Assets/black_king.png'), (PIECE_SIZE))

PIECES = [W_PAWN, W_ROOK, W_KNIGHT, W_BISHOP, W_QUEEN,
          W_KING, B_PAWN, B_ROOK, B_KNIGHT, B_BISHOP, B_QUEEN, B_KING]
