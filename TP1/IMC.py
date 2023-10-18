poids = float(input("entrez votre poids"))
taill = float(input("entrez votre taille"))

IMC = poids / taill ** 2

if IMC < 16.5:
    print("Famine")
elif  18.5 > IMC >= 16.5:
    print("Maigreur")
elif 25 > IMC >=18.5:
    print("Corpulence normale")
elif 30 > IMC >= 25:
    print("Surpoids")
elif 35 > IMC >= 30:
    print("Obisité modérée")
elif 40 > IMC >= 30:
    print("Obisité modérée")
else:
    print("Obisité morbide ou massive")
    