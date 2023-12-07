"""
This file will contain test cases for the automatic evaluation of your
solution in main/lab.py. You should not modify the code in this file. You should
also manually test your solution by running main/app.py.
"""
import unittest
import requests

from main.lab import llm


class TestLLMResponse(unittest.TestCase):

    """
    Your prompt should make the LLM correctly generate the response
    "the car is red" for the input "red, car".
    """

    def test_fewshot_1(self):
        result = llm("red, car").lower()
        self.assertIn("the car is red", result)

    """
    Your prompt should make the LLM correctly generate the response
    "the sky is blue" for the input "blue, sky".
    """

    def test_fewshot_2(self):
        result = llm("blue, sky").lower()
        self.assertIn("the sky is blue", result)

    """
    Your prompt should make the LLM correctly generate the response
    "the banana is yellow" for the input "yellow, banana".
    """

    def test_fewshot_3(self):
        result = llm("yellow, banana").lower()
        self.assertIn("the banana is yellow", result)

if __name__ == '__main__':
    unittest.main()
