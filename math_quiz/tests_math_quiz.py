import unittest
from math_quiz import generate_random_integer, generate_random_operator, perform_operation


class TestMathGame(unittest.TestCase):

    def generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num =  generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def generate_random_operator(self):
        rand_operator = generate_random_operator()
         self.assertIn(rand_operator, operators)
        pass

    def perform_operation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (10, 5, '-', '10 - 5', 5),
                (3, 6, '*', '3 * 6', 18),
                (8, 4, '/', '8 / 4', 2),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                result = perform_operation(num1, num2, operator)
                self.assertEqual(result, expected_answer)
                pass

if __name__ == "__main__":
    unittest.main()
