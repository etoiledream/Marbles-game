from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas # 为什么ball有canvas属性?
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 245, 100) 
        starts = [-3, -2, -1, 1, 2, 3] # 为什么是这六个数？
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id) # get the position of the ball with id, return [x1, y1, x2, y2]
        # the ball touch the top of the canvas
        if pos[1] <= 0: 
            self.y = 3
        # the ball touch the bottom of the canvas
        if pos[3] >= self.canvas_height:
            self.y = -3
        # the ball touch the left border
        if pos[0] <= 0:
            self.x = 3
        # the ball touch the right border
        if pos[2] >= self.canvas_width:
            self.x = -3

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 250) # move 10 pix along x, move 10 pix along y
        self.canvas_width = self.canvas.winfo_width()
        self.x = 3
        self.y = 0

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

tk = Tk()
tk.title('Game')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update() # tk.update作用？

#ball_color = colorchooser.askcolor()
ball = Ball(canvas, 'red')
paddle = Paddle(canvas, 'blue')

while True:
    ball.draw()
    paddle.draw()
    tk.update_idletasks() # 作用？
    tk.update()
    time.sleep(0.01)