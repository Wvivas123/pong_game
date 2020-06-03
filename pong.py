import turtle
import os

print("Welcome to Pong!")
print("---------------")
print(" |             ")
print("       0       ")
print("             | ")
print("---------------")


player1_name = input("What is Player 1's Name? ")
player2_name = input("What is Player 2's Name? ")


wn = turtle.Screen()
wn.title("Pong by William Vivas")

wn.bgcolor("green")
wn.setup(width=800, height=600)
wn.tracer(0)

score_a = 0
score_b = 0

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color('white')
paddle_a.shapesize(stretch_len=1, stretch_wid=5)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color('white')
paddle_b.shapesize(stretch_len=1, stretch_wid=5)
paddle_b.penup()
paddle_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color('white')
ball.penup()
ball.goto(0, 0)

ball.dx = 2
ball.dy = -2

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("{}: 0 {}: 0".format(player1_name, player2_name), align="center", font=("Courier", 24, "normal"))








# Paddle Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')

while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1


    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("{}: {} {}: {}".format(player1_name, score_a, player2_name, score_b), align="center", font=("Courier", 24, "normal"))
        os.system("afplay Pong_Sound_Score.wav&")

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("{}: {} {}: {}".format(player1_name, score_a, player2_name, score_b), align="center", font=("Courier", 24, "normal"))
        os.system("afplay Pong_Sound_Score.wav&")


    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        os.system("afplay Pong_Sound.wav&")

        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        os.system("afplay Pong_Sound.wav&")
        ball.setx(-340)
        ball.dx *= -1






