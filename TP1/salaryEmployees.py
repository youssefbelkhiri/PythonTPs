grade = input("entrez le grade de l'emploiyée")
nbrHrs = int(input("entrez le nombre des heurs"))

gradsList = {
    'A':{'tarif':200,'hrsPrime':20,'prime':1000},
    'B':{'tarif':150,'hrsPrime':20,'prime':800},
    'C':{'tarif':120,'hrsPrime':15,'prime':500},
    'D':{'tarif':100,'hrsPrime':15,'prime':350},
    'E':{'tarif':80,'hrsPrime':10,'prime':100},
}

if grade in gradsList:
    tarif = gradsList[grade]['tarif']
    prime = gradsList[grade]['prime']
    hrsPrime = gradsList[grade]['hrsPrime']
    salaire = (tarif  * nbrHrs) + (prime * (nbrHrs // hrsPrime))
    print(f"le salaire de l'emploé est {salaire} DH")
else:
    print("le grade n'est pas validé")