import unittest
from app.multi import multiplicación
class TestMulti(unittest.TestCase):
    def test_1(self):
        a = 2
        b = 3
        self.assertEqual(multiplicación(a,b),6)