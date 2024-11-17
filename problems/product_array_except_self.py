def product_except_self(nums):
    # len(nums)が複数出てくるためnums_lenを用意
    nums_len = len(nums)

    # prefixとsuffixを用意
    prefix_products = [0] * nums_len
    suffix_products = [0] * nums_len
    # prefixとsuffixのproductsを計算
    for i in range(nums_len):
        prefix_products[i] = prefix_products[i-1] * nums[i] if i != 0 else nums[i]
    # suffixの場合は、numsを逆順で作る
    for i in range(nums_len - 1, -1, -1):
        suffix_products[i] = suffix_products[i+1] * nums[i] if i != nums_len - 1 else nums[i]

    # answerはprefix[i-1] * suffix[i+1]で求める
    # ただし、i-1とi+1が範囲内であることをチェックする
    # 範囲外の場合はproductに影響しない1とする
    # prefixの末尾とsuffixの先頭はすべての要素のproductになるので使われない
    answers = []
    for i in range(nums_len):
        prefix = prefix_products[i-1] if i - 1 >= 0 else 1
        suffix = suffix_products[i+1] if i + 1 < nums_len else 1
        answers.append(prefix * suffix)
    return answers


def test_product_except_self():
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert product_except_self([1, 1, 1]) == [1, 1, 1]
    assert product_except_self([10, 3]) == [3, 10]

if __name__ == '__main__':
    print(product_except_self([1, 2, 3, 4]))
