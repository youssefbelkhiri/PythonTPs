L = [1,-30,0,-2,500,4,2,100]
M = []

M.extend([x for x in L if x < 0])
M.extend([x for x in L if x == 0])
M.extend([x for x in L if x > 0])

print(M)