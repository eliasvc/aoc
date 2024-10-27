import unittest
from day1 import move, basement_position


class TestDay1(unittest.TestCase):
    def test_move(self):
        tests = [
            {"input": "(())", "expected": 0},
            {"input": "()()", "expected": 0},
            {"input": "(()(()(", "expected": 3},
            {"input": "(((", "expected": 3},
            {"input": "))(((((", "expected": 3},
            {"input": "())", "expected": -1},
            {"input": "))(", "expected": -1},
            {"input": ")))", "expected": -3},
            {"input": ")())())", "expected": -3},
        ]
        for test in tests:
            result = move(0, test["input"])
            self.assertEqual(result, test["expected"])

    def test_basement_position(self):
        tests = [{"input": ")", "expected": 1},
                 {"input": "()())", "expected": 5}]

        for test in tests:
            result = basement_position(0, test["input"])
            self.assertEqual(result, test["expected"])


if __name__ == "__main__":
    unittest.main()
