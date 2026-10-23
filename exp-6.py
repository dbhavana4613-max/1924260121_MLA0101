import heapq
g={'A':[('B',1),('C',4)],'B':[('D',2)],'C':[('D',1)],'D':[]}
h={'A':3,'B':2,'C':1,'D':0}
q=[(h['A'],0,'A',['A'])]
while q:
    f,cost,n,path=heapq.heappop(q)
    if n=='D':
       print("path:",path,"cost:",cost)
       break
    for x,w in g[n]:
       c=cost+w
       heapq.heappush(q,(c+h[x],c,x,path+[x]))
