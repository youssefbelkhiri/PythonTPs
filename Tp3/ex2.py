import math
def delta(a,b,c):
    return b**2 -4*a*c
def NombreRacine( a,b,c):
    if(delta(a,b,c)<0):
        return 0
    elif(delta(a,b,c)==0):
        return 1
    else:
        return 2
def AfficheNombreRacine(a,b,c):
    print(NombreRacine(a,b,c))

def Racine1(a, b, c):
    if delta(a, b, c) >= 0:
        x1 = (-b + math.sqrt(delta(a, b, c))) / (2 * a)
        return x1
    else:
        return None

def Racine2(a, b, c):
    if delta(a, b, c) >= 0:
        x2 = (-b - math.sqrt(delta(a, b, c))) / (2 * a)
        return x2
    else:
        return None
def conversion_temps(heures, minutes, secondes):
    return heures * 3600 + minutes * 60 + secondes

def temps_ecoule(heure1, minute1, seconde1, heure2, minute2, seconde2):
    temps1 = conversion_temps(heure1, minute1, seconde1)
    temps2 = conversion_temps(heure2, minute2, seconde2)
    duree = abs(temps2 - temps1)
    return duree

def conversion_distance(km, m, cm):
    return km * 1000 + m + cm / 100

def vitesse(km, m, cm, heures, minutes, secondes):
    distance_en_metres = conversion_distance(km, m, cm)
    temps_en_secondes = conversion_temps(heures, minutes, secondes)
    if temps_en_secondes == 0:
        return None
    else:
        vitesse_mps = distance_en_metres / temps_en_secondes
        return vitesse_mps



