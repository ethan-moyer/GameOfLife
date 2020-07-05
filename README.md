# GameOfLife
![Demo](/demo.gif?raw=true "Demo")
## What Is This?
An implementation of [Conway's Game of Life ](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) made in Python using raylib-py, numpy, and scipy.
## Installing
### Prerequisites
Ensure that you have these packages installed
```
numpy==1.19.0  
raylib-py==0.1.1  
scipy==1.5.0
```
### Starting the Game
Run `__main__.py`, then you must state your game dimensions and zoom scale (1 being 1px x 1px = 1 cell).
```
> python __main__.py
Game X Size: 100
Game Y Size: 100
Zoom Scale: 5
```
## Controls
Button | Action
------------ | -------------
P | Pause game.
C | Clear grid.
Left Mouse | Draw cells (game must be paused).
Right Mouse | Erase cells (game must be paused).
