def nand(left, right):
    if (left and right):
        return False
    else:
        return True
def not_(x):
    if x:
        return False
    else:
        return True
    
#def and_(l, r):
#    if (l is False


def test_nand_t_t():
    assert nand(True, True) == False

def test_nand_t_f():
    assert nand(True, False) == True

def test_nand_f_t():
    assert nand(False, True) == True

def test_nand_f_f():
    assert nand(False, False) == True

def test_nand_t_t():
    assert nand(True, True) == False

def test_not_t():
    assert not_(True) == False
def test_not_f():
    assert not_(False) == True
#def test_nand_bogus_type():
#    nand("this is a string which unfortunately is truthy in Python", (,))
