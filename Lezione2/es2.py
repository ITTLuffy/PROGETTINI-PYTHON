# - Realizzare un conto alla rovescia accettando in ingresso il valore iniziale 
# (intero e positivo) e una funzione di attesa della libreria time.
import time

def contoAllaRovescia(valore, wait):
    if valore < 0:
        return 0
    
    while valore > 0:
        print(valore)
        wait(1)
        valore -= 1

contoAllaRovescia(10, time.sleep)
    
    

