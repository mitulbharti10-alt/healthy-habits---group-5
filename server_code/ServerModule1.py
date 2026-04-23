import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def get_current_user_info():
  # This returns the current user row or None
  return anvil.users.get_user()

@anvil.server.callable
def update_user_profile(name):
  user = anvil.users.get_user()
  if user:
    user['name'] = name # Assumes you added a 'name' column to Users table


  

  

  


  





