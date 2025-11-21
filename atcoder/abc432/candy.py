def solve_candy_problem(N, X, Y, A):
    """
    飴の問題を解く関数。

    Args:
        N: 子供の数
        X: 小さな飴の重さ
        Y: 大きな飴の重さ
        A: 各子供がもらう飴の総数のリスト (A_1, A_2, ..., A_N)

    Returns:
        条件を満たす配り方が存在すれば、大きな飴の総数の最大値 (int)。
        存在しなければ -1。
    """

    # === ステップ 1: パラメータと定数の準備 ===
    diff_XY = Y - X

    # === ステップ 2: 絞り込み条件 2 (合同式/余り) のチェック ===
    # まず、基準となる余りを計算する
    # Aの要素は A[0] から A[N-1] まで
    if not A: # 子供がいないエッジケース
        return 0

    remainder_base = (A[0] * X) % diff_XY

    # 他のすべての子供について、余りが同じかチェックする
    for i in range(1, N):
        remainder_i = (A[i] * X) % diff_XY
        if remainder_i != remainder_base:
            # 一人でも余りが違えば、全員の体重を同じにすることは不可能
            return -1

    # もし、ここまで到達したら、すべての子供で余りが同じ R であることが保証される
    R = remainder_base

    # === ステップ 3: 絞り込み条件 1 (範囲) の計算 ===
    # TotalWeight が取りうる値の範囲 [W_min, W_max] を計算する
    # max(A_i) * X
    W_min = max(A) * X
    # min(A_i) * Y
    W_max = min(A) * Y

    if W_min > W_max:
        # 共通の重さが存在しうる範囲がない
        return -1

    # === ステップ 4: TotalWeight 候補の探索と、大きな飴の総数の最大値の探索 ===
    max_total_big_candies = -1 # まだ解が見つかっていないことを示す

    # TotalWeight の最初の候補を見つける
    # W_min 以上の、最初の「k * diff_XY + R」の形をした数
    first_candidate_W = W_min
    if first_candidate_W % diff_XY != R:
        # W_min の余りが R でない場合、次の R になるまで調整する
        first_candidate_W += (R - (first_candidate_W % diff_XY) + diff_XY) % diff_XY

    # 絞り込まれた TotalWeight 候補を、diff_XY 間隔でループする
    for total_weight in range(first_candidate_W, W_max + 1, diff_XY):

        # --- この total_weight が本当に実現可能か、チェックする ---
        is_possible = True
        current_total_big_candies = 0

        for i in range(N):
            # b_i = (TotalWeight - A_i * X) / (Y - X) を計算
            numerator = total_weight - (A[i] * X)

            # numerator は diff_XY で割り切れるはず (合同式のチェック済み)
            big_candies_i = numerator // diff_XY

            # b_i が満たすべき2つの条件をチェック
            # 1. b_i は 0 以上か？
            # 2. b_i は A_i 以下か？
            if not (0 <= big_candies_i <= A[i]):
                is_possible = False
                break # 一人でも条件を満たさなければ、この total_weight はダメ

            current_total_big_candies += big_candies_i

        # --- チェック結果の判定 ---
        if is_possible:
            # この total_weight は実現可能だった
            # 大きな飴の総数を、今までの最大値と比較して更新する
            if max_total_big_candies == -1 or current_total_big_candies > max_total_big_candies:
                max_total_big_candies = current_total_big_candies

    return max_total_big_candies


def solve_candy_binary_search(N, X, Y, A):
    sum_A = sum(A)
    sum_AX = sum(a * X for a in A)
    diff_XY = Y - X

    def check(B):
        # 判定問題: 大きな飴の総数を B 個にできるか？

        # ステップ1: TotalWeight候補 W を計算
        numerator_W = B * diff_XY + sum_AX
        if numerator_W % N != 0:
            return False
        W = numerator_W // N

        # ステップ2 & 3: 各子供の b_i が条件を満たすかチェック
        for i in range(N):
            numerator_b = W - A[i] * X

            # b_i が整数になるか
            if numerator_b % diff_XY != 0:
                return False
            b_i = numerator_b // diff_XY

            # 0 <= b_i <= A_i を満たすか
            if not (0 <= b_i <= A[i]):
                return False

        # すべてのチェックを通過
        return True

    # 二分探索の範囲を設定
    # low: 大きな飴が0個 (最小)
    # high: すべての飴が大きな飴 (最大)
    low = 0
    high = sum_A
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if check(mid):
            # mid 個は可能だった。もっと多くできるか試す。
            ans = mid
            low = mid + 1
        else:
            # mid 個は不可能だった。もっと少なくする必要がある。
            high = mid - 1

    return ans


def solve_candy_optimized(N, X, Y, A):
    sum_A = sum(A)
    sum_AX = sum(a * X for a in A)
    diff_XY = Y - X

    # ステップ1: TotalWeightの合同条件をチェック
    remainder_base = (A[0] * X) % diff_XY
    for i in range(1, N):
        if (A[i] * X) % diff_XY != remainder_base:
            return -1
    R = remainder_base

    # ステップ2: B の取りうる範囲 [B_min, B_max] を計算
    # B >= (N * a * X - sum_AX) / diff_XY for all a in A
    # B >= max((N * a * X - sum_AX) / diff_XY for a in A)
    lower_bounds_b = []
    for a in A:
        num = N * a * X - sum_AX
        # 天井関数 (ceil) を使う
        lower_bounds_b.append((num + diff_XY - 1) // diff_XY if num > 0 else num // diff_XY)
    B_min = max(lower_bounds_b)

    # B <= (N * a * Y - sum_AX) / diff_XY for all a in A
    # B <= min((N * a * Y - sum_AX) / diff_XY for a in A)
    upper_bounds_b = []
    for a in A:
        num = N * a * Y - sum_AX
        upper_bounds_b.append(num // diff_XY)
    B_max = min(upper_bounds_b)

    # ステップ3: [B_min, B_max] の範囲で、条件を満たす最大の B を探す
    if B_min > B_max:
        return -1

    # 私たちが探している B は、対応する W が合同条件を満たす必要がある。
    # W = (B * diff_XY + sum_AX) / N
    # W % diff_XY == R
    # ( (B * diff_XY + sum_AX) / N ) % diff_XY == R
    # この条件を満たす B を探す

    # B_max から逆順に探すのが一番早い
    for B in range(B_max, B_min - 1, -1):
        numerator_W = B * diff_XY + sum_AX
        if numerator_W % N == 0:
            W = numerator_W // N
            if W % diff_XY == R:
                # これが、条件を満たす最大の B
                return B

    return -1


N, X, Y = list(map(int, input().split()))
A = list(map(int, input().split()))
result = solve_candy_optimized(N, X, Y, A)
print(result)