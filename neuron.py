
def relu(z):
    return max(0.0, z)

def neuron(inputs, weights, bias, activation):
    total = 0.0
    for x, w in zip(inputs, weights):
        total += x * w
    total += bias
    return activation(total)

inputs = [2.0, 3.0]
weights = [0.5, -1.0]
bias = 1.0

output = neuron(inputs, weights, bias, relu)
print(output)