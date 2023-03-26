def handle_response(message):
    p_message = message.lower()
    if p_message == '$RoleStoreHelp':
        return 'This bot has no commands, it all works in the background. Using userids, it stores a users last known nickname and role assignements, and re=assigns them if a user re-joins the server'