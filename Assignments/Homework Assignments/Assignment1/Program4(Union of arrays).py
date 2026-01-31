# You are given two arrays a[] and b[]. return the union of the two arrays in any order
def union_arrays(a, b):
    seen = {}
    result = []

    for x in a:
        if x not in seen:
            seen[x] = True
            result.append(x)

    for x in b:
        if x not in seen:
            seen[x] = True
            result.append(x)

    return result


a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
print(union_arrays(a, b))
