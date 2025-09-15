# test_main.py

import unittest
from main import process_user_input
from memory import Memory


class DummyAI:
    """Mock AI for testing."""
    def ask(self, user_input: str) -> str:
        if "add" in user_input:
            return "print(2+2)"
        return "Hello from AI"


class TestMain(unittest.TestCase):
    def setUp(self):
        self.ai = DummyAI()
        self.memory = Memory()

    def test_simple_response(self):
        output = process_user_input("hello", self.ai, self.memory)
        self.assertIn("Hello from AI", output["response"])
        self.assertIsNone(output["execution"])  # no code execution

    def test_code_execution(self):
        output = process_user_input("add numbers", self.ai, self.memory)
        self.assertEqual(output["execution"].strip(), "4")  # code runs correctly


if __name__ == "__main__":
    unittest.main()
