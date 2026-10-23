def minimax(tree,depth,max_turn):
    if depth==2:
        return tree
    if max_turn:
        return max(minimax(x,depth+1,False)for x in tree)
    return min(minimax(x,depth+1,True)for x in tree)
tree=[[3,5],[2,9]]
print("Best value:",minimax(tree,0,True))
