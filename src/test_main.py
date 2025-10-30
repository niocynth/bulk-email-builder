import unittest

from src.main import *

class TestGenNewTicketTrigger(unittest.TestCase):
    def test_minimal(self):
        query = gen_new_ticket_trigger("support@example.com", "5")
        validation = 'INSERT INTO ticket_triggers (title, event_trigger, event_flags, by_agent_mode, by_user_mode, by_app_mode, is_enabled, is_hidden, is_editable, terms, actions, run_order) VALUES ("Email Trigger for support@example.com", "newticket", "", "web,email", "email", "", 1, 0, 1, "{\\\"@DATA\\\": {\\\"terms\\\": [{\\\"set_terms\\\": [{\\\"op\\\": \\\"is\\\", \\\"type\\\": \\\"CheckEmailToAddress\\\", \\\"options\\\": {\\\"email\\\": \\\"support@example.com\\\"}}]}, {\\\"set_terms\\\": [{\\\"op\\\": \\\"is\\\", \\\"type\\\": \\\"CheckEmailCcAddress\\\", \\\"options\\\": {\\\"email\\\": \\\"support@example.com\\\"}}]}, {\\\"set_terms\\\": [{\\\"op\\\": \\\"contains\\\", \\\"type\\\": \\\"CheckEmailHeader\\\", \\\"options\\\": {\\\"name\\\": \\\"Received\\\", \\\"value\\\": \\\"support@example.com\\\"}}]}], \\\"version\\\": 1}, \\\"@CLASS\\\": \\\"Application\\\\\\\\DeskPRO\\\\\\\\Tickets\\\\\\\\Triggers\\\\\\\\TriggerTerms\\\"}", "{\\\"@DATA\\\": {\\\"actions\\\": [{\\\"type\\\": \\\"SetEmailAccount\\\", \\\"options\\\": {\\\"email_account_id\\\": \\\"5\\\"}}], \\\"version\\\": 1}, \\\"@CLASS\\\": \\\"Application\\\\\\\\DeskPRO\\\\\\\\Tickets\\\\\\\\Triggers\\\\\\\\TriggerActions\\\"}", 100);'
        
        print("\n\n=============\nTest Minimal:\n=============")
        print(f"\n--------\nExpected\n--------\n{validation}")
        print(f"\n------\nResult\n------\n{query}\n")

        self.assertEqual(query, validation)

if __name__ == "__main__":
    unittest.main()