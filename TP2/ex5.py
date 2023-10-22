L = [1,2,3,8,9]
index = 0
val = 4
while index < len(L) and L[index] < val:
    index += 1
L.insert(index,val)
print(L)  