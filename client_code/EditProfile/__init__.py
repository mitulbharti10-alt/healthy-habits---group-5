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
    else:
      open_form('LoginPage')

  def save_button_click(self, **event_args):
    # Call the server and catch the return message
    result = anvil.server.call('update_user_profile', 
                               self.username_box.text, 
                               self.email_box.text)

    if result == "Success":
      Notification("Profile saved!", style="success").show()
    elif result == "Email already used":
      # Highlight the problem for the user
      alert("This email address is already linked to another account. Please use a different one.", 
            title="Email Already in Use")
    else:
      Notification(result, style="danger").show()


  def to_do_button_click(self, **event_args):
    """Go to your to_do form list"""
    open_form('to_do')

  def sign_out_button_click(self, **event_args):
    """Logs the user out and returns to login"""
    anvil.users.logout()
    open_form('LoginPage')
