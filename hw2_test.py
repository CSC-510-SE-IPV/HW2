import hw2_debugging

def test_merge_sort1():
    assert hw2_debugging.mergeSort([2,1,3]) == [1,2,3]

def test_merge_sort2():
    assert hw2_debugging.mergeSort([1, 2, 3, 4]) == [1, 2, 3, 4]
    
def test_merge_sort3():
    assert hw2_debugging.mergeSort([5, 1, 3, 5, 2]) == [1, 2, 3, 5, 5]

def test_merge_sort4():
    assert hw2_debugging.mergeSort([]) == []    