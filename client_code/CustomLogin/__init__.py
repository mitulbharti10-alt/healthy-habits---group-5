from ._anvil_designer import CustomLoginTemplate
from anvil import *
import anvil.users

class CustomLogin(CustomLoginTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  def login_button_click(self, **event_args):
    try:
      # Manually attempt login
      user = anvil.users.login_with_email(self.email_box.text, self.password_box.text)
      if user:
        open_form('EditProfile')

    except anvil.users.UserNotEnabled:
      # Your custom "Contact Admin" message
      alert("This account is not yet active. Please contact the administrator.")

    except anvil.users.AuthenticationFailed:
      Notification("Invalid email or password", style="danger").show()

  def show_pw_check_change(self, **event_args):
    # Toggle password visibility
    self.password_box.hide_text = not self.show_pw_check.checked
