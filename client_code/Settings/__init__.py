from ._anvil_designer import SettingsTemplate
from anvil import *
import anvil.server
import anvil.users

class Settings(SettingsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def reset_pw_click_click(self, **event_args):
    # This pops up Anvil's secure, pre-built password change dialog
    # It handles all the validation (matching passwords, length, etc.) automatically
    anvil.users.change_password_with_form()

    # Show a professional notification when they finish
    Notification("Password updated successfully!").show()

  def reset_pw_click(self, **event_args):
    anvil.users.change_password_with_form()
    Notification("Password updated!").show()





class Settings(SettingsTemplate):
  def __init__(self, **properties):
    # This must be the first thing inside __init__
    self.init_components(**properties)

    # 1. Get the current user
    user = anvil.users.get_user()

    # 2. Check if they have a name saved in the 'name' column
    if user and user['username']:
      self.name_label.text = f"Welcome, {user['name']}!"
    else:
      # Fallback if the name is empty (Anvil users always have an email)
      self.name_label.text = f"Welcome, {user['email']}!"


