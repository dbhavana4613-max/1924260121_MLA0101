from collections import deque
g={'A':['B','C'],'B':['D'],'C':['E'],'D':[],'E':[]}
q=deque(['A'])
while q:
    n=q.popleft()
    print(n,end=" ")
    q.extend(g[n])
                                
