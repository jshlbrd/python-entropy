import unittest

from six import b

from entropy import shannon_entropy


class TestShannonEntropy(unittest.TestCase):
    def assert_entropy(self, data, expected):
        self.assertAlmostEqual(shannon_entropy(data), expected, places=3)

    def test_0(self):
        self.assert_entropy(b('\x00') * 1024, 0.0)

    def test_f(self):
        self.assert_entropy(b('\xff') * 1024, 0.0)

    def test_alternate_0f(self):
        self.assert_entropy(b('\x00\xff') * 512, 0.125)

    def test_alternate_f0(self):
        self.assert_entropy(b('\xff\x00') * 512, 0.125)

    def test_alternate_0cf(self):
        self.assert_entropy(b('\x00\xcc\xff') * 512, 0.198)

    def test_one(self):
        self.assert_entropy(b('').join(b(chr(i)) for i in range(256)), 1.0)
