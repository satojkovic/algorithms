def max_area(height):
    # amount of water (height[i] is range from 0)
    ret = 0
    # two pointer: left and right
    left, right = 0, len(height) - 1
    
    while left < right:
        min_height = min(height[left], height[right])
        amount = min_height * (right - left)
        ret = max(ret, amount)
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
    
    return ret


def test_max_area():
    assert max_area([1,8,6,2,5,4,8,3,7]) == 49
    assert max_area([1, 1]) == 1
    assert max_area([0, 0, 0, 0, 0]) == 0
    assert max_area([0, 10]) == 0