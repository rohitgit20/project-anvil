from solution import second_largest

def test_normal_case():
    assert second_largest([1, 2, 3, 4]) == 3

def test_unsorted_list():
    assert second_largest([10, 5, 8, 20]) == 10

def test_duplicates():
    assert second_largest([5, 5, 5, 3]) == 3

def test_all_same():
    assert second_largest([7, 7, 7]) == -1

def test_single_element():
    assert second_largest([10]) == -1

def test_negative_numbers():
    assert second_largest([-1, -2, -3]) == -2