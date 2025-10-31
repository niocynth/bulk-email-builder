import unittest

from src.actions import *

class TestAddIndividualActions(unittest.TestCase):
    def test_add_sla_action_minimal(self):
        query = add_sla_action(["1"])
        validation = ', {\\\"type\\\": \\\"SetSlas\\\", \\\"options\\\": {\\\"add_sla_ids\\\": [\\\"1\\\"], \\\"remove_sla_ids\\\": []}}'

        print("\n\n=============\nTest Add SLA Action Minimal:\n=============")
        print(f"\n--------\nExpected\n--------\n{validation}")
        print(f"\n------\nResult\n------\n{query}\n")

        self.assertEqual(query, validation)

    def test_add_agent_followers_action_minimal(self):
        query = add_agent_followers_action(["29"])
        validation = ', {\\\"type\\\": \\\"SetAgentFollowers\\\", \\\"options\\\": {\\\"add_agent_ids\\\": [\\\"29\\\"]}}'

        print("\n\n=============\nTest Add Agent Followers Minimal:\n=============")
        print(f"\n--------\nExpected\n--------\n{validation}")
        print(f"\n------\nResult\n------\n{query}\n")

        self.assertEqual(query, validation)

    def test_add_department_action_minimal(self):
        query = add_department_action("2")
        validation = ', {\\\"type\\\": \\\"SetDepartment\\\", \\\"options\\\": {\\\"department_id\\\": \\\"2\\\"}}'

        print("\n\n=============\nTest Add Department Action Minimal:\n=============")
        print(f"\n--------\nExpected\n--------\n{validation}")
        print(f"\n------\nResult\n------\n{query}\n")

        self.assertEqual(query, validation)

    def test_add_agent_team_action_minimal(self):
        query = add_agent_team_action("2")
        validation = ', {\\\"type\\\": \\\"SetAgentTeam\\\", \\\"options\\\": {\\\"agent_team_id\\\": \\\"2\\\"}}'

        print("\n\n=============\nTest Add Agent Team Action Minimal:\n=============")
        print(f"\n--------\nExpected\n--------\n{validation}")
        print(f"\n------\nResult\n------\n{query}\n")

        self.assertEqual(query, validation)

    def test_set_urgency_action_minimal(self):
        query = set_urgency_action(8)
        validation = ', {\\\"type\\\": \\\"SetUrgency\\\", \\\"options\\\": {\\\"mode\\\": \\\"set\\\", \\\"urgency\\\": 8}}'

        print("\n\n=============\nTest Set Urgency Action Minimal:\n=============")
        print(f"\n--------\nExpected\n--------\n{validation}")
        print(f"\n------\nResult\n------\n{query}\n")

        self.assertEqual(query, validation)

    def test_add_labels_action_minimal(self):
        query = add_labels_action(["Financial"])
        validation = ', {\\\"type\\\": \\\"SetLabels\\\", \\\"options\\\": {\\\"add_labels\\\": [\\\"Financial\\\"], \\\"remove_labels\\\": []}}'

        print("\n\n=============\nTest Add Labels Action Minimal:\n=============")
        print(f"\n--------\nExpected\n--------\n{validation}")
        print(f"\n------\nResult\n------\n{query}\n")

        self.assertEqual(query, validation)
    
class TestAddActions(unittest.TestCase):
    def test_add_actions_minimal(self):
        actions = [
            (ActionType.SET_SLA, ["1"]),
            (ActionType.SET_AGENT_FOLLOWERS, ["29"]),
            (ActionType.SET_DEPARTMENT, "2"),
            (ActionType.SET_AGENT_TEAM, "2"),
            (ActionType.SET_URGENCY, 8),
            (ActionType.SET_LABELS, ["Financial"])
        ]
        query = add_actions(actions)
        validation = ', {\\\"type\\\": \\\"SetSlas\\\", \\\"options\\\": {\\\"add_sla_ids\\\": [\\\"1\\\"], \\\"remove_sla_ids\\\": []}}, {\\\"type\\\": \\\"SetAgentFollowers\\\", \\\"options\\\": {\\\"add_agent_ids\\\": [\\\"29\\\"]}}, {\\\"type\\\": \\\"SetDepartment\\\", \\\"options\\\": {\\\"department_id\\\": \\\"2\\\"}}, {\\\"type\\\": \\\"SetAgentTeam\\\", \\\"options\\\": {\\\"agent_team_id\\\": \\\"2\\\"}}, {\\\"type\\\": \\\"SetUrgency\\\", \\\"options\\\": {\\\"mode\\\": \\\"set\\\", \\\"urgency\\\": 8}}, {\\\"type\\\": \\\"SetLabels\\\", \\\"options\\\": {\\\"add_labels\\\": [\\\"Financial\\\"], \\\"remove_labels\\\": []}}'

        print("\n\n=============\nTest Add Actions Minimal:\n=============")
        print(f"\n--------\nExpected\n--------\n{validation}")
        print(f"\n------\nResult\n------\n{query}\n")

        self.assertEqual(query, validation)

if __name__ == "__main__":
    unittest.main()