def daily_temperatures_bf(temperatures):
    answer = []
    for i, temp in enumerate(temperatures):
        diff = 0
        for j in range(i + 1, len(temperatures)):
            if temperatures[j] > temp:
                diff = j - i
                break
        answer.append(diff)
    return answer


def test_daily_temperatures_bf():
    assert daily_temperatures_bf([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
    assert daily_temperatures_bf([30,40,50,60]) == [1,1,1,0]
    assert daily_temperatures_bf([30,60,90]) == [1, 1, 0]
    assert daily_temperatures_bf([10]) == [0]
    assert daily_temperatures_bf([20, 20, 20, 20, 20]) == [0, 0, 0, 0, 0]
