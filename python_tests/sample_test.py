from unittest import TestCase


class TestTrivial(TestCase):
    def test_pass(self):
        assert 4 == 4
    
    def test_fail(self):
        assert 3 == 1
