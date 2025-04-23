def merge_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left: list, right: list) -> list:
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def get_min_k_number(arr: list, k: int) -> int | None:
    sorted_arr = quick_sort(arr)
    if k >= len(sorted_arr) | k < 0:
        return None
    return sorted_arr[k]


def get_min_max(arr: list):
    sorted_arr = merge_sort(arr)
    return (sorted_arr[0], sorted_arr[len(sorted_arr) - 1])


if __name__ == "__main__":
    source_arr = [47, 11, 7, 13, 2, -1, 267, -46, 0]
    print(f"Source array: {source_arr}")
    result = get_min_max(source_arr)
    print(f"MIN and MAX result: {result}")
    k = 3
    min_k_number = get_min_k_number(source_arr, k)
    print(f"MIN {k} number is: {min_k_number}")
