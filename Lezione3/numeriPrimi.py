import math
def primiNumeriPrimi(n):
    primi = [2, 3, 5, 7, 11]
    
    x = 13
    indice = 0
    while (len(primi) < n - 1): # ciclo grande
        primo = True # variabile per stampare o no il numero
        
        for i in primi: # ciclo che gestisce tutti i numeri
            if x % i == 0: # se non è primo
                primo = False # non è primo
             
        if(primo): # se è primo
            primi.append(x) # lo aggiungo
        
        x += 2 # incremento la x di 2 (salto i pari)
    
    primi.insert(0, 1)
    print(primi)
    print(len(primi))


while True:
    # devo essere certo che l'utente abbia inserito un numero intero
    a = input("Dimmi quanti numeri primi vuoi ")
    try:
        a = int(a)
        if (a < 10 and a > 100):
            print("Numero tra 10 e 1000")
        else:
            break
    except:
        print("Hai sbagliato, devi scrivere un numero intero")
        
primiNumeriPrimi(a)
            
            
            
def primiNumeriPrimiMiei(n):
    x = 2
    primi = []
    
    while (len(primi) < n - 1):
        isPrimo = True
        
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                isPrimo = False
                break
            
        if(isPrimo):
            primi.append(x)
        x += 1
        
    primi.insert(0, 1)
    print(primi)
    print(len(primi))

