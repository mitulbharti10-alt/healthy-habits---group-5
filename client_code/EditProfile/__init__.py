from ._anvil_designer import EditProfileTemplate
from anvil import *
import anvil.users
import anvil.server

class settings(SettingsTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    # 1. Load the User's name at the top
    user = anvil.users.get_user()
    if user:
      # We use .get() to avoid errors if the username column is empty
      name = user.get('username') or user.get('email')
      self.name_label.text = f"Welcome, {name}!"

  def reset_pw_btn_click(self, **event_args):
    """Opens the secure password reset form"""
    anvil.users.change_password_with_form()
    Notification("Password updated successfully!").show()

  def edit_profile_click(self, **event_args):
    """Navigates to the Profile Edit page"""
    open_form('EditProfile')

  def logout_btn_click(self, **event_args):
    """Logs the user out and returns to login page"""
    anvil.users.logout()
    Notification("You have been signed out.").show()
    # Ensure 'LoginPage' matches the name in your App Browser exactly
    open_form('LoginPage') 

  def back_btn_click(self, **event_args):
    """Returns to the main ToDo list"""
    open_form('ToDo')
