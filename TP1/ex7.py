a = int(input("entrez le nombre num 1:"))
b = int(input("entrez le nombre num 2:"))
op = input("entrez l'opération qui tu veux:")
match op:
    case '*':
        print(str(a),op,str(b),"=",str(a*b))
    case '/':
        print(str(a),op,str(b),"=",str(a/b))
    case '-':
        print(str(a),op,str(b),"=",str(a-b))
    case '+':
        print(str(a),op,str(b),"=",str(a+b))
    case default:
        print("nice")