def merged_dicts(dict1, dict2):
    merge_dict = dict1 | dict2
    print(merge_dict)

info1 = {
    "Name": "Max",
    "age": 10
}

info2 = {
    "is present": True,
    "grade": 5
}

merged_dicts(info1, info2)
