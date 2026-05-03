from ._anvil_designer import LoginPageTemplate
from anvil import *
import anvil.facebook.auth
import anvil.users
import anvil.server

class LoginPage(LoginPageTemplate):
  def __init__(self, **properties):
    # Set up the UI components first
    self.init_components(**properties)

    # Prompt the user to log in as soon as the form loads
    user = anvil.users.login_with_form()

    # Optional: Redirect or update UI if login is successful
    if user:
      print(f"Welcome, {user['email']}")
    else:
      print("Login cancelled.")


