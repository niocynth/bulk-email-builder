def gen_email_account():
    pass

### Generate SQL to create a new ticket trigger based on email criteria
def gen_new_ticket_trigger(email_address, email_account_id, email_field_parent_id=None, email_field_child_id=None, actions_list=""):
    # declare variables
    additional_actions = ""
    email_field_term = ""
    
    # set title
    title = f"Email Trigger for {email_address}"

    # add manually selecting an email to the terms if specified
    if email_field_parent_id and email_field_child_id:
        email_field_term = ", {\\\"set_terms\\\": [{\\\"op\\\": \\\"is\\\", \\\"type\\\": \\\"CheckTicketField" + email_field_parent_id + "\\\", \\\"options\\\": {\\\"value\\\": [\\\"" + email_field_child_id + "\\\"], \\\"field_id\\\": \\\"" + email_field_parent_id + "\\\", \\\"type_name\\\": \\\"choice\\\"}}]}"
        additional_actions = ", {\\\"type\\\": \\\"SetTicketField" + email_field_parent_id + "\\\", \\\"options\\\": {\\\"op\\\": \\\"set\\\", \\\"value\\\": \\\"" + email_field_child_id + "\\\"}}"

    # construct terms (escaped JSON object)
    terms = "{\\\"@DATA\\\": {\\\"terms\\\": [{\\\"set_terms\\\": [{\\\"op\\\": \\\"is\\\", \\\"type\\\": \\\"CheckEmailToAddress\\\", \\\"options\\\": {\\\"email\\\": \\\"" + email_address + "\\\"}}]}, {\\\"set_terms\\\": [{\\\"op\\\": \\\"is\\\", \\\"type\\\": \\\"CheckEmailCcAddress\\\", \\\"options\\\": {\\\"email\\\": \\\"" + email_address +"\\\"}}]}, {\\\"set_terms\\\": [{\\\"op\\\": \\\"contains\\\", \\\"type\\\": \\\"CheckEmailHeader\\\", \\\"options\\\": {\\\"name\\\": \\\"Received\\\", \\\"value\\\": \\\"" + email_address + "\\\"}}]}" + email_field_term + "], \\\"version\\\": 1}, \\\"@CLASS\\\": \\\"Application\\\\\\\\DeskPRO\\\\\\\\Tickets\\\\\\\\Triggers\\\\\\\\TriggerTerms\\\"}"

    # construct any additional actions
    if actions_list != "":
        additional_actions += actions_list

    # construct actions (escaped JSON object)
    actions = "{\\\"@DATA\\\": {\\\"actions\\\": [{\\\"type\\\": \\\"SetEmailAccount\\\", \\\"options\\\": {\\\"email_account_id\\\": \\\"" + email_account_id + "\\\"}}" + additional_actions + "], \\\"version\\\": 1}, \\\"@CLASS\\\": \\\"Application\\\\\\\\DeskPRO\\\\\\\\Tickets\\\\\\\\Triggers\\\\\\\\TriggerActions\\\"}"
    # construct final query
    query = f'INSERT INTO ticket_triggers (title, event_trigger, event_flags, by_agent_mode, by_user_mode, by_app_mode, is_enabled, is_hidden, is_editable, terms, actions, run_order) VALUES ("{title}", "newticket", "", "web,email", "email", "", 1, 0, 1, "{terms}", "{actions}", 100);'

    return query

### Generate SQL to create a ticket update trigger based on email criteria
def gen_ticket_update_trigger(email_address, email_field_parent_id, email_field_child_id, email_account_id, actions_list=""):
    # declare variables
    additional_actions = ""

    # set title
    title = f"Update Trigger for {email_address}"

    # construct terms (escaped JSON object)
    terms = "{\\\"@DATA\\\": {\\\"terms\\\": [{\\\"set_terms\\\": [{\\\"op\\\": \\\"is\\\", \\\"type\\\": \\\"CheckTicketField" + email_field_parent_id + "\\\", \\\"options\\\": {\\\"value\\\": [\\\"" + email_field_child_id + "\\\"], \\\"field_id\\\": \\\"" + email_field_parent_id + "\\\", \\\"type_name\\\": \\\"choice\\\"}}]}], \\\"version\\\": 1}, \\\"@CLASS\\\": \\\"Application\\\\\\\\DeskPRO\\\\\\\\Tickets\\\\\\\\Triggers\\\\\\\\TriggerTerms\\\"}"

    # construct any additional actions
    if actions_list != "":
        additional_actions += actions_list

    # construct actions (escaped JSON object)
    actions = "{\\\"@DATA\\\": {\\\"actions\\\": [{\\\"type\\\": \\\"SetEmailAccount\\\", \\\"options\\\": {\\\"email_account_id\\\": \\\"" + email_account_id + "\\\"}}" + additional_actions + "], \\\"version\\\": 1}, \\\"@CLASS\\\": \\\"Application\\\\\\\\DeskPRO\\\\\\\\Tickets\\\\\\\\Triggers\\\\\\\\TriggerActions\\\"}"

    # construct final query
    query = f'INSERT INTO ticket_triggers (title, event_trigger, event_flags, by_agent_mode, by_user_mode, by_app_mode, is_enabled, is_hidden, is_editable, terms, actions, run_order) VALUES ("{title}", "update", "", "web", "", "", 1, 0, 1, "{terms}", "{actions}", 100);'

    return query