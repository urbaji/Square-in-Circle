import turtle

def draw_circle(radius):
    turtle.penup()
    turtle.goto(0, -radius) 
    turtle.pendown()
    
    steps = 120  
    angle = 360 / steps
    side_length = (2 * 3.141592653589793 * radius) / steps  

    for _ in range(steps):
        turtle.forward(side_length)
        turtle.left(angle)

def draw_square_inside_circle(radius):
    side = radius * 1.41421356237  

    turtle.penup()
    turtle.goto(-side / 2, side / 2)  
    turtle.pendown()

    for _ in range(4):
        turtle.forward(side)
        turtle.right(90)

def main():
    turtle.speed(0)
    draw_circle(100)
    draw_square_inside_circle(100)
    turtle.done()

if __name__ == "__main__":
    main()