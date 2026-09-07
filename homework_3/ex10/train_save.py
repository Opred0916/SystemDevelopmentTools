import torch
from torch import nn

torch.manual_seed(4)

x = torch.tensor([[-1.0], [0.0], [1.0], [2.0]])
y = 2 * x + 1

model = nn.Linear(1, 1)
loss_fn = nn.MSELoss()
opt = torch.optim.SGD(model.parameters(), lr=0.1)

for _ in range(100):
    pred = model(x)
    loss = loss_fn(pred, y)

    opt.zero_grad()
    loss.backward()
    opt.step()

torch.save(model.state_dict(), "model.pth")
print("Model saved to model.pth")

