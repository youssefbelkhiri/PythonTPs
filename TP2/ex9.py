choix = int(input("entrez 1(pour euro en mad) ou 2(pour mad en euro)"))
L = []
while True:
    val = int(input("entrez la valeur"))
    if val < 0 :
        break
    if choix == 1:
        newVal = val * 10.86
    elif choix == 2:
        newVal = val * 0.092
    L.append(newVal)    
print(L)