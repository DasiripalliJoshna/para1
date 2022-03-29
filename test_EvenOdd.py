import EvenOdd
import pytest

@pytest.mark.parametrize("a,result",[(10,True),(15,False),(12,True),(23,False),(2,True)])
def test_EvenOdd(a,result):
    ans=EvenOdd.Check_Even(a)
    assert ans==result