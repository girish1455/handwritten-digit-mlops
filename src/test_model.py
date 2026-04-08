
import unittest
import os

class TestModel(unittest.TestCase):

    def test_model_exists(self):
        self.assertTrue(os.path.exists("models/model.pkl"))

if __name__ == "__main__":
    unittest.main()
