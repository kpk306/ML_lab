import numpy as np

X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([0,0,0,1])

w = np.zeros(2)
b = 0
lr = 0.1

for epoch in range(10):
    for i in range(len(X)):
        net = np.dot(X[i], w) + b
        y_pred = 1 if net >= 0 else 0
        error = y[i] - y_pred
        w += lr * error * X[i]
        b += lr * error

print("Weights:", w)
print("Bias:", b)
