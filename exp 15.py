parent=[("John","Alice"),("Alice","Bob")]
for x,y in parent:
    print(x,"is parent of",y)
    for x,y in parent:
        for a,b in parent:
            if y==a:
                print(x,"is grandparent of ",b)
