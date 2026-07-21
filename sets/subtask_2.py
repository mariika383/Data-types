def is_subset(set1, set2):
    return set1.issubset(set2)

print(is_subset({1, 5, 9}, {"banana", True, 4}))
print(is_subset({7, 80}, {6, 7, 9, 80}))