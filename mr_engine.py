import time
from textwrap import wrap
import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageTk

#TODO: Add comments
app = tk.Tk()
app.title("Maze Runner")

game_speed = 1.0
tracking = False
maze = []

runner_up_img = Image.open("gfx/zorda_up.png")
runner_down_img = Image.open("gfx/zorda_down.png")
runner_left_img = Image.open("gfx/zorda_left.png")
runner_right_img = Image.open("gfx/zorda_right.png")
runner = ImageTk.PhotoImage(runner_up_img)
runner_pos_x = 0
runner_pos_y = 0

wall_img = Image.open("gfx/wall.png")
wall = ImageTk.PhotoImage(wall_img)

way_img = Image.open("gfx/way.png")
way = ImageTk.PhotoImage(way_img)

track_img = Image.open("gfx/tracker.png")
track = ImageTk.PhotoImage(track_img)

finish_img = Image.open("gfx/finish.png")
finish = ImageTk.PhotoImage(finish_img)

finish_pos_x = -1
finish_pos_y = -1

size_x = 0
size_y = 0
block_size = 50
direction = 'u'
canvas = Canvas(app)


def load_maze(level):
    global size_x, size_y
    maze_file = open(level, "r")

    for line in maze_file:
        maze_row = wrap(line, 1)
        maze.append(maze_row)
    size_x = len(maze[0]) * block_size
    size_y = len(maze) * block_size

    canvas.configure(width=size_x, height=size_y)


def create_tile(pos_x, pos_y, image):
    canvas.create_image(pos_x * block_size + (block_size * 0.5), pos_y * block_size + (block_size * 0.5), image=image)


def draw_block(pos_x, pos_y):
    create_tile(pos_x, pos_y, wall)


def draw_finish(pos_x, pos_y):
    create_tile(pos_x, pos_y, way)
    create_tile(pos_x, pos_y, finish)


def draw_way(pos_x, pos_y):
    create_tile(pos_x, pos_y, way)


def draw_track(pos_x, pos_y):
    create_tile(pos_x, pos_y, track)


def draw_player(pos_x, pos_y):
    create_tile(pos_x, pos_y, runner)


def turn_right():
    global runner, direction

    if direction == 'u':
        direction = 'r'
        runner = ImageTk.PhotoImage(runner_right_img)
    elif direction == 'r':
        direction = 'd'
        runner = ImageTk.PhotoImage(runner_down_img)
    elif direction == 'd':
        direction = 'l'
        runner = ImageTk.PhotoImage(runner_left_img)
    elif direction == 'l':
        direction = 'u'
        runner = ImageTk.PhotoImage(runner_up_img)

    print(f"Runner facing: {direction}")
    draw()


def not_facing_wall():
    if direction == 'u' and maze[runner_pos_y - 1][runner_pos_x] == "#":
        return False
    elif direction == 'd' and maze[runner_pos_y + 1][runner_pos_x] == "#":
        return False
    elif direction == 'l' and maze[runner_pos_y][runner_pos_x - 1] == "#":
        return False
    elif direction == 'r' and maze[runner_pos_y][runner_pos_x + 1] == "#":
        return False
    return True


def move():
    global maze, runner_pos_y, runner_pos_x, tracking

    way_symbol = "_"
    if tracking:
        way_symbol = "-"

    if not_facing_wall():
        maze[runner_pos_y][runner_pos_x] = way_symbol
        if direction == 'u':
            runner_pos_y -= 1
        elif direction == 'd':
            runner_pos_y += 1
        elif direction == 'r':
            runner_pos_x += 1
        elif direction == 'l':
            runner_pos_x -= 1
        maze[runner_pos_y][runner_pos_x] = "P"

    print(f"Runner at {runner_pos_x}, {runner_pos_y} - Treasure at {finish_pos_x}, {finish_pos_y}")
    draw()


def finished():
    global runner_pos_x, runner_pos_y, finish_pos_x, finish_pos_y
    if runner_pos_y == finish_pos_y and runner_pos_x == finish_pos_x:
        return True
    return False


def draw():
    global runner_pos_x, runner_pos_y, finish_pos_x, finish_pos_y, game_speed
    canvas.delete("all")
    pos_y = 0
    for row in maze:
        pos_x = 0
        for block in row:
            if block == "#":
                draw_block(pos_x, pos_y)
            elif block == "_" or block == "-":
                draw_way(pos_x, pos_y)
                if block == "-":
                    draw_track(pos_x, pos_y)
            elif block == "Z":
                draw_finish(pos_x, pos_y)
                finish_pos_y = pos_y
                finish_pos_x = pos_x
            elif block == "P":
                runner_pos_x = pos_x
                runner_pos_y = pos_y
                draw_way(pos_x, pos_y)
                draw_player(pos_x, pos_y)
            pos_x += 1
        pos_y += 1
    time.sleep(0.02 / game_speed)
    app.update()


def start(level, speed, enable_tracking=False):
    global game_speed, tracking
    tracking = enable_tracking
    game_speed = speed
    load_maze(level)
    canvas.pack(fill="both", expand=True)
    draw()
