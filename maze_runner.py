from mr_engine import *


def complex_solution():
    while not finished():
        turn_right()
        if not_facing_wall():
            move()
        else:
            turn_left()

        if not_facing_wall():
            move()
        else:
            turn_left()
            move()


def complex_solution():
    while not finished():
        turn_right()
        if not_facing_wall():
            move()
        else:
            turn_left()

        if not_facing_wall():
            move()
        else:
            turn_left()
            move()


def easy_solution():
    right_turns = 0
    while not finished():
        if right_turns == 2:
            turn_right()
        if not_facing_wall():
            right_turns = 0
            move()
        else:
            right_turns += 1
            turn_right()


def turn_left():
    turn_right()
    turn_right()
    turn_right()


def solve_maze_1():
    move()
    move()
    move()
    turn_right()
    move()
    move()
    move()
    move()
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()
    move()
    move()
    move()
    turn_left()
    move()
    move()
    turn_right()
    move()
    move()
    move()
    move()
    turn_right()
    move()
    move()
    move()
    move()
    turn_right()
    move()
    move()
    move()
    move()


def playground():
    turn_right()

    move()
    move()
    move()
    turn_left()
    move()
    move()
    move()
    turn_left()
    move()
    move()
    move()


def playground_loop():
    # it 3
    going_up = True

    # it 2
    while not finished():
        # it 1
        while not_facing_wall():
            move()
        if going_up:
            turn_right()
            move()
            turn_right()
            going_up = False
        else:
            turn_left()
            move()
            turn_left()
            going_up = True


def solve_maze():
    playground_loop()


start(level="level/playground.txt", speed=0.5, enable_tracking=True)
solve_maze()
app.mainloop()
