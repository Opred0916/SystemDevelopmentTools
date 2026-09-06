def slow_task():
    total = 0
    for i in range(1000000):
        total += i
    return sum(range(1000000))


print(slow_task())