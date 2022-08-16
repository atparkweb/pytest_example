from unittest import TestCase
import unittest

class TryTesting(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)

    @unittest.skip("This always fails")
    def test_always_fails(self):
        self.assertTrue(False)
