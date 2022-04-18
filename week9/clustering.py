import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv('iris_data.csv')

df = iris[['Sepal length','Sepal width','Species']]
iris = iris.drop(columns=['Petal length','Petal width'])

d = dict(tuple(iris.groupby("Species")))
print(type(d["I. setosa"]))

fig = plt.figure()
ax = fig.add_subplot(111)

for key, value in d.items():
    x = value["Sepal length"].tolist()
    y = value["Sepal width"].tolist()
    ax.scatter(x,y)
    
