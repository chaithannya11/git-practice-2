def get_user_name(user):
    return user["name"]

def is_active_user(user):
    return user.get("active",false)

def get_user_email(user):
    return user["email"]

def get_user_role(user):
    return user["role"]