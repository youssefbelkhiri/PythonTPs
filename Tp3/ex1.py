def somme(i,n):
    if i == n:
        return n
    else:
        if i<n:
            return i+somme(i+1,n)
        else:
            return n+somme(i,n+1)
print(somme(5,8))
