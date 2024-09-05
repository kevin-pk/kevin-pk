
from sklearn.neighbors import KNeighborsClassifier

# [height,weight, shoes size]

X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
    [190, 90, 47], [175, 64, 39],
    [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

# Identifying who is male and who is female
y =['male', 'female', 'female', 'female', 'male', 'male', 'male', 'female', 'male','female','male']

clf = KNeighborsClassifier(n_neighbors =1)

# fitting the data
clf = clf.fit(X,y)

# testing the model to make a decision
prediction = clf.predict([[170,29,37]])
print(prediction)