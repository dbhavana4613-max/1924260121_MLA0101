from sklearn.tree import DecisionTreeClassifier
X=[[20,20000],[25,30000],[40,60000],[50,80000]]
Y=[0,0,1,1]
model=DecisionTreeClassifier(random_state=0)
model.fit(X,Y)
print(model.predict([[45,70000]]))
