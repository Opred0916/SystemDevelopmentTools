import torch
from torch import nn

torch.manual_seed(3)

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

with torch.no_grad():
    test_x = torch.tensor([[3.0], [4.0]])
    test_y = model(test_x)

    print("Predictions:")
    print(test_y)
    