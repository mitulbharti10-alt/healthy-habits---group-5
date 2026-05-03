from ._anvil_designer import EditProfileTemplate
from anvil import *
import anvil.users
import anvil.server

class EditProfile(EditProfileTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    # 1. Load the user's data when the page opens
    user = anvil.users.get_user()
    if user:
      self.email_box.text = user['email']
      self.username_box.text = user['username']
      self.profile_pic.source = user['picture'] # Shows the saved image
    else:
      open_form('LoginPage')

  def file_loader_1_change(self, file, **event_args):
    """Shows a preview as soon as a new photo is picked"""
    self.profile_pic.source = file

  def save_button_click(self, **event_args):
    """Saves all changes (including the image) to the database"""
    u_name = self.username_box.text
    u_email = self.email_box.text
    u_img = self.file_loader_1.file

    # Calls the 'update_user_profile' function in your server module
    success = anvil.server.call('update_user_profile', u_name, u_email, u_img)

    if success:
      Notification("Profile saved successfully!", style="success").show()
    else:
      Notification("Error saving profile.", style="danger").show()

  def to_do_button_click(self, **event_args):
    """Go to your to_do form list"""
    open_form('to_do')

  def sign_out_button_click(self, **event_args):
    """Logs the user out and returns to login"""
    anvil.users.logout()
    open_form('LoginPage')
