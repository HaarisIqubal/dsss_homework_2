import unittest
from math_quiz import input_number, choose_sign, apply_operation
class TestMathGame(unittest.TestCase):
    def test_input_number(self):

        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values

            rand_num = input_number(min_val, max_val)

            self.assertTrue(min_val <= rand_num <= max_val)

    def test_choose_sign(self):
        # TODO
        # Test if the sign generated is valid from sign array or not
        valid_signs = ['+', '-', '*']
        for _ in range(len(valid_signs)):
            result = choose_sign()
            self.assertIn(result, valid_signs, f"The result '{result}' is not a valid mathematical sign")
            pass

    def test_apply_operation(self):

            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (12, 5, '*', '12 * 5', 60),
                (5, 7, '-', '5 - 7', -2),
                (8, 8, '+', '8 + 8', 16),
                (9, 4, '-', '9 - 4', 5)
            ]


            for num1, num2, operator, expected_problem, expected_answer in test_cases:

                # TODO
                PROBLEM, ANSWER = apply_operation(num1,num2,operator)
                self.assertEqual(expected_problem,PROBLEM, f"The expected problem don't match the problem. Expected Problem: {expected_problem}, Problem: {PROBLEM}")
                self.assertEqual(expected_answer,ANSWER, f"The expected problem don't match the problem. Expected Answer: {expected_answer}, Answer: {ANSWER}")
                pass


if __name__ == "__main__":

    unittest.main()

