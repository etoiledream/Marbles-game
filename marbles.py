from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, paddle, color):
        self.score = 0
        self.canvas = canvas
        self.paddle = paddle
        self.hit_bottom = False
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 245, 100)
        # random start speed and direction
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -2
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        # get the position of the ball with id, return [x1, y1, x2, y2]
        pos = self.canvas.coords(self.id)
        # the ball touch the top of the canvas
        if pos[1] <= 0: 
            self.y = 2
        # the ball touch the bottom of the canvas, game over
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        # the ball hit the paddle, y direction turn round and get one score, the speed increases as paddle
        if self.hit_paddle(pos) == True:
            self.score += 1
            self.y = -1 * abs(self.paddle.x)
        # the ball touch the left border
        if pos[0] <= 0:
            self.x = 2
        # the ball touch the right border
        if pos[2] >= self.canvas_width:
            self.x = -2

    def hit_paddle(self, pos):
        paddle_pos = self.paddle.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                return True
        return False

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 250) # move 10 pix along x, move 10 pix along y
        self.canvas_width = self.canvas.winfo_width()
        self.x = 4
        self.y = 0
        # bind event
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        # stop when touching the border
        if pos[0] <= 0:
            self.x = 4
        if pos[2] >= self.canvas_width:
            self.x = -4

    def turn_left(self, evt):
        self.x = -4

    def turn_right(self, evt):
        self.x = 4

tk = Tk()
tk.title('Game')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')

score_text = canvas.create_text(430, 10, text='score : %d' % ball.score, font=('Courier', 10))

while True:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    else:
        canvas.create_text(250, 200, text='Lost! Score is %d' % ball.score, fill='red', font=('Courier', 20))
    # update the score
    canvas.itemconfig(score_text, text='score : %d' % ball.score)
    tk.update()
    time.sleep(0.01)