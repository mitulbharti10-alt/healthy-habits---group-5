import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def update_user_profile(new_name, new_email, new_pic):
  # 1. Get the user who is currently logged in
  user = anvil.users.get_user()

  if user:
    # 2. Update the columns in your 'Users' table
    # Make sure your table columns are named 'full_name' and 'profile_image'
    user['full_name'] = new_name
    user['email'] = new_email

    # 3. Only save the picture if they uploaded a new one
    if new_pic:
      user['profile_image'] = new_pic

    return "Success"
  else:
    return "No user logged in"

