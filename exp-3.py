import heapq
g={'A':[('B',1),('C',4)],'B':[('D',2)],'C':[],'D':[]}
q=[(0,'A')]
while q:
    c,n=heapq.heappop(q)
    print(n,c)
    for x,w in g[n]:
        heapq.heappush(q,(c+w,x))
