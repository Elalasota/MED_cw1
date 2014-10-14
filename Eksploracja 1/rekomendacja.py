#!/usr/bin/env python
#-*- coding: utf-8 -*-
#  Wzorowane na przykładzie Rona Zacharskiego
#

from math import sqrt

users = {"Ania": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bonia":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Celina": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dominika": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Ela": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Fruzia":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Gosia": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Hela": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }



def manhattan(rating1, rating2):
    """Oblicz odległość w metryce taksówkowej między dwoma  zbiorami ocen danymi w postaci: 
    {'The Strokes': 3.0, 'Slightly Stoopid': 2.5} Zwróć -1, gdy zbiory nie mają wspólnych elementów"""
    odleglosc=0
    klucze1=rating1.keys()
    klucze2=rating2.keys()
    for klucz in klucze1:
        if klucz in rating2.keys():
            odleglosc=odleglosc+abs(rating2[klucz]-rating1[klucz])
        else:
            print(-1)
            pass
    print 
    return odleglosc
    # TODO: wpisz kod
    pass
manhattan(users["Ania"],users["Ela"])
print "Odległość w metryce taksówkowej użytkowników wynosi: "+str(manhattan(users["Ania"],users["Ela"]))
def computeNearestNeighbor(username, users):
    """dla danego użytkownika, zwróć listę innych użytkowników według bliskości preferencji"""
    odleglosc={}
    distances = []
    for klucz in users:
        if klucz!=username:
            #odleglosc[klucz]=manhattan(users[username], users[klucz])
            odleglosc[manhattan(users[username], users[klucz])]=klucz
    #distances=sorted(odleglosc, key=odleglosc.get)
    distances=sorted(odleglosc.items(), key=lambda x:x[0])
    print str(username)+", twoi najblizsi sasiedzi to: "+str(distances)
    return distances
computeNearestNeighbor("Ania",users)

def recommend(username, users):
    """Zwróć listę rekomendacji dla użytkownika"""
    # znajdź preferencje najbliższego sąsiada
    nearest = computeNearestNeighbor(username, users)[0][1]
    recommendations ={}
    for klucz in users:
        if klucz==nearest: #poszukiwanie najblizszego sasiada w danym slowniku
            for kl in users[klucz]: #wylowienie slownika uzytkownika ze slownika glownego
    # zarekomenduj użytkownikowi wykonawcę, którego jeszcze nie ocenił, a zrobił to jego najbliższy sąsiada
                if kl not in users[username].keys():    #szukanie zespolow, ktore nie byly sluchane przez uzytkownika, a tylko przez sasiada
                    #recommendations.append(kl)
                    recommendations[kl]=users[nearest][kl]    
    print str(username)+", możesz poznać nowe zespoły, które ocenił Twój najbliższy sąsiad: "+str(recommendations)
    # using the fn sorted for variety - sort is more efficient
    return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True)

# przykłady

recommend('Hela', users)
recommend('Celina', users)
