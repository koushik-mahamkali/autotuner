from .classic import insertion_sort
def counting_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    output = []
    for i, c in enumerate(count):
        output.extend([i] * c)
    return output

def radix_sort(arr):
    RADIX = 10
    placement = 1
    max_digit = max(arr)
    while placement <= max_digit:
        buckets = [[] for _ in range(RADIX)]
        for i in arr:
            tmp = int((i // placement) % RADIX)
            buckets[tmp].append(i)
        a = 0
        for b in range(RADIX):
            for i in buckets[b]:
                arr[a] = i
                a += 1
        placement *= RADIX
    return arr

def bucket_sort(arr):
    if not arr:
        return arr
    bucket_count = 10
    max_val = max(arr)
    min_val = min(arr)
    bucket_range = (max_val - min_val) / bucket_count
    buckets = [[] for _ in range(bucket_count)]
    for num in arr:
        index = int((num - min_val) // bucket_range)
        if index == bucket_count:
            index -= 1
        buckets[index].append(num)
    arr = []
    for bucket in buckets:
        arr.extend(sorted(bucket))
    return arr

def cycle_sort(arr):
    writes = 0
    for cycleStart in range(0, len(arr) - 1):
        item = arr[cycleStart]
        pos = cycleStart
        for i in range(cycleStart + 1, len(arr)):
            if arr[i] < item:
                pos += 1
        if pos == cycleStart:
            continue
        while item == arr[pos]:
            pos += 1
        arr[pos], item = item, arr[pos]
        while pos != cycleStart:
            pos = cycleStart
            for i in range(cycleStart + 1, len(arr)):
                if arr[i] < item:
                    pos += 1
            while item == arr[pos]:
                pos += 1
            arr[pos], item = item, arr[pos]
        writes += 1
    return arr

def flash_sort(arr):
    if len(arr) == 0:
        return arr
    n = len(arr)
    m = int(0.43 * n)
    min_val = min(arr)
    max_val = max(arr)
    if min_val == max_val:
        return arr
    l = [0] * m
    c = (m - 1) / (max_val - min_val)
    for i in range(n):
        k = int(c * (arr[i] - min_val))
        l[k] += 1
    for i in range(1, m):
        l[i] += l[i - 1]
    hold = arr[0]
    move = j = 0
    k = m - 1
    while move < n:
        while j > l[k] - 1:
            j += 1
            k = int(c * (arr[j] - min_val))
        flash = arr[j]
        while j != l[k]:
            k = int(c * (flash - min_val))
            l[k] -= 1
            flash, arr[l[k]] = arr[l[k]], flash
            move += 1
    return insertion_sort(arr)

def postman_sort(arr):
    return sorted(arr)  # Placeholder for research sort
