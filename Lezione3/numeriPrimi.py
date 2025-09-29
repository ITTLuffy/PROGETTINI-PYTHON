import math
def primiNumeriPrimi(n):
    primi = [2, 3, 5, 7, 11]
    
    x = 13
    indice = 0
    while (len(primi) < n): # ciclo grande
        primo = True # variabile per stampare o no il numero
        
        for i in primi: # ciclo che gestisce tutti i numeri
            if x % i == 0: # se non è primo
                primo = False # non è primo
             
        if(primo): # se è primo
            primi.append(x) # lo aggiungo
        
        x += 2 # incremento la x di 2 (salto i pari)
    
    print(primi)
    print(len(primi))



primiNumeriPrimi(100)
            
            
def primiNumeriPrimiMiei(n):
    x = 2
    primi = []
    
    while (len(primi) < n):
        isPrimo = True
        
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                isPrimo = False
                break
            
        if(isPrimo):
            primi.append(x)
        x += 1
        
    print(primi)
    print(len(primi))

primiNumeriPrimiMiei(100)
