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
#
#     def test_fails(self):
#         assert 0 == 1
          
   

class TestPass(TestCase):
    def test_passes(self):
        assert 6 == 6
    
    def this_also_passes(self):
        assert 'a' == 'a'
