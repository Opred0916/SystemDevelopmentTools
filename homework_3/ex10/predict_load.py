import torch
from torch import nn

model = nn.Linear(1, 1)
model.load_state_dict(torch.load("model.pth", weights_only=True))
model.eval()

with torch.no_grad():
    x = torch.tensor([[3.0]])
    y = model(x)

print(f"Prediction for 3: {y.item():.4f}")

