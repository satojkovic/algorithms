def count_points(rings):
    rod = [0 for _ in range(10)]
    for i in range(0, len(rings), 2):
        color = 1 if rings[i] == 'R' else 2 if rings[i] == 'G' else 4
        rod[int(rings[i+1])] |= color
    return sum([1 for c in rod if c == 7])


def test_count_points():
    assert count_points("B0B6G0R6R0R6G9") == 1
    assert count_points("B0R0G0R9R0B0G0") == 1
    assert count_points("G4") == 0
