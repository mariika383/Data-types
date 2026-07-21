def common(list1, list2):
    result = []

    for i in list1:
        if i in list2:
            result.append(i)

    return result

print(common(["apple", 2, False, "pineapple"], [4, 6, True, 2, "apple"]))