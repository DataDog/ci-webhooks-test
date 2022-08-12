import os
from unittest import TestCase
from random import randrange

def my_func():
    raise ValueError

class TestTrivial(TestCase):
    def test_pass(self):
        assert 4 == 4
    
    def test_flaky(self):
        build_num = os.getenv('BUILDKITE_BUILD_NUMBER')
        if build_num:
            assert int(build_num) % 2 == 0
        else:
            assert randrange(10) > 5
    
    def test_fail(self):
        assert 5 == 7
    
    def test_1(self):
        assert my_func() == 4
   
