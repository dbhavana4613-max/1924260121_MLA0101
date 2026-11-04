people={
    "Arun":"12-04-2005",
    "Ravi":"20-08-2004",
    "Priya":"15-01-2006"
    }
name = input("Enter name: ").title()
print(people.get(name, "Record not found"))
