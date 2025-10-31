import unittest

from src.sql_gen import *
from src.actions import add_actions, ActionType


class TestGenEmailAccount(unittest.TestCase):
    def test_gen_email_account_none(self):
        # gen_email_account is unimplemented and should return None
        print("\n\n=============\nTest gen_email_account returns None:\n=============")
        self.assertIsNone(gen_email_account())


class TestGenTicketTriggersSubstring(unittest.TestCase):
    def test_new_ticket_contains_email_and_account(self):
        query = gen_new_ticket_trigger("a@b.com", "5")

        print("\n\n=============\nTest gen_new_ticket_trigger contains expected substrings:\n=============")
        print(f"\n------\nResult\n------\n{query}\n")

        self.assertIn("Email Trigger for a@b.com", query)
        # check that the SetEmailAccount block contains the provided account id (escaped in JSON)
        self.assertIn('\\\"email_account_id\\\": \\\"5\\\"', query)
        # terms should include a CheckEmailToAddress term
        self.assertIn('CheckEmailToAddress', query)

    def test_update_ticket_with_actions_contains_fields(self):
        actions = add_actions([
            (ActionType.SET_CUSTOM_FIELD, ("19", "20")),
            (ActionType.SET_AGENT, "2")
        ])
        query = gen_ticket_update_trigger("support@example.com", "19", "20", "5", actions)

        print("\n\n=============\nTest gen_ticket_update_trigger contains expected substrings:\n=============")
        print(f"\n------\nResult\n------\n{query}\n")

        self.assertIn("Update Trigger for support@example.com", query)
        self.assertIn('CheckTicketField19', query)
        self.assertIn('SetTicketField19', query)
        self.assertIn('SetAgent', query)
        self.assertIn('\\\"email_account_id\\\": \\\"5\\\"', query)


if __name__ == "__main__":
    unittest.main()
