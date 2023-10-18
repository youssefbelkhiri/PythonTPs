sum=0
cmp=0
for i in range(0,4):
    note = float(input("entrez la note num "+str(i+1)+":"))
    coe = int(input("entrez le coefficient:"))
    sum += note*coe
    cmp += coe
if(sum/cmp >=10):
    print("moyenne de ces notes: ",str(sum/cmp)," semestre validé")
elif(sum/cmp >=7):
    print("moyenne de ces notes: ",str(sum/cmp)," rattrapage")
else:
    print("moyenne de ces notes: ",str(sum/cmp)," semestre non validé")
