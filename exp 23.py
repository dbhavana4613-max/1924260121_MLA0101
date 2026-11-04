facts={"fever","cough"}
rules=[({"fever","cough"},"possible_flu"),({"possible_flu"},"consult_doctor")]
changed=True
while changed:
    changed=False
    for conditions,result in rules:
        if conditions<=facts and result not in facts:
            facts.add(result)
            changed=True
            print(sorted(facts))
