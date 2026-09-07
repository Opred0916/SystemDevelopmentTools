import torch
from torch import nn

torch.manual_seed(1)

x = torch.linspace(-1, 1, 21).reshape(-1, 1)
y = 2 * x + 1

model = nn.Linear(1, 1)
loss_fn = nn.MSELoss()
opt = torch.optim.SGD(model.parameters(), lr=0.1)

for epoch in range(50):
    pred = model(x)
    loss = loss_fn(pred, y)

    opt.zero_grad()
    loss.backward()
    opt.step()

print(f"Final loss: {loss.item():.6f}")
print(f"Weight: {model.weight.item():.4f}")
print(f"Bias: {model.bias.item():.4f}")
