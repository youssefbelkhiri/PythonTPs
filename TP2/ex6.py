nbr = int(input("entrez un nombre"))
L = [1,2,5,3,2,1]
L = [i for i in L if i != nbr]
print(L)