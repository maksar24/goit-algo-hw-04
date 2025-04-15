def merge(left, right):
    merged = []
    left_i = 0
    right_i = 0

    while left_i < len(left) and right_i < len(right):
        if left[left_i] <= right[right_i]:
            merged.append(left[left_i])
            left_i += 1
        else:
            merged.append(right[right_i])
            right_i += 1

    while left_i < len(left):
        merged.append(left[left_i])
        left_i += 1

    while right_i < len(right):
        merged.append(right[right_i])
        right_i += 1

    return merged

def merge_k_lists(lists):
    if not lists:
        return []

    while len(lists) > 1:
        merged_lists = []

        for i in range(0, len(lists), 2):
            left = lists[i]
            right = lists[i + 1] if i + 1 < len(lists) else []
            merged_lists.append(merge(left, right))

        lists = merged_lists

    return lists[0]

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
