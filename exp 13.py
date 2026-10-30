from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
X,y=load_iris(return_X_y=True)
a,b,c,d=train_test_split(
    X,y,test_size=0.2,random_state=1
    )
model=MLPClassifier(max_iter=2000,random_state=1)
model.fit(a,c)
print("Accuracy:",round(model.score(b,d),2))
