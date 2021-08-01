import pygame
from game import Game
from constants import WIDTH, HEIGHT, SQUARE_SIZE, WIN, WHITE, BLACK
from minimax.algorithm import minimax

pygame.display.set_caption("Chess")
FPS = 60

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

##################################################
# Still need to implement following functionality:
# 
# Check
# Checkmate
# Castles
# Pawn promotion to a rook, bishop, queen
##################################################

def main():
    difficultyChosen = False
    while not difficultyChosen:
        setting = int(input("Select a difficulty: \n1) Beginner\n2) Intermediate\n3) Expert\n"))
        print()
        if setting == 1 or setting == 2 or setting == 3:
            setting += 2
            print("Loading game!...")
            difficultyChosen = True
        else:
            print()
            print("Please type either 1, 2 or 3")
            print()

    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)
        
        if game.turn == BLACK:
            value, new_board = minimax(game.get_board(), 3, True, game, float('-inf'), float('inf'))
            game.ai_move(new_board)
        
        if game.winner() != None:
            if game.winner() == WHITE:
                print("White wins!")
            else:
                print("Black wins!")
            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)        
        
        game.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()
