import unittest

from src.actions import *


class TestAddActionsEdgeCases(unittest.TestCase):
    def test_add_actions_empty(self):
        query = add_actions([])
        validation = ''

        print("\n\n=============\nTest Add Actions Empty:\n=============")
        print(f"\n--------\nExpected\n--------\n{validation}")
        print(f"\n------\nResult\n------\n{query}\n")

        self.assertEqual(query, validation)

    def test_add_actions_unknown_raises(self):
        # If an unknown action type is provided we expect an exception
        print("\n\n=============\nTest Add Actions Unknown Type Raises:\n=============")
        with self.assertRaises(Exception):
            add_actions([("UNKNOWN", "1")])


if __name__ == "__main__":
    unittest.main()
