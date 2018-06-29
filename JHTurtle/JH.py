from turtle import Turtle as t, Screen
import random as r  # Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).

# from turtle import Turtle as t, Screen
wn = Screen()

wn.bgcolor('black')

wn.screensize(2000, 2000)

point = 0

pt = t()

draw = t()  # -280, 250 부터


def drawwall():
    draw.pencolor("white")
    draw.penup()
    draw.goto(-280, 250)
    draw.pendown()
    draw.goto(280, 250)
    draw.goto(280, -250)
    draw.goto(-280, -250)
    draw.goto(-280, 250)
    draw.speed(2)


def L():  # 재시작하는 함수
    global playing
    global point
    if playing == False:
        point = 0
        config()
        middle.clear()
        playing = True
        travel()


playing = True

spaceship = t()
red = t()
middle = t()
green = t()


def config():  # 설정하는 부분
    global speed
    global redspeed
    spaceship.color('green')
    spaceship.goto(0, 0)
    spaceship.setheading(0)
    spaceship.speed(0)  # 속도 = 0 : 제일 빨리 움직이게 설정
    speed = 5  # 움직이는 칸 수(거리)
    spaceship.penup()

    red.color('red')
    red.penup()
    red.goto(0, 100)
    red.speed(0)
    redspeed = 4
    red.penup()

    middle.goto(0, 0)
    middle.penup()
    middle.ht()
    middle.pencolor("white")

    green.penup()
    green.goto(100, 100)
    green.speed(0)
    green.shape("circle")
    green.color("green")

    pt.penup()
    pt.ht()
    pt.goto(-290, 250)
    pt.pencolor("white")
    pt.clear()
    pt.write("No point LOL", move=False, align="left", font=("Arial", 18, "normal"))


def gr():
    global point
    if green.distance(spaceship) < 15:
        x = r.randint(-250, 250)
        y = r.randint(-200, 200)
        green.setx(x)
        green.sety(y)
        point += 1
        pt.clear()
        pt.write("point = " + str(point), move=False, align="left", font=("Arial", 18, "normal"))


def redmove():
    global redspeed
    angle = red.towards(spaceship.position())
    red.setheading(angle)
    red.forward(redspeed)


def travel():
    global speed
    global playing

    spaceship.forward(speed)
    if (spaceship.xcor() >= 280 or spaceship.ycor() <= -250 or spaceship.xcor() <= -280 or spaceship.ycor() >= 250):
        spaceship.forward(-speed)  # 앞으로 몇 칸 가라 : 밖에 나가지 않았을 때
        # 논리연산자 : A and B, A or B, not A
    redmove()
    gr()
    global point
    if spaceship.distance(red) < 15:  # 두개가 닿았을 때
        middle.goto(0, 50)
        middle.write("YOU ARE DEAD", True, align="center", font=("Arial", 28, "normal"))
        middle.goto(0, -50)
        middle.write("PRESS SPACE TO RESTART", True, align="center", font=("Arial", 28, "normal"))
        playing = False
    else:
        wn.ontimer(travel, 5)  # 5 msec : 0.005 sec

wn.onkey(lambda: spaceship.setheading(0), 'Right')
wn.onkey(lambda: spaceship.setheading(90), 'Up')
wn.onkey(lambda: spaceship.setheading(180), 'Left')
wn.onkey(lambda: spaceship.setheading(270), 'Down')
wn.onkey(L, 'space')  # 스페이스바 눌렀을 때 L을 실행한다.

wn.listen()

drawwall()
config()
travel()

wn.mainloop()

# "벽에 닿으면" : 좌우 280, -280
# 내 위치의 x좌표 > 280 (오른쪽으로 나갔다)
# 내 위치의 x좌표 < -280 (왼쪽으로 나갔다)

# randint(두개의 인자를 받는다 200, -200사이 200, -200사이) if(두개의 인자) 그러면 뒤로 움직임