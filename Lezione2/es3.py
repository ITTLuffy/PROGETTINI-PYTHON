# - Disegnare un triangolo equilatero con la libreria turtle

import turtle

def disegnaTriangoloEquilatero(lato):
    turtle.speed(1)
    turtle.pencolor("red")
    turtle.pensize(14)
    
    for i in range(3):
        turtle.forward(lato)
        turtle.left(120) # angolo esterno

disegnaTriangoloEquilatero(100)