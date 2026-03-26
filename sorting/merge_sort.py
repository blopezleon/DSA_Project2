def _merge(left: list[dict], right: list[dict], key: str) -> list[dict]:
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
       
        if left[i][key] <= right[j][key]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

   
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def merge_sort(songs: list[dict], key: str) -> list[dict]:
    if len(songs) <= 1:
        return list(songs)

    mid = len(songs) // 2
    left_half  = songs[:mid]
    right_half = songs[mid:]

    sorted_left  = merge_sort(left_half,  key)
    sorted_right = merge_sort(right_half, key)

    return _merge(sorted_left, sorted_right, key)

def merge_sort_iterative(songs: list[dict], key: str) -> list[dict]:
    arr = list(songs)
    n = len(arr)
    if n <= 1:
        return arr

    width = 1
    while width < n:
        for left_start in range(0, n, 2 * width):
            mid       = min(left_start + width, n)
            right_end = min(left_start + 2 * width, n)

            left_part  = arr[left_start:mid]
            right_part = arr[mid:right_end]
            merged     = _merge(left_part, right_part, key)

            arr[left_start:left_start + len(merged)] = merged

        width *= 2  

    return arr