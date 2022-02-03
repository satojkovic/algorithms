def sparse_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == '':
            l, r = mid - 1, mid + 1
            while True:
                if l < left and r > right:
                    return -1
                elif r <= right and arr[r] != '':
                    mid = r
                    break
                elif l >= left and arr[l] != '':
                    mid = l
                    break
                l -= 1
                r += 1
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def sparse_search_r(arr, target):
    def _sparse_search_r(arr, target, left, right):
        if left > right:
            return -1
        mid = left + (right - left) // 2
        if arr[mid] == '':
            l, r = mid - 1, mid + 1
            while True:
                if l < left and r > right:
                    return -1
                elif r <= right and arr[r] != '':
                    mid = r
                    break
                elif l >= left and arr[l] != '':
                    mid = l
                    break
                l -= 1
                r += 1
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return _sparse_search_r(arr, target, mid + 1, right)
        else:
            return _sparse_search_r(arr, target, left, mid - 1)
    return _sparse_search_r(arr, target, 0, len(arr) - 1)


def test_sparse_search():
    assert sparse_search(["at", "", "", "", "ball", "",
                         "", "car", "", "", "dad", "", ""], "ball") == 4
    assert sparse_search(["at", "", "", "", "ball", "",
                         "", "car", "", "", "dad", "", ""], "dad") == 10
    assert sparse_search(["at", "", "", "", "ball", "",
                         "", "car", "", "", "dad", "", ""], "cars") == -1
    assert sparse_search(["", "", ""], "test") == -1


def test_sparse_search_r():
    assert sparse_search_r(["at", "", "", "", "ball", "",
                            "", "car", "", "", "dad", "", ""], "ball") == 4
    assert sparse_search_r(["at", "", "", "", "ball", "",
                            "", "car", "", "", "dad", "", ""], "dad") == 10
    assert sparse_search_r(["at", "", "", "", "ball", "",
                            "", "car", "", "", "dad", "", ""], "cars") == -1
    assert sparse_search_r(["", "", ""], "test") == -1
