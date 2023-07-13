import unittest
from models import State


class StateTest(unittest.TestCase):

    def test_state_initialization(self):
        state = State()
        self.assertEqual(state.name, "")

    def test_state_attributes(self):
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")


if __name__ == '__main__':
    unittest.main()
