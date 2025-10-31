import unittest

from src.sql_gen import *
from src.actions import *

class TestGenNewTicketTrigger(unittest.TestCase):
    def test_minimal(self):
        query = gen_new_ticket_trigger("support@example.com", "5")
        validation = 'INSERT INTO ticket_triggers (title, event_trigger, event_flags, by_agent_mode, by_user_mode, by_app_mode, is_enabled, is_hidden, is_editable, terms, actions, run_order) VALUES ("Email Trigger for support@example.com", "newticket", "", "web,email", "email", "", 1, 0, 1, "{\\\"@DATA\\\": {\\\"terms\\\": [{\\\"set_terms\\\": [{\\\"op\\\": \\\"is\\\", \\\"type\\\": \\\"CheckEmailToAddress\\\", \\\"options\\\": {\\\"email\\\": \\\"support@example.com\\\"}}]}, {\\\"set_terms\\\": [{\\\"op\\\": \\\"is\\\", \\\"type\\\": \\\"CheckEmailCcAddress\\\", \\\"options\\\": {\\\"email\\\": \\\"support@example.com\\\"}}]}, {\\\"set_terms\\\": [{\\\"op\\\": \\\"contains\\\", \\\"type\\\": \\\"CheckEmailHeader\\\", \\\"options\\\": {\\\"name\\\": \\\"Received\\\", \\\"value\\\": \\\"support@example.com\\\"}}]}], \\\"version\\\": 1}, \\\"@CLASS\\\": \\\"Application\\\\\\\\DeskPRO\\\\\\\\Tickets\\\\\\\\Triggers\\\\\\\\TriggerTerms\\\"}", "{\\\"@DATA\\\": {\\\"actions\\\": [{\\\"type\\\": \\\"SetEmailAccount\\\", \\\"options\\\": {\\\"email_account_id\\\": \\\"5\\\"}}], \\\"version\\\": 1}, \\\"@CLASS\\\": \\\"Application\\\\\\\\DeskPRO\\\\\\\\Tickets\\\\\\\\Triggers\\\\\\\\TriggerActions\\\"}", 100);'
        
        print("\n\n=============\nTest New Ticket Trigger Minimal:\n=============")
        print(f"\n--------\nExpected\n--------\n{validation}")
        print(f"\n------\nResult\n------\n{query}\n")

        self.assertEqual(query, validation)

class TestGenTicketUpdateTrigger(unittest.TestCase):
    def test_minimal(self):
        query = gen_ticket_update_trigger("support@example.com", "19", "20", "5")
        validation = 'INSERT INTO ticket_triggers (title, event_trigger, event_flags, by_agent_mode, by_user_mode, by_app_mode, is_enabled, is_hidden, is_editable, terms, actions, run_order) VALUES ("Update Trigger for support@example.com", "update", "", "web", "", "", 1, 0, 1, "{\\\"@DATA\\\": {\\\"terms\\\": [{\\\"set_terms\\\": [{\\\"op\\\": \\\"is\\\", \\\"type\\\": \\\"CheckTicketField19\\\", \\\"options\\\": {\\\"value\\\": [\\\"20\\\"], \\\"field_id\\\": \\\"19\\\", \\\"type_name\\\": \\\"choice\\\"}}]}], \\\"version\\\": 1}, \\\"@CLASS\\\": \\\"Application\\\\\\\\DeskPRO\\\\\\\\Tickets\\\\\\\\Triggers\\\\\\\\TriggerTerms\\\"}", "{\\\"@DATA\\\": {\\\"actions\\\": [{\\\"type\\\": \\\"SetEmailAccount\\\", \\\"options\\\": {\\\"email_account_id\\\": \\\"5\\\"}}], \\\"version\\\": 1}, \\\"@CLASS\\\": \\\"Application\\\\\\\\DeskPRO\\\\\\\\Tickets\\\\\\\\Triggers\\\\\\\\TriggerActions\\\"}", 100);'

        print("\n\n=============\nTest Ticket Update Trigger Minimal:\n=============")
        print(f"\n--------\nExpected\n--------\n{validation}")
        print(f"\n------\nResult\n------\n{query}\n")

        self.assertEqual(query, validation)

class TestGenTriggersWithActions(unittest.TestCase):
    def test_new_ticket_with_actions(self):
        actions = add_actions([
            (ActionType.SET_SLA, ["1"]),
            (ActionType.SET_DEPARTMENT, "2"),
            (ActionType.SET_URGENCY, 5)
        ])
        query = gen_new_ticket_trigger("support.example.com", "5", "19", "20", actions)
        validation = 'INSERT INTO ticket_triggers (title, event_trigger, event_flags, by_agent_mode, by_user_mode, by_app_mode, is_enabled, is_hidden, is_editable, terms, actions, run_order) VALUES ("Email Trigger for support.example.com", "newticket", "", "web,email", "email", "", 1, 0, 1, "{\\\"@DATA\\\": {\\\"terms\\\": [{\\\"set_terms\\\": [{\\\"op\\\": \\\"is\\\", \\\"type\\\": \\\"CheckEmailToAddress\\\", \\\"options\\\": {\\\"email\\\": \\\"support.example.com\\\"}}]}, {\\\"set_terms\\\": [{\\\"op\\\": \\\"is\\\", \\\"type\\\": \\\"CheckEmailCcAddress\\\", \\\"options\\\": {\\\"email\\\": \\\"support.example.com\\\"}}]}, {\\\"set_terms\\\": [{\\\"op\\\": \\\"contains\\\", \\\"type\\\": \\\"CheckEmailHeader\\\", \\\"options\\\": {\\\"name\\\": \\\"Received\\\", \\\"value\\\": \\\"support.example.com\\\"}}]}, {\\\"set_terms\\\": [{\\\"op\\\": \\\"is\\\", \\\"type\\\": \\\"CheckTicketField19\\\", \\\"options\\\": {\\\"value\\\": [\\\"20\\\"], \\\"field_id\\\": \\\"19\\\", \\\"type_name\\\": \\\"choice\\\"}}]}], \\\"version\\\": 1}, \\\"@CLASS\\\": \\\"Application\\\\\\\\DeskPRO\\\\\\\\Tickets\\\\\\\\Triggers\\\\\\\\TriggerTerms\\\"}", "{\\\"@DATA\\\": {\\\"actions\\\": [{\\\"type\\\": \\\"SetEmailAccount\\\", \\\"options\\\": {\\\"email_account_id\\\": \\\"5\\\"}}, {\\\"type\\\": \\\"SetTicketField19\\\", \\\"options\\\": {\\\"op\\\": \\\"set\\\", \\\"value\\\": \\\"20\\\"}}, {\\\"type\\\": \\\"SetSlas\\\", \\\"options\\\": {\\\"add_sla_ids\\\": [\\\"1\\\"], \\\"remove_sla_ids\\\": []}}, {\\\"type\\\": \\\"SetDepartment\\\", \\\"options\\\": {\\\"department_id\\\": \\\"2\\\"}}, {\\\"type\\\": \\\"SetUrgency\\\", \\\"options\\\": {\\\"mode\\\": \\\"set\\\", \\\"urgency\\\": 5}}], \\\"version\\\": 1}, \\\"@CLASS\\\": \\\"Application\\\\\\\\DeskPRO\\\\\\\\Tickets\\\\\\\\Triggers\\\\\\\\TriggerActions\\\"}", 100);'
        print(f"\n--------\nExpected\n--------\n{validation}")
        print(f"\n------\nResult\n------\n{query}\n")

        self.assertEqual(query, validation)

if __name__ == "__main__":
    unittest.main()