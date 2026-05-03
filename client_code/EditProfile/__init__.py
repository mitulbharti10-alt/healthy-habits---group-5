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
      self.dob_box.text = user['dob']


    else:
      # Redirect to login if no one is logged in
      open_form('LoginPage')

  def save_button_click(self, **event_args):
    """Saves the profile details to the database"""
    # Validation: Don't allow saving empty fields
    if not self.username_box.text or not self.email_box.text:
      Notification("Cannot save empty fields!", style="danger").show()
      return

    # Call the server and catch the return message
    result = anvil.server.call('update_user_profile', 
                               self.username_box.text, 
                               self.email_box.text)

    if result == "Success":
      Notification("Profile saved!", style="success").show()
    elif result == "Email already used":
      alert("This email address is already linked to another account. Please use a different one.", 
            title="Email Already in Use")
    else:
      Notification(result, style="danger").show()

  def continue_to_dashboard(self, **event_args):
    """Checks for required fields before moving to the next screen"""
    name = self.username_box.text
    email = self.email_box.text

    # Check Name
    if not name:
      Notification("Full Name is required!", style="danger").show()
      self.username_box.focus()
      return

    # Check Email
    if not email:
      Notification("Email Address is required!", style="danger").show()
      self.email_box.focus()
      return

    # If both are filled, proceed
    open_form('dashboard')

  def to_do_button_click(self, **event_args):
    """Navigation to the To-Do list"""
    open_form('to_do')

  def sign_out_button_click(self, **event_args):
    """Logs the user out and returns to login"""
    anvil.users.logout()
    open_form('LoginPage')



  @handle("continue_to_goals", "click")
  def continue_to_goals_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('ToDo')
