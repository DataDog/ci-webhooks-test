from unittest import TestCase
from random import randrange


class TestTrivial(TestCase):
    def test_pass(self):
        assert 4 == 4
    
    def test_flaky(self):
        assert randrange(10) > 5
        
    def test_new_flaky(self):
        assert randrange(10) > 5
    
    def test_fail(self):
        assert 5 == 7
