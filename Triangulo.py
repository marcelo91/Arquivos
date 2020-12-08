import turtle

def draw_tringuloC(some_turtle):
    for i in range(1,4):
        some_turtle.forward(40)
        some_turtle.left(120)
        
def draw_tringuloB(some_turtle):
    draw_tringuloC(some_turtle)
    some_turtle.forward(40)
    draw_tringuloC(some_turtle)
    some_turtle.left(60)
    draw_tringuloC(some_turtle)
    some_turtle.forward(40)
    some_turtle.left(60)
    draw_tringuloC(some_turtle)
    some_turtle.forward(40)
    some_turtle.left(180)

def draw_tringuloA(some_turtle):
    draw_tringuloB(some_turtle)
    some_turtle.forward(80)
    some_turtle.left(60)
    draw_tringuloB(some_turtle)
    some_turtle.right(120)
    some_turtle.forward(80)
    some_turtle.right(180)
    draw_tringuloB(some_turtle)
    some_turtle.left(60)

def draw_triangule():
    window = turtle.Screen()
    window.bgcolor("blue")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow", "red")
    brad.speed(0)
    draw_tringuloA(brad)
    draw_tringuloA(brad)
    brad.right(120)
    brad.forward(320)
    brad.left(120)
    brad.forward(160)
    draw_tringuloA(brad)



    window.exitonclick()
draw_triangule()

    

