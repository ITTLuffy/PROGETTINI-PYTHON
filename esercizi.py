import time
import turtle
# - Calcolare la divisione intera accettando come parametri dividendo e divisore, utilizzando solo somme e sottrazioni. 
# Il risultato deve essere una tupla con quoziente intero e resto

def divisione(dividendo, divisore): # funzione principale
    if divisore == 0:
        return(None, None)
    quoziente = 0 # risultato
    resto = 0 # resto
    while dividendo >= divisore: # finché il dividendo è maggiore/uguale di divisore
        quoziente = quoziente + 1 # aumento il quoziente
        dividendo = dividendo - divisore # aggiorno il valore del dividendo
    resto = dividendo # aggiorno il resto (quello che rimane)
    return quoziente, resto # ritorno una tupla con quoziente e resto

print(divisione(17, 5)) # stampo un esempio
print(divisione(4, 4))

# - Realizzare un conto alla rovescia accettando in ingresso il valore iniziale (intero e positivo) e una funzione di attesa della libreria time.

def contoAllaRovescia(iniz, wait): # funzione che prende il valore iniziale e la funzione wait
    while iniz >= 0: # finché è maggiore di 0
        print(iniz) # stampo al variabile
        wait(0) # funzione wait
        iniz -= 1 # decremento la variabile

contoAllaRovescia(10, time.sleep) # testo


# - Disegnare un triangolo equilatero con la libreria turtle

def disegnaTriangolo(lato):
    turtle.speed(1)
    turtle.pensize(10)  
    turtle.pencolor("pink")  

    for i in range(3):
        turtle.forward(lato)
        turtle.left(120) # angolo esterno

lato = 100
# disegnaTriangolo(lato)


# - Poi un quadrato, un pentagono, un esagono, un eptagono, un ottagono, ... e qualsiasi poligono regolare di N lati (indicato tramite parametro)

# (n-2) x 180 / n formula per calcolare l'angolo

turtle.clear()

def disegnaPoligono(lato, nLati):
    turtle.speed(1)
    turtle.pensize(10)  
    turtle.pencolor("pink")  

    for i in range(nLati):
        turtle.forward(lato)
        turtle.left(180 - ((nLati-2) * 180 / nLati))
    turtle.clear()

lato = 100

# disegnaPoligono(100, 12)

