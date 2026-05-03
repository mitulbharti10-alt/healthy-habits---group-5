from ._anvil_designer import EditProfileTemplate
from anvil import *
import anvil.users
import anvil.server

class EditProfile(EditProfileTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    # Load the user's current data into the boxes
    user = anvil.users.get_user()
    if user:
      self.email_box.text = user['email']
      self.username_box.text = user['username']
    else:
      open_form('LoginPage')

  def save_button_click(self, **event_args):
    """Runs when the user clicks the Save button"""
    # 1. Collect what the user typed in the boxes
    u_name = self.username_box.text
    u_email = self.email_box.text

    # 2. Call the server function to update the database
    success = anvil.server.call('update_user_profile', u_name, u_email)

    # 3. Show the "Saved" message
    if success:
      Notification("Profile saved successfully!", style="success").show()
    else:
      Notification("Error saving profile.", style="danger").show()

