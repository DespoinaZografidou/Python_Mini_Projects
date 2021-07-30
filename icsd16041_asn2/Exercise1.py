# Despoina Zwgrafidou 321/2016041 
import random

Passwords=[]    #pinakas/lista gia thn apothikeush twn kwdikwn
Sympols=['!','@','$','#','%','^','&','*']   #pinakas pou emperiexei xarakthres gia na eisagoume sto kwdiko pu tha dhmioyrghsoume

#vrogxos epanalhpshs gia thn epanalhpsh ths diadikasia an thelhsei o xrhsths
while True :  

    #vrogxos epanalhpshw se periptwsh pou o xrhsths den eisagei kati gia thn sugkekrimenh erwthsh
    while True :
        name = input("What \'s your name ?: ").capitalize()     #eisagwgh onomatos 
        if len(name)==0:   #ean den eisagei tipota o xrhsths
            continue    #ksanaemfanise thn erwthsh
        else:   #alliws vges apo ton vrogxo
            break

    #vrogxos epanalhpshw se periptwsh pou o xrhsths den eisagei kati gia thn sugkekrimenh erwthsh
    while True :
        colour = input ("What \'s your favourite colour ?: ")
        if len(colour)==0:  #ean den eisagei tipota o xrhsths
            continue  #ksanaemfanise thn erwthsh
        else:    #alliws vges apo ton vrogxo
            break

    #vrogxos epanalhpshw se periptwsh pou o xrhsths den eisagei kati gia thn sugkekrimenh erwthsh
    while True :
        number = input ("What \'s your favourite number ?: ")
        if len(number)==0:   #ean den eisagei tipota o xrhsths
            continue     #ksanaemfanise thn erwthsh
        else:  #alliws vges apo ton vrogxo
            break

     #vrogxos epanalhpshw se periptwsh pou o xrhsths den eisagei h eisagei 0,1,2,3 ws arithmo pshfiwn gia ton kwdiko tou
    while True :
        length = input ("How many digitals you want on your password ?(length>4): ")  #eisagwgh plhthos pshfiwn pou thelei na exei o kwdikos tou 
        if (len(length)==0 or length=='0' or length=='1'or length=='2'or length=='3'):  #ean den eisagei tipota h eisagei 0,1,2,3 o xrhsths
            print('Try again!')
            continue   #ksanaemfanise thn erwthsh
        else:    #alliws vges apo ton vrogxo
            length=int(length) #metetrepse to length se integer
            break

    string="" #arxikopoihsh metavlhths h opoia xrhshmopoihtai gia thn apothikeush to enos kwdikou
      
      #-------------Efoson einai 3 erwthseis uparxoun 6 sundiasmoi gia thn dhmiourgia tou password-------
        
    if(random.randrange(1,6) == 1): #onoma+symvolo,xrwma+symvolo,noumero+symvolo
        part = len(name) // 2
        string += name[:part] + Sympols[random.randrange(0,8)] 
        part = len(colour) // 2
        string += colour[:part] + Sympols[random.randrange(0,8)] 
    
        string += number+ Sympols[random.randrange(0,8)] 

    elif(random.randrange(1,6) == 2):#xrwma+symvolo,onoma+symvolo,noumero+symvolo
        part = len(colour) // 2
        string += colour[:part] + Sympols[random.randrange(0,8)]
        part = len(name) // 2
        string += name[:part] + Sympols[random.randrange(0,8)]  
    
        string += number + Sympols[random.randrange(0,8)] 
    
    elif(random.randrange(1,6) == 3):#xrwma+symvolo,noumero+symvolo,onoma+symvolo
        part = len(colour) // 2
        string += colour[:part] + Sympols[random.randrange(0,8)]  

        string += number+ Sympols[random.randrange(0,8)]

        part = len(name) // 2
        string += name[:part] + Sympols[random.randrange(0,8)] 

    elif(random.randrange(1,6) == 4):#noumero+symvolo,xrwma+symvolo,onoma+symvolo
    
        string += number+ Sympols[random.randrange(0,8)]

        part = len(colour) // 2
        string += colour[:part] + Sympols[random.randrange(0,8)]  
        part = len(name) // 2
        string += name[:part] + Sympols[random.randrange(0,8)] 

    elif(random.randrange(1,6) == 5):#noumero+symvolo,onoma+symvolo,xrwma+symvolo
    
        string += number+ Sympols[random.randrange(0,8)]
    
        part = len(name) // 2
        string += name[:part] + Sympols[random.randrange(0,8)] 
        part = len(colour) // 2
        string += colour[:part] + Sympols[random.randrange(0,8)]  

    elif(random.randrange(1,6) == 6):#onoma+symvolo,noumero+symvolo,xrwma+symvolo
        part = len(name) // 2
        string += name[:part] + Sympols[random.randrange(0,8)] 
    
        string += number+ Sympols[random.randrange(0,8)]
    
        part = len(colour) // 2
        string += colour[:part] + Sympols[random.randrange(0,8)]  

    #an o kwdikos pou dhmiourghthike einai megaluteros apo ton kwdiko pou epithimei o xrhsths
    if (len(string) > length):
        string = string [0:length]  #emfanise kai apothikeuse to plhthos poy epithumei o xrhsths 
    #an o kwdikos einai mikroteros apo to plhthos poy epithimei o xrhsths 
    elif (len(string) < length):
        for a in range ( len(string) , length ):    #ews otou sumplhrwse twn aritmo pou epithumei o xrhsths
            string += str(a)    # sumpllhrwse noumera 


    print('One of the possible password for you is: ', string)   #emfanise ton kwdiko

    Passwords.append(string)    #eishgage ton kwdiko ston pinaka/lista me toys kwdikous

    #vrogxos epanalhpshs poy elegxei thn apanthsh tou xrhsth gia to an thelei na epanalavei thn diadikasia
    while True :
        answer = input("Do you want to try again for another password ?(yes or no): ")  #o xrhsths eisagei thn apanthsh tou 
        if (answer != 'yes' and answer != 'no'):    #an h apanthsh den einai yes h no tote ksanaemfanise thn erwthsh
            continue
        else: # alliws vges apo ton vrogxo
            break
    #an h apanthsh einai no tote stamathse to programma   
    if (answer == 'no'):
        break

print("These are all the passwords we generated:\n", Passwords)     #emfanise thn lista me tous kwdikous