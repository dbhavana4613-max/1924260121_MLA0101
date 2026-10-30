from itertools import permutations
for p in permutations(range(10),8):
    S,E,N,D,M,O,R,Y=p
    if S and M:
        a=1000*S+100*E+10*N+D
        b=1000*M+100*O+10*R+E
        c=10000*M+1000*O+100*N+10*E+Y
        if a+b==c:
            print(a,"+",b,"=",c)
            break
            
