# - Calcolare la divisione intera accettando come parametri dividendo e divisore, utilizzando solo somme e sottrazioni. 
# Il risultato deve essere una tupla con quoziente intero e resto
def divisione(dividendo, divisore):
    quoziente = 0
    resto = 0
    while (dividendo >= divisore):
        quoziente += 1
        dividendo = dividendo - divisore
    resto = dividendo # quello che rimane
    print(f"{quoziente}, {resto}")
        
divisione(5, 4)
divisione(1, 4)
divisione(2, 2)
divisione(7, 5)
