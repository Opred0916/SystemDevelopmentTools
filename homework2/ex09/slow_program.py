def slow_task():
    total = 0
    for i in range(1000000):
        total += i
    return total


def fast_task():
    return sum(range(1000))


print(slow_task())
print(fast_task())

