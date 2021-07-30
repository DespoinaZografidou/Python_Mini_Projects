#321/2016041,Despoina zwgrafidou
import re                                   #vivlio8hkh gia tous lektikous/suntaktikous analutes
import csv                                  #vivlio8hkh gia thn anagnwsh tou csv arxeiou
import urllib.request                       #vivliou8hkh gia thn anagnwsh tou csv arxeiou apo url
import sys

#klassh pou orizei to krousma
class Case ():                                                                  
    def __init__(self,number,date):   
        self.date = date                                                        
        self.number = number                                                    

#klash pou orizei thn xwra
class Country (Case):
    def __init__(self,name):
        self.name=name 
        self.geo_parts=[]
        self.caselist=[]
        self.totalcases=0
    
    #prosthikh krousmatwn 
    def addcases(self,numbers,dates):  
        if self.caselist != []:                                         #se periptwsh pou h lista me ta skourmata den einai kenh
            for i in range(len(self.caselist)):
                self.caselist[i].number+=int(numbers[i])                #prostheth thn ka8e 8esh tis kainourgias listas krousmatwn me thn ka8e 8esh ths palias listas                                 
        else:                                                           #se periptwsh pou h lista einai kenh
            for n in range(len(numbers)):
                self.caselist.append(Case(int(numbers[n]),dates[n]))    #gemizei tin caselist me krousmata-antikeimena 

    #prosthikh geografikou diamerismatos            
    def addgeo_part(self,name):
        geo_part=Country(name)
        self.geo_parts.append(geo_part)

    #upologimos sunolikwn krousmatwn
    def gettotalcases(self):
        for case in self.caselist:
            self.totalcases += case.number
        return self.totalcases
    
    #gia thn tupwsh olwn twn krousmatwn ana mera gia thn xwra
    def getallcases(self):
        list=[]
        dt=[]
        for case in self.caselist:
            list.append(case.number)
            dt.append(case.date)
            
        for i in range(len(list)):
            print( dt[i],' = ',list[i])   
    
    #gia thn tupwsh twn krousmatwn gia sugkekrimenh hmeromhnia ths xwras
    def getcase(self, date):                                                    
        for case in self.caselist:                                                 
            if case.date == date:                                               
                print(self.name + ' = '+ str(case.number))                                              
        

#anoigei to arxeio kai to diaxwrizei me \n
r = urllib.request.urlopen("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv").read().decode('utf8').split("\n") 

csvfile = csv.reader(r)                                                          #exagete me epanalhpsh
lines = list(csvfile)                                                            #pernei tis grammes
datelist=[]                                                                      #lista gia thn apothikeush hmeromhniwn
countrylist=[]                                                                   #lista gia thn apothikeush twn xwrwn-antikeimenwn

for line in lines:                                                               #gia kathe grammh pou diavazeis sto arxeio
    
    #eisagwgh sth lista oi hmeromhnies ths prwths grammhs
    if 'Country/Region' in line:
        datelist=line[4:]                                          
        
    #dhmiourgia xwrwn-antikeimenwn    
    if ''.join(line[1:2])!='Country/Region':                                  #apofugh prwths grammhs
        string=''.join(line[1:2])
        string2=''.join(line[0:1])

        for country in countrylist:                                          #elegxos sthn lista countrylist an uparxei hdh h sugkekrimenh xwra-antikeimeno kai eisagei ta nea stoixeia ths xwras
            if country.name == string:
                country.addgeo_part(string2)
                country.addcases(line[4:],datelist) 
                break

        else:                                                               #an den uparxei h sugkekrimenh xwra antikeimeno dhmiourgei nea kai eisagei ta stoixeia
            addcountry=Country(string)
            addcountry.addgeo_part(string2)
            addcountry.addcases(line[4:],datelist)
            countrylist.append(addcountry)

 #Menu   
while True:
    while True:
        choice=input("Menu:\n0.Exit\n1.Cases per country\n2.Case per day\n3.Show the country with the maximum cases:\n")

        if choice!='0' and choice != '1' and choice != '2' and choice != '3' :         #elegxos epiloghs tou xrhsth          
            print("This choice is not valid !!!\n")
            continue
        else:
            break

    #tupwsh ola ta krousmata ths xwra pou epelekse o xrhsths
    if choice == '1':
        cntr=input("Insert the country:")
        for country in countrylist:
            if country.name == cntr:
                print( country.name +':')
                country.getallcases()
                break

     #tupwsh ta krousmata twn xwrwn thn hmeromhnia pou eishgage o xrhsths           
    if choice=='2':
        date = input("Insert a date (mm/dd/yy): ")
        for country in countrylist:
            country.getcase(date)
            
    #tupwsh ths xwras me ta perissotera krousmata
    if choice=='3':
        max=-1
        for country in countrylist:
            if max<country.gettotalcases():
                max=country.gettotalcases()
                cname=country.name
        print('The country with the maximum cases is '+cname+' with '+ str(max) + ' cases')  
    
    #eksodos apo to programma
    if choice=='0':
        break


    