import nose
import temperature as temp
import math_w as math


########################################################
#Test temperature module

def test_to_celsius():
    '''Test function for to_celsius'''
    assert(temp.to_celsius(32) == 0)

def test_above_freezing():
    '''Test function for above_freezing.'''
    assert(temp.above_freezing(10) == True)

def test_below_freezing():
    '''Test function for above_freezing.'''
    assert(temp.below_freezing(-10) == True)

def test_at_freezing():
    '''Test function for above_freezing.'''
    assert(temp.at_freezing(0) == True)


########################################################
#Test math_w module
def test_add():
    """Test function for add"""
    assert(math.add(10, 10) == 20)

def test_sub():
    """Test function for sub"""
    assert(math.sub(10, 10) == 0)

def test_multi():
    """Test function for multi"""
    assert(math.multi(10, 10) == 100)

def test_divide():
    """Test function for divide"""
    assert(math.divide(10, 10) == 1)

def test_pow():
    """Test function for pow"""
    assert(math.pow(2, 2) == 4)

def test_root():
    """Test function for root"""
    assert(math.root(25, 2) == 5)

def test_remn():
    """Test function for remn"""
    assert(math.remn(25, 2) == 1)

def test_abs():
    """Test function for abs"""
    assert(math.abs(-25) == 25)

def test_cpi():
    """Test fuction for cpi"""
    assert(math.cpi(3.14) == True)

if __name__ == '__main__' :
    nose.runmodule()