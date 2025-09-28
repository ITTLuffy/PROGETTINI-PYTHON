# - Poi un quadrato, un pentagono, un esagono, un eptagono, un ottagono, ... 
# e qualsiasi poligono regolare di N lati (indicato tramite parametro)

# 180 - (n-2) x 180 / n formula per calcolare l'angolo
import turtle


def disegnaPoligono(lato, nLati):
    turtle.speed(1)
    turtle.pencolor("red")
    turtle.pensize(14)
    
    for i in range(nLati):
        turtle.forward(lato)
        turtle.left(180 - ((nLati-2) * 180 / nLati))
    turtle.clear()
        
disegnaPoligono(100, 4) 
disegnaPoligono(100, 3) 
disegnaPoligono(100, 5) 
disegnaPoligono(100, 6) 
disegnaPoligono(100, 7) 
disegnaPoligono(100, 8) 
disegnaPoligono(100, 9) 
