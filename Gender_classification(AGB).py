from sklearn.ensemble import AdaBoostClassifier
# [height,weight, shoes size]

X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
    [190, 90, 47], [175, 64, 39],
    [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

# Identifying who is male and who is female
Y =['male', 'female', 'female', 'female', 'male', 'male', 'male', 'female', 'male','female','male']

# initializing AGB

agb = AdaBoostClassifier(learning_rate =0.1)

#fitting the model 

clf= agb.fit(X,Y)

predict = clf.predict([[190,90,37]])
print(predict)