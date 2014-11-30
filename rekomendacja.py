#  Wzorowane na przykładzie Rona Zacharskiego
#

from math import sqrt
import numpy

users = {
        "Ania": 
            {"Blues Traveler": 1.0,
            "Broken Bells": 1.5,
            "Norah Jones": 2,
            "Deadmau5": 2.5,
            "Phoenix": 3.0,
            "Slightly Stoopid": 0.5,
            "The Strokes": 0.0,
            "Vampire Weekend": 2.0},
         "Bonia":
            {"Blues Traveler": 4.0,
            "Broken Bells": 4.5, 
            "Norah Jones": 5.0,
            "Deadmau5": 5.5, 
            "Phoenix": 6.0, 
            "Slightly Stoopid": 3.5, 
            "The Strokes": 2.0,
            "Vampire Weekend": 5.0}
        }

        
def manhattan(rating1, rating2):
    
    """Oblicz odległość w metryce taksówkowej między dwoma  zbiorami ocen
       danymi w postaci: {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}
       Zwróć -1, gdy zbiory nie mają… wspólnych elementów"""
       
    # TODO: wpisz kod
    klucze1 = rating1.keys()
    klucze2 = rating2.keys()
    odleglosc = 0
    udaloSiePorownac = False

    for klucz in klucze1:
        if klucz in rating2.keys():
            udaloSiePorownac = True
            odleglosc = odleglosc + abs(rating2[klucz] - rating1[klucz])
    
    if (udaloSiePorownac==True):
        print "Odleglosc Manhattan:"
        print odleglosc
        return odleglosc
    else:
        return -1

def pearson(rating1, rating2):
    klucze1 = rating1.keys()
    klucze2 = rating2.keys()
    korelacja=0
    sumaXY=0
    sumaX=0
    sumaY=0
    n=0
    sumaXX=0
    sumaYY=0

    for klucz in klucze1:
        if klucz in rating2.keys():
            
            sumaXY= sumaXY + rating1[klucz]*rating2[klucz]
            sumaX= sumaX+ rating1[klucz]
            sumaY= sumaY+ rating2[klucz]
            n= n+1
            sumaXX= sumaXX + rating1[klucz]*rating1[klucz]
            sumaYY= sumaYY + rating2[klucz]*rating2[klucz]

            
    licznik= sumaXY- sumaX*sumaY/n
    mianownik= sqrt(sumaXX- sumaX*sumaX/n) * sqrt(sumaYY-sumaY*sumaY/n)
    korelacja= licznik/mianownik
    # korelacja=0.98 -> silna korelacja
    print "Korelacja"
    print korelacja
    return korelacja


def pearsonNumpy(rating1, rating2):
    korelacja=0
    keys = list(rating1.viewkeys() | rating2.viewkeys()) # Lista ze wszystkimi kluczami z obu słowników
    korelacja=numpy.corrcoef([rating1[x] for x in keys], [rating2[x] for x in keys])[0][1]
    print "Korelacja Numpy"
    print korelacja
    return korelacja

pearson(users["Ania"], users["Bonia"])
manhattan(users["Ania"], users["Bonia"])
pearsonNumpy(users["Ania"], users["Bonia"])
