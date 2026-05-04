import anvil.users
import anvil.server

@anvil.server.callable
def update_user_profile(new_username, new_email):
  user = anvil.users.get_user()
  if user:
    user.update(username=new_username, email=new_email)
    return True
  return False
