from ._anvil_designer import LoginTemplate
from anvil import *
import anvil.users

class Login(LoginTemplate): # This line MUST match the name in the sidebar
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Show the login form
    user = anvil.users.login_with_form()

    if user:
      open_form('EditProfile')
    else:
      Notification("Please log in to continue.").show()

