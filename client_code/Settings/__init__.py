from ._anvil_designer import SettingsTemplate
from anvil import *
import anvil.server
import anvil.users

class Settings(SettingsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def reset_pw_btn_click(self, **event_args):
    anvil.users.change_password_with_form()
    Notification("Password updated successfully!").show()

  def logout_btn_click(self, **event_args):
    #Log the user out from the server
    anvil.users.logout()

    Notification("You have been signed out.").show()

    open_form('LoginPage') 

  @handle("edit_profile", "click")
  def edit_profile(self, **event_args):
    open_form('EditProfile')

from ._anvil_designer import SettingsTemplate
from anvil import *
import anvil.server
import anvil.users

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

