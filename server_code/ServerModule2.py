import anvil.users
import anvil.server
from anvil.tables import app_tables

@anvil.server.callable
def update_user_profile(new_username, new_email):
  user = anvil.users.get_user()
  if user:
    # This line updates the 'username' and 'email' columns in your table
    user['username'] = new_username
    user['email'] = new_email
    return True
  return False
