planets={
    "Mercury":"Closest to sun",
    "Venus":"Hottest planet",
    "Earth":"Known to support life",
    "Mars":"Red planet",
    "Jupiter":"Largest planet"
    }
name=input("Enter planet:").title()
print(planets.get(name,"Information unavailable"))
