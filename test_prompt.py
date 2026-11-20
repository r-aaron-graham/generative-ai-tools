import unittest
from prompt import render


class PromptTests(unittest.TestCase):
    def test_literal_material(self):
        self.assertIn("$unknown", render("engineers", "$unknown"))

    def test_blank_inputs(self):
        for audience, material in (("", "text"), ("engineers", "  ")):
            with self.assertRaises(ValueError):
                render(audience, material)

    def test_length_limits(self):
        self.assertIn("x" * 200, render("x" * 200, "y" * 20000))
        for audience, material in (("x" * 201, "text"), ("engineers", "x" * 20001)):
            with self.assertRaises(ValueError):
                render(audience, material)


if __name__ == "__main__":
    unittest.main()
