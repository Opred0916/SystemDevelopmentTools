def find_max(numbers):
    maximum = numbers[0]

    for i in range(len(numbers) + 1):
        if numbers[i] > maximum:
            maximum = numbers[i]

    return maximum


print(find_max([3, 7, 2, 9]))

