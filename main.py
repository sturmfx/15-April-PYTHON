import tkinter as tk
import random

root = tk.Tk()
root.title("Лови Фигню")
canvas_width = 400
canvas_height = 600
wood_width = 100
wood_height = 20
circle_size = 20
score = 0
high_score = 0
missed = 0
speed = 5
delta_speed = 2
lives = 3
wood_start_y = canvas_height - wood_height
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="green")
canvas.pack()
wood = canvas.create_rectangle(0, wood_start_y, wood_width, canvas_height, fill="brown")
circle = canvas.create_oval(0, 0, circle_size, circle_size, fill="red")


def spawn_circle():
    global circle
    x = random.randint(0, canvas_width - circle_size)
    y = -circle_size
    canvas.coords(circle, x, y, x + circle_size, y + circle_size)


def move_wood(event):
    x, y = canvas.coords(wood)[:2]
    if event.keysym == 'Left':
        x = x - 10
    elif event.keysym == 'Right':
        x = x + 10
    x = max(min(x, canvas_width - wood_width), 0)
    canvas.coords(wood, x, y, x + wood_width, y + wood_height)


def update_game():
    global score, missed, speed, delta_speed, lives
    wx, wy = canvas.coords(wood)[:2]
    cx, cy = canvas.coords(circle)[:2]

    canvas.move(circle, 0, speed)
    if cy + circle_size >= wy and wx <= cx + circle_size / 2 <= wx + wood_width:
        score = score + 1
        speed = speed + delta_speed
        root.title(f"Счёт: {score}, жизней потрачено: {missed} из {lives}")
        spawn_circle()

    elif cy + circle_size >= canvas_height:
        missed = missed + 1
        root.title(f"Счёт: {score}, жизней потрачено: {missed} из {lives}")
        spawn_circle()
    if missed < lives:
        canvas.after(50, update_game)
    else:
        end_game()


def restart_game(event):
    global score, missed, speed, lives, wood, circle, delta_speed
    score = 0
    missed = 0
    speed = 5
    lives = 3
    delta_speed = 2
    canvas.delete("all")
    wood = canvas.create_rectangle(0, wood_start_y, wood_width, canvas_height, fill="brown")
    circle = canvas.create_oval(0, 0, circle_size, circle_size, fill="red")
    spawn_circle()
    update_game()


def end_game():
    global high_score
    if score > high_score:
        high_score = score
    canvas.create_text(canvas_width / 2, canvas_height / 2, text=f"Игра закончена! Счёт {score}, рекорд: {high_score}",
                       fill="black", font=("Ariel", 10))
    canvas.create_text(canvas_width / 2, canvas_height / 2 + 40, text="Нажмите кнопку мыши чтобы рестрартнутся",
                       fill="black", font=("Ariel", 10))
    canvas.bind("<Button-1>", restart_game)


spawn_circle()
canvas.focus_set()
canvas.bind("<Key>", move_wood)
update_game()
root.mainloop()
