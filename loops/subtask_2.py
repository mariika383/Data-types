def even_nums(numbers):
    result = []

    for num in numbers:
        if num % 2 == 0:
            result.append(num)

    return result

print(even_nums([10, 0, -15, -98, 105, 10002, 32.4]))