from enum import Enum


'''
Set SLAs: , {\\\"type\\\": \\\"SetSlas\\\", \\\"options\\\": {\\\"add_sla_ids\\\": [\\\"1\\\"], \\\"remove_sla_ids\\\": []}}
Set Agent Followers: , {\\\"type\\\": \\\"SetAgentFollowers\\\", \\\"options\\\": {\\\"add_agent_ids\\\": [\\\"29\\\"]}}
Set Department: , {\\\"type\\\": \\\"SetDepartment\\\", \\\"options\\\": {\\\"department_id\\\": \\\"2\\\"}}
Set Agent Team: , {\\\"type\\\": \\\"SetAgentTeam\\\", \\\"options\\\": {\\\"agent_team_id\\\": \\\"2\\\"}}
Set Urgency: , {\\\"type\\\": \\\"SetUrgency\\\", \\\"options\\\": {\\\"mode\\\": \\\"raise\\\", \\\"urgency\\\": 8}}
Set Labels: , {\\\"type\\\": \\\"SetLabels\\\", \\\"options\\\": {\\\"add_labels\\\": [\\\"Financial\\\"], \\\"remove_labels\\\": []}}
Set Custom Field: , {\\\"type\\\": \\\"SetTicketField19\\\", \\\"options\\\": {\\\"op\\\": \\\"set\\\", \\\"value\\\": \\\"20\\\"}}
Set Agent: , {\\\"type\\\": \\\"SetAgent\\\", \\\"options\\\": {\\\"agent_id\\\": \\\"2\\\"}}
Set Round Robin: , {\\\"type\\\": \\\"SetRoundRobin\\\", \\\"options\\\": {\\\"id\\\": \\\"1\\\"}}
'''

class ActionType(Enum):
    SET_SLA = "SetSlas"
    SET_AGENT_FOLLOWERS = "SetAgentFollowers"
    SET_DEPARTMENT = "SetDepartment"
    SET_AGENT_TEAM = "SetAgentTeam"
    SET_URGENCY = "SetUrgency"
    SET_LABELS = "SetLabels"
    SET_CUSTOM_FIELD = "SetCustomField"
    SET_AGENT = "SetAgent"
    SET_ROUND_ROBIN = "SetRoundRobin"


### Build individual action snippets
def add_sla_action(sla_ids):
    return f', {{\\\"type\\\": \\\"SetSlas\\\", \\\"options\\\": {{\\\"add_sla_ids\\\": [{",".join([f"\\\"{sla_id}\\\"" for sla_id in sla_ids])}], \\\"remove_sla_ids\\\": []}}}}'

def add_agent_followers_action(agent_ids):
    return f', {{\\\"type\\\": \\\"SetAgentFollowers\\\", \\\"options\\\": {{\\\"add_agent_ids\\\": [{",".join([f"\\\"{agent_id}\\\"" for agent_id in agent_ids])}]}}}}'

def add_department_action(department_id):
    return f', {{\\\"type\\\": \\\"SetDepartment\\\", \\\"options\\\": {{\\\"department_id\\\": \\\"{department_id}\\\"}}}}'

def add_agent_team_action(agent_team_id):
    return f', {{\\\"type\\\": \\\"SetAgentTeam\\\", \\\"options\\\": {{\\\"agent_team_id\\\": \\\"{agent_team_id}\\\"}}}}'

def set_urgency_action(urgency):
    return f', {{\\\"type\\\": \\\"SetUrgency\\\", \\\"options\\\": {{\\\"mode\\\": \\\"set\\\", \\\"urgency\\\": {urgency}}}}}' 

def add_labels_action(labels):
    return f', {{\\\"type\\\": \\\"SetLabels\\\", \\\"options\\\": {{\\\"add_labels\\\": [{",".join([f"\\\"{label}\\\"" for label in labels])}], \\\"remove_labels\\\": []}}}}'

def set_custom_field_action(field_id, value):
    return f', {{\\\"type\\\": \\\"SetTicketField{field_id}\\\", \\\"options\\\": {{\\\"op\\\": \\\"set\\\", \\\"value\\\": \\\"{value}\\\"}}}}'

def set_agent_action(agent_id):
    return f', {{\\\"type\\\": \\\"SetAgent\\\", \\\"options\\\": {{\\\"agent_id\\\": \\\"{agent_id}\\\"}}}}'

def set_round_robin_action(round_robin_id):
    return f', {{\\\"type\\\": \\\"SetRoundRobin\\\", \\\"options\\\": {{\\\"id\\\": \\\"{round_robin_id}\\\"}}}}'

### Combine multiple actions into a single string
def add_actions(actions):
    result = ""
    for action in actions:
        match action[0]:
            case ActionType.SET_SLA:
                result += add_sla_action(action[1])
            case ActionType.SET_AGENT_FOLLOWERS:
                result += add_agent_followers_action(action[1])
            case ActionType.SET_DEPARTMENT:
                result += add_department_action(action[1])
            case ActionType.SET_AGENT_TEAM:
                result += add_agent_team_action(action[1])
            case ActionType.SET_URGENCY:
                result += set_urgency_action(action[1])
            case ActionType.SET_LABELS:
                result += add_labels_action(action[1])
            case ActionType.SET_CUSTOM_FIELD:
                result += set_custom_field_action(action[1][0], action[1][1])
            case ActionType.SET_AGENT:
                result += set_agent_action(action[1])
            case ActionType.SET_ROUND_ROBIN:
                result += set_round_robin_action(action[1])
            case _:
                raise Exception(f"Unknown action type: {action[0]}")
    return result