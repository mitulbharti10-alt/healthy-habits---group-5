import anvil.users
import anvil.server
from anvil.tables import app_tables
import anvil.tables.query as q

@anvil.server.callable
def update_user_profile(new_username, new_email):
  user = anvil.users.get_user()
  if not user:
    return "Not logged in"

  # 1. Check if ANY OTHER user already has this email
  # We search for the email but EXCLUDE the current user's row
  existing_user = app_tables.users.get(email=new_email)

  if existing_user and existing_user != user:
    return "Email already used" # Send this back to the form

  # 2. If it's unique (or is already the current user's email), save it
  user.update(username=new_username, email=new_email)
  return "Success"
