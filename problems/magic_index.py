def magic_index(A):
    def binary_search(A, left_idx, right_idx):
        if left_idx > right_idx:
            return -1
        mid_idx = (left_idx + right_idx) // 2
        if A[mid_idx] == mid_idx:
            return mid_idx
        elif A[mid_idx] < mid_idx:
            return binary_search(A, mid_idx + 1, right_idx)
        else:
            return binary_search(A, left_idx, mid_idx - 1)
    return binary_search(A, 0, len(A) - 1)

if __name__ == "__main__":
    print(magic_index([-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]))