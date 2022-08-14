"""              Indian Flag by Snehashish               """
import turtle
import time

screen = turtle.Screen()
screen.bgcolor("#b3daff")
screen.title("Indian Flag")
india = turtle.Turtle()
india.penup()
india.shape("circle")

flag_height = 300
flag_width = 450

start_x = -225
start_y = 150

stripe_height = flag_height/3
stripe_width = flag_width

chakra_radius = stripe_height / 2


def draw_fill_rectangle(x, y, height, width, color):
    india.goto(x,y)
    india.pendown()
    india.color(color)
    india.begin_fill()
    india.forward(width)
    india.right(90)
    india.forward(height)
    india.right(90)
    india.forward(width)
    india.right(90)
    india.forward(height)
    india.right(90)
    india.end_fill()
    india.penup()

def draw_stripes():
    x = start_x
    y = start_y
    draw_fill_rectangle(x, y, stripe_height, stripe_width, "#FF9933")
    y = y - stripe_height   
    draw_fill_rectangle(x, y, stripe_height, stripe_width, "white")
    y = y - stripe_height
    draw_fill_rectangle(x, y, stripe_height, stripe_width, '#138808')
    y = y - stripe_height

def draw_chakra():
    india.speed(1)
    india.goto(0,0)
    color = "#000080"
    india.penup()
    india.color(color)
    india.fillcolor(color)
    india.goto(0, 0 - chakra_radius)
    india.pendown()
    india.circle(chakra_radius)

    for _ in range(24):
        india.penup()
        india.goto(0,0)
        india.left(15)
        india.pendown()
        india.forward(chakra_radius)

def draw_stick():
    india.color("Gold")
    india.pensize(10)
    india.penup()
    india.goto(-222,147)
    india.right(90)
    india.pendown()
    india.forward(800)
 
def draw_stick0():
    india.color("#3d251e")
    india.pensize(410)
    india.penup()
    india.goto(-500,-860)
    india.right(90)
    india.pendown()
    india.backward(970)

def love_india():
    india.goto(-10,500)
    india.color('Red')
    style = ("Times New Roman", 16, "bold")
    india.write("I love my India", font=style, align="center")
    

time.sleep(1)
love_india()
draw_stripes()
draw_chakra()
draw_stick()
draw_stick0()
india.hideturtle()
screen.mainloop()
