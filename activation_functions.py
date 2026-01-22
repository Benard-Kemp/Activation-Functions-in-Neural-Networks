import math

def sigmoid(z):
    return 1 / (1 + math.exp(-z))


def relu(z):
    return max(0.0, z)

print(sigmoid(-2.0))  # ~0.12
print(sigmoid(0.0))   # 0.5
print(sigmoid(2.0))   # ~0.88

print(relu(-3.0))  # 0.0
print(relu(2.5))   # 2.5

