def fill_session(request, context):
    user_id = request.session.get('user_id', '')
    username = request.session.get('username', '')
    permission = request.session.get('permission', -1)
    context['user_id'] = user_id
    context['permission'] = permission
    context['username'] = username
    return context