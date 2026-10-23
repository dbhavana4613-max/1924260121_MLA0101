def alphabeta(tree,depth,alpha,beta,is_max):
    if depth==2:
        return tree
    if is_max:
        v= float('-inf')
        for x in tree:
            v=max(v,alphabeta(x,depth+1,alpha,beta,False))
            alpha=max(alpha,v)
            if alpha>=beta:
                break
        return v
    else:
        v=float('inf')
        for x in tree:
           v=min(v,alphabeta(x,depth+1,alpha,beta,True))
           beta=min(beta,v)
           if alpha>=beta:
             break
    return v
tree=[[3,5],[2,9]]
print("Best value:",alphabeta(tree,0,-999,999,True))
