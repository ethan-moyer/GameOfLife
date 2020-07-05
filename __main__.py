import os
from raylibpy import *
from game import Game

def main(x1, y1, zoom, seed=None):
    init_window(x1 * zoom, y1 * zoom, "Game of Life")
    set_target_fps(60)

    game = Game(x1, y1)
    pause = False
    mouse_pos = [0, 0]

    while not window_should_close():
        #Drawing
        begin_drawing()
        for row in range(game.grid.shape[0]):
            for col in range(game.grid.shape[1]):
                if game.grid[row,col] == 1:
                    draw_rectangle(col*zoom, row*zoom, zoom, zoom, WHITE)
                else:
                    draw_rectangle(col*zoom, row*zoom, zoom, zoom, BLACK)
        end_drawing()

        #Inputs
        if is_key_pressed(KEY_P):
            pause = not pause
        if is_key_pressed(KEY_C):
            game.clear()

        mouse_pos[0] = min(max(0, get_mouse_position()[0]), 499)
        mouse_pos[1] = min(max(0, get_mouse_position()[1]), 499)
        grid_pos_x = int(mouse_pos[0] / zoom)
        grid_pos_y = int(mouse_pos[1] / zoom)

        if is_mouse_button_down(0) and pause:
            game.grid[grid_pos_y,grid_pos_x] = 1
        if is_mouse_button_down(1) and pause:
            game.grid[grid_pos_y,grid_pos_x] = 0

        #Run Game
        if not pause:
            game.cycle()
            
    close_window()

if __name__ == "__main__":
    game_x = int(input("Game X Size: "))
    game_y = int(input("Game Y Size: "))
    zoom = int(input("Zoom Scale: "))
    main(game_x, game_y, zoom)