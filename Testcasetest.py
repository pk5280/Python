import unittest


class TestListElements(unittest.TestCase):
    def setUp(self):
        self.expected = ['foo', 'bar', 'baz']
        self.result = ['baz', 'foo', 'bar']

    def test_count_eq(self):
        """Will succeed"""
        self.assertCountEqual(self.result, self.expected)

if __name__ == "__main__":
    unittest.main()