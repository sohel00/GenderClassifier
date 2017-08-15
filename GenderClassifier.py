from sklearn import tree

# [height,weight,shoe size]
X = [[180,81,44],[177,40,43],[160,60,38],[154,54,37],[166,65,40],[190,90,47],[175,64,39],[177,70,39],[159,55,37],[171,75,42],[181,85,43]]
Y = ['male','female','female','female','male','male','male','female','male','female','male']

classify = tree.DecisionTreeClassifier()

# fitting the data in classify
classify = classify.fit(X,Y)

# saving the output in prediction
prediction = classify.predict([[140,75,45]])

print prediction
