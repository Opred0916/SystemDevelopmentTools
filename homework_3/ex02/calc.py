import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--a", type=float, required=True)
parser.add_argument("--b", type=float, required=True)

args = parser.parse_args()

print(f"sum = {args.a + args.b}")
print(f"product = {args.a * args.b}")