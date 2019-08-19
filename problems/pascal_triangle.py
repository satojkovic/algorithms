# Time complexity: O(num_rows^2)
#  append ops is O(1)
#  for each iteration of the outer loop, the inner loop runs row number times.
#  therefore, 1 + 2 + 3 + .. + num_rows = (num_rows * (num_rows + 1)) / 2 => num_rows^2
#
# Space complexity: O(num_rows^2)
#  we need to store each rows
#  therefore, 1 + 2 + 3 + ... + num_rows => num_rows^2
def pascal_triangle1(num_rows):
    ret = []
    for i in range(num_rows):
        elems = []
        for j in range(0, i + 1, 1):
            if j == 0 or j == (i + 1) - 1:
                elems.append(1)
            else:
                elems.append(ret[i-1][j] + ret[i-1][j-1])
        ret.append(elems)
    return ret
