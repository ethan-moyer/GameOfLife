import os
from raylibpy import *
from game import Game

def main():
    init_window(500, 500, "Game of Life")
    set_target_fps(60)

    game = Game(100, 100)
    game.cycle()

    while not window_should_close():
        begin_drawing()
        clear_background(BLACK)
        for row in range(game.grid.shape[0]):
            for col in range(game.grid.shape[1]):
                if game.grid[row,col] == 1:
                    draw_rectangle(col*5, row*5, 5, 5, WHITE)
                else:
                    draw_rectangle(col*5, row*5, 5, 5, BLACK)
        end_drawing()

        game.cycle()
    
    close_window()

if __name__ == "__main__":
    main()