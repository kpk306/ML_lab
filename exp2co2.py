import numpy as np

X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

w1 = np.random.rand(2,2)
w2 = np.random.rand(2,1)
lr = 0.5

def sigmoid(x):
    return 1/(1+np.exp(-x))

for epoch in range(10000):
    h = sigmoid(np.dot(X, w1))
    o = sigmoid(np.dot(h, w2))

    error = y - o
    w2 += lr * np.dot(h.T, error * o * (1-o))
    w1 += lr * np.dot(X.T, np.dot(error * o * (1-o), w2.T) * h * (1-h))

print("Output after training:")
print(o)
