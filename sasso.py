import random 

punteggioCpu = 0
punteggioGiocatore =0


mossa = ['sasso', 'carta', 'forbici']

print ('Benvenuti alla morra cinese v0.01')


while True:
    
    
    giocatore = (input("Scegli la tua mossa: sasso | carta |forbici	 \n").lower())
    if giocatore == 'x':
        break

        
    computer = random.choice(mossa)
    
    if giocatore in mossa:
        
        print (f' il giocatore lancia {giocatore }')
        print (f' il computer lancia {computer}')
        
        if giocatore ==computer :
            print(' partita patta')
            print(punteggioGiocatore)
            print(punteggioCpu)
            print('____________________________')
        
        elif giocatore== 'sasso' and computer == 'forbici':
            print (' vince giocatore ')
            punteggioGiocatore +=1
            print(punteggioGiocatore)
            print(punteggioCpu)
            print('____________________________')
            
        
        elif giocatore== 'carta' and computer == 'sasso':
            print (' vince giocatore ')
            punteggioGiocatore +=1
            print(punteggioGiocatore)
            print(punteggioCpu)
            print('____________________________')
            
        elif giocatore== 'forbici' and computer == 'carta':
            print ('vince giocatore ')
            punteggioGiocatore +=1
            print(punteggioGiocatore)
            print(punteggioCpu)
            print('____________________________')
            
        else:
            print('vince computer ')
            punteggioCpu+=1
            print(punteggioGiocatore)
            print(punteggioCpu)
            print('____________________________')
                  

    else :
        print('errore : ripeti selezione')
        print('____________________________')

      
       
