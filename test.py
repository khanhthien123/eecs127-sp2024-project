import torch

x = torch.Tensor([[1, 2, 3], [0, 5, 0]])
y = x[0] <= x[1]

print(x.data)