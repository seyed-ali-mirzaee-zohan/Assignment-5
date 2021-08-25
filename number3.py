import turtle
window=turtle.Screen()
window.setup(700,600)
window.bgcolor("yellow")
window.title("Exercise number 3")
agent=turtle.Turtle()
agent.pensize(2)
agent.speed(1)
agent.shape("turtle")
agent.color("red")
origin_of_coordinates=-3
for i in range(3,10):
    for j in range(i):
        angle=360.0/i #  شایان ذکر است که مجموع زوایای خارجی چندضلعی های منتظم برابر با 360 درجه است
        agent.forward(30+i*10)
        agent.left(angle)
    agent.penup()
    agent.goto(origin_of_coordinates,2.5*origin_of_coordinates)
    agent.pendown()
    origin_of_coordinates-=8
window.exitonclick()