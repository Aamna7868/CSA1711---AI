from sklearn.tree import DecisionTreeClassifier

# Features: [Study hours, Attendance]
X = [
    [1, 40],
    [2, 50],
    [3, 60],
    [4, 70],
    [5, 80],
    [6, 90]
]

# 0 = Fail, 1 = Pass
y = [0, 0, 0, 1, 1, 1]

model = DecisionTreeClassifier(random_state=0)
model.fit(X, y)

prediction = model.predict([[5, 85]])

print("Prediction:", "Pass" if prediction[0] == 1 else "Fail")