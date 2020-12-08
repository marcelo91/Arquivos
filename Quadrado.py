import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_square2():
    window = turtle.Screen()
    window.bgcolor("blue")
    brad = turtle.Turtle()
    brad.shape("triangle")
    brad.color("yellow", "red")
    brad.speed(0)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    window.exitonclick()
draw_square2()

    

