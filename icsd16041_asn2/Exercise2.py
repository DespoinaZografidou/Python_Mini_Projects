#Despoina Zwgrafidou 321/2016041
import os

#vrogxos epanalhpshs gia thn epanalhpsh ths diadikasia an thelhsei o xrhsths
while True :

    #vrogxos epanalhpshw se periptwsh pou o xrhsths den eisagei kati gia thn sugkekrimenh erwthsh
    while True :
        answer = input('\nChoose one of the following:\n   1)Insert new word\n   2)Search for a word\n   answer: ')
        if (len(answer)==0):    #ean den eisagei tipota o xrhsths 
            continue   #ksanaemfanise thn erwthsh
        elif (answer=='1' or answer=='2'): #an epiliksei o xrisths 1 h 2 sunexise to programma
             break   # vges apo ton vrogxo
        else:    #an eisagei o xrhsths kati asxeto 
            continue    # ksanaemfanise th erwthsh

    #an o xrhsths epileksei thn 1h epilogh
    if(answer == '1'):
        #vrogxos epanalhpshw se periptwsh pou o xrhsths den eisagei kati gia thn sugkekrimenh erwthsh
        while True:
            word=input('Insert the word that you want in english: ')
            if (len(word)==0 ):     #ean den eisagei tipota o xrhsths
                continue     #ksanaemfanise thn erwthsh
            else:   #an eisagei kati  o xrhsths
                break
        #vrogxos epanalhpshw se periptwsh pou o xrhsths den eisagei kati gia thn sugkekrimenh erwthsh
        while True:
            translation=input('Insert the greek translation of the word: ')
            if (len(translation)==0):   #ean den eisagei tipota o xrhsths
                continue     #ksanaemfanise thn erwthsh
            else:   #an eisagei kati  o xrhsths
                break    # vges apo ton vrogxo
    
    
        location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) #euresh topothesia tou arxeio
        fp = open(os.path.join(location,'dict.txt'), 'a') #dhmiourgia/anoigma arxeiou
        fp.write(word +','+translation +'\n')   #eisagwgh leksis kai metafrashs sto arxeio
        fp.close()  #kleisimo arxeiou
        print('----------The word is in the script!!!------------') #typwsh oti ta stoixeia katagrafikan sto arxeio 

    #an o xrhsths epileksei thn 2h epilogh
    if(answer=='2'):
        #vrogxos epanalhpshw se periptwsh pou o xrhsths den eisagei kati gia thn sugkekrimenh erwthsh
        while True:
            keyword=input('Give the word tha you want to search: ')
            if (len(keyword)==0 ):  #ean den eisagei tipota o xrhsths
                continue     #ksanaemfanise thn erwthsh
            else:   #an eisagei kati  o xrhsths
                break   # vges apo ton vrogxo
    
        location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))   #euresh topothesia tou arxeio
        fp = open(os.path.join(location,'dict.txt'), 'r') # anoigma arxeiou gia diavasma
    
        temp={} #dhmiourgia listas gia sugrathsh kai lekshs kleidi se emfanish shmasias ths

       #vrogxos epanalhpsh gia to diavasma tou arxeiou grammh grammh
        for line in fp:
            (word,meaning)=line.split(',') #se kathe grammh pou diavazei spasthn se 2 kommatia sto shmeio pou uparxei to komma
            temp[word]=meaning #kai sth lista thesh tou kleidiou eishgage th shmasia 
        if keyword in temp: # ean uparxei thesh me to kleidh 
            print(keyword +' = ' + temp[keyword]) # emfanise th shmasia

        fp.close()   #kleisimo arxeiou     

    #vrogxos epanalhpshs poy elegxei thn apanthsh tou xrhsth gia to an thelei na epanalavei thn diadikasia
    while True :
        replay = input("Do you want to continue ?(yes or no): ")  #o xrhsths eisagei thn apanthsh tou 
        if (replay != 'yes' and replay != 'no'):    #an h apanthsh den einai yes h no 
            continue     #ksanaemfanise thn erwthsh
        else: # alliws vges apo ton vrogxo
            break
    #an h apanthsh einai no tote stamathse to programma   
    if (replay == 'no'):
        break