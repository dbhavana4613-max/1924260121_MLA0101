import heapq
g={'A':['B','C'],'B':['D'],'C':['E'],'D':[],'E':[]}
h={'A':5,'B':3,'C':2,'D':1,'E':0}
q=[(h['A'],'A')]
while q:
    _,n=heapq.heappop(q)
    print(n,end=" ")
    for x in g[n]:
        heapq.heappush(q,(h[x],x))
        
