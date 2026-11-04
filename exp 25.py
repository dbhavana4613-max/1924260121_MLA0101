graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}
 
h = {"A": 3, "B": 2, "C": 1, "D": 0}
 
start = input("Start: ")
goal = input("Goal: ")
open_list = [start]
 
while open_list:
    node = min(open_list, key=lambda x: h.get(x, 999))
    open_list.remove(node)
    print(node, end=" ")
 
    if node == goal:
        print("\nGoal found")
        break
 
    open_list += [
        n for n in graph.get(node, [])
        if n not in open_list
    ]


