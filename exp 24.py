rules={"flu":["fever","cough"]}
facts={"fever","cough"}
def prove(goal):
    if goal in facts:
        return True
    if goal in rules:
        return all(prove(x)for x in rules[goal])
        return False
print("Goal proved:",prove("flu"))
