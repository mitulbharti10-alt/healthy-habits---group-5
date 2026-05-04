import anvil.users
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def update_user_theme(is_dark):
  # 1. Get the user currently logged into the app
  user = anvil.users.get_user()

  if user:
    # 2. Save the True/False value to the 'dark_mode' column
    # Make sure you added this column to your Users table!
    user['dark_mode'] = is_dark
