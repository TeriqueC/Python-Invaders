#Space Invaders
import turtle
import math
import random

#screen
wn=turtle.Screen()
wn.bgcolor('black')
wn.title('space invaders')

#border
bp=turtle.Turtle()
bp.speed(0)
bp.color('white')
bp.penup()
bp.goto(-300,-300)
bp.pendown()
bp.pensize(3)
for side in range(4):
    bp.fd(600)
    bp.lt(90)
bp.hideturtle()

#score
score=0
#draw score
sp=turtle.Turtle()


#Creating Player
p1=turtle.Turtle()
p1.color('blue')
p1.shape('triangle')
p1.penup()
p1.speed(0)
p1.goto(0,-250)
p1.setheading(90)

#players weapon
w=turtle.Turtle()
w.color('yellow')
w.shape('triangle')
w.penup()
w.speed(0)
w.setheading(90)
w.shapesize(0.5, 0.5)
w.hideturtle()
weaponspeed=20
#weapon state, being fired or ready to fire
wstate= 'ready'

#number of invaders
numinvaders=5
#create empty list of invaders
invaders=[]
#add invaders to list
for i in range(numinvaders):
    #creating invader
    invaders.append(turtle.Turtle())

for invader in invaders:
    invader.color('red')
    invader.shape('circle')
    invader.penup()
    invader.speed(0)
    x= random.randint(-200, 200)
    y=random.randint(100, 250)
    invader.goto(x,y)

invaderspeed=2    

#moving the player
def p1_lt():
    x=p1.xcor()
    x-=15
    if x < -280:
        x= -280
    p1.setx(x)

def p1_rt():
    x=p1.xcor()
    x+=15
    if x > 280:
        x= 280
    p1.setx(x)

#shooting weapon
def w_f():
    #declare weaponstate as a global so it can be changed if necessary
    global wstate
    if wstate=='ready':
        wstate='fire'
        #moving bullet
        x=p1.xcor()
        y=p1.ycor() +10
        w.setposition(x,y)
        w.showturtle()

def isCollision(t1, t2):
    distance= math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2)+math.pow(t1.ycor()-t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False
    
#key binding
wn.listen()
wn.onkeypress(p1_lt, 'Left')
wn.onkeypress(p1_rt, 'Right')
wn.onkeypress(w_f, 'space')

#main game loop
while True:

    for invader in invaders:
        #moving the invader
        x = invader.xcor()
        x+=invaderspeed
        invader.setx(x)

        #moving invaders down and back
        if invader.xcor()>280:
            for i in invaders:
                y=i.ycor()
                y-=40
                i.sety(y)
            invaderspeed*=-1

        if invader.xcor()<-280:
            for i in invaders:
                y=i.ycor()
                y-=40
                i.sety(y)
            invaderspeed*=-1

        #weapon hits invader
        if isCollision(w, invader):
            #reset weapon
            w.hideturtle()
            wstate='ready'
            w.goto(0, -400)
            #reset invader
            x= random.randint(-200, 200)
            y=random.randint(100, 250)
            invader.goto(x,y)


        #collision with player
        if isCollision(p1, invader):
            p1.hideturtle()
            invader.hideturtle()
            w.hideturtle()
            print('game over')
            break


    #weapon movement
    if wstate=='fire':
        y=w.ycor()
        y+=weaponspeed
        w.sety(y)
    #border check
    if w.ycor()> 275:
        w.hideturtle()
        wstate='ready'
        
 
