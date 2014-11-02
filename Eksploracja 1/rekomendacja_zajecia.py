#  Wzorowane na przykÅ‚adzie Rona Zacharskiego
#

from math import sqrt

users = {     """słownik użytkowników, gdzie kluczem jest imię użytkownika, a wartościami są
                 kolejne słowniki, w którymi kluczami są nazwy zespołów, a wartościami są oceny użytkowników"""
        "Ania": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bonia":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Celina": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dominika": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Ela": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Fruzia":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Gosia": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Hela": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }



def manhattan(rating1, rating2):    #definiowanie funkcji manhattan
    
    """Oblicz odległość w metryce taksówkowej między dwoma  zbiorami ocen
       danymi w postaci: {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}
       Zwróć -1, gdy zbiory nie mają… wspólnych elementów"""
       
    # TODO: wpisz kod
    klucze1 = rating1.keys()    #uzyskanie nazw zespołów, które są kluczami w 1szym słowniku
    klucze2 = rating2.keys()    #uzyskanie nazw zespołów, które są kluczami w 2gim słowniku
    odleglosc = 0               
    udaloSiePorownac = False    #początkowy warunek, że użytkownicy nie ocenili żądnego tego samego zespołu

    for klucz in klucze1:           #wykonuje dla każdego klucza ze zbioru kluczy 
        if klucz in rating2.keys():     #jeśli klucz z 1szego słownika znajduje się w drugim zbiorze kluczy
            udaloSiePorownac = True     #użytkownicy ocenili jakieś te same zespoły
            odleglosc = odleglosc + abs(rating2[klucz] - rating1[klucz])    #obliczenie odległości

    if (udaloSiePorownac==True):    #jeśli mieli jakieś wspólne zespoły zwraca odległość
        return odleglosc
    else:                           #użytkownicy nie mają wspólnych zespołów
        return -1

def testManhattan(rating1, rating2, odleglosc):         #funkcja testowa, sprawdza, czy dobrze liczymy odległość
    if manhattan(rating1, rating2) == odleglosc:
        return True
    else:
        return False

##print (testManhattan({'łzy': 5, 'TL':3},
##                    {'łzy':10},
##                    5)
##       )
##
##print (testManhattan({'łzy': 5, 'TL':3},
##                    {'BS':10},
##                    -1)
##       )
    
    
##odlegloscOdAniDoHeli = manhattan(users["Ania"], users["Hela"])
##print ("od Ani do Heli jest ", odlegloscOdAniDoHeli)

# print( recommend('Hela', users))
# print( recommend('Celina', users))

def obliczNajblizszegoSasiada(imie, uzytkownicy):
    """dla danego uÅ¼ytkownika, zwróć listę innych użytkowników według bliskości preferencji"""
    odleglosci = []
    for imie2 in uzytkownicy:       #dla każdego klucza(imienia) w słowniku użytkowników
        odleglosc = 0
        if imie!=imie2:        #jeśli aktualny klucz - imię, jest różny od imienia osoby, dla której poszukujemy listy sąsiadów
            odleglosc = manhattan(uzytkownicy[imie], uzytkownicy[imie2]) #liczy odległość typu Manhattan
            odleglosci.append((odleglosc, imie2)) #dodanie do listy sąsiada i odległości
    return sorted(odleglosci)       #sortowanie wg odległości

##print(obliczNajblizszegoSasiada('Hela',users))

def recommend(username, users):
    """Zwróć listę rekomendacji dla użytkownika"""
    # znajdź preferencje najbliższego sąsiada
    nearestName = obliczNajblizszegoSasiada(username, users)[0][1]  #imię najbliższego sąsiada, bierze imię z 1 elementu listy
    print 'Najblizszy sasiad to: %s' % nearestName
    recommendations = []
    ratingOfNearest = users[nearestName]    #pobiera ze słownika zestaw wartości dla danego użytkownika, który jest najbliższym sąsiadem dla danej osoby
    print 'Jego rekomendacje to:'
    print ratingOfNearest 
    # zarekomenduj użytkownikowi wykonawcę, którego jeszcze nie ocenił, a zrobi‚ to jego najbliższy sąsiad
    userRating = users[username]    #pobranie zespołów, których słucha dana osoba, dla której szukamy rekomendacji
    
    for artist in ratingOfNearest:      #dla każdego wykonawcy, które słucha nasz najbliższy sąsiad
        if not artist in userRating:    #jeśli wykonawca nie występuje w zbiorze użytkownika
            recommendations.append((artist, ratingOfNearest[artist]))   #dodanie do listy rekomendacji nazwy wykonawcy i oceny sąsiada
    # zwróć posortowane rekomendacje
    return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True) #sortowanie 

print recommend('Hela', users)
