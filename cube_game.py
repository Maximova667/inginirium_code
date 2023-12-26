import random
import tkinter as tk


def move_player(event):
    if event.keysym == 'w':
        canvas.move(player, 0, -20)
    if event.keysym == 'a':
        canvas.move(player, -20, 0)
    if event.keysym == 's':
        canvas.move(player, 0, 20)
    if event.keysym == 'd':
        canvas.move(player, 20, 0)


def create_point():
    global point
    point_pos = (random.randint(1, 580), random.randint(1, 580))
    point = canvas.create_oval(point_pos[0], point_pos[1], point_pos[0] + 80, point_pos[1] + 80, fill='#f28507')


def restart_game():
    global canvas, player, point
    start_pos = (random.randint(1, 580), random.randint(1, 580))
    player = canvas.create_rectangle(start_pos[0], start_pos[1], start_pos[0] + 80, start_pos[1] + 80, fill='#75ff42')
    restart_bt.config(state="disabled")
    create_point()


root = tk.Tk()
root.title = 'My game'
root.geometry('640x640')

label_score = tk.Label(root, text='Welcome!')
restart_bt = tk.Button(root, text='start new game', command=restart_game)
canvas = tk.Canvas(root, width=640, height=640, bg="#42b0ff")

player = ""
point = ""
label_score.pack()
restart_bt.pack()
canvas.pack()
root.bind('<KeyPress>', move_player)
root.mainloop()
