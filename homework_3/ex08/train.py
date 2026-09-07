import torch
from torch import nn

torch.manual_seed(2)

x = torch.linspace(-1, 1, 21).reshape(-1, 1)
y = 2 * x + 1

model = nn.Linear(1, 1)
loss_fn = nn.MSELoss()
opt = torch.optim.SGD(model.parameters(), lr=0.1)

for epoch in range(1, 51):
    pred = model(x)
    loss = loss_fn(pred, y)

    opt.zero_grad()
    loss.backward()
    opt.step()

    if epoch % 10 == 0:
        print(f"epoch {epoch}: loss = {loss.item():.6f}")
        