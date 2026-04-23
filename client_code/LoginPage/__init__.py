from ._anvil_designer import LoginPageTemplate
from anvil import *
import anvil.users
import anvil.server

class LoginPage(LoginPageTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  def login_button_click(self, **event_args):
    # Triggers the standard Email/Google popup
    user = anvil.users.login_with_form()
    if user:
      self.check_user_and_proceed()

  def google_login_click(self, **event_args):
    # Direct Google login shortcut
    user = anvil.users.login_with_google()
    if user:
      self.check_user_and_proceed()

  def check_user_and_proceed(self):
    # After login, move to the next screen (e.g., 'MainPage')
    open_form('MainPage')

# If you want the login form to show up automatically as soon as the app loads:
anvil.users.login_with_form()

# Inside your LoginPage or HomeForm
def submit_button_click(self, **event_args):
  data_to_save = self.text_box_1.text

  # Call the server function
  anvil.server.call('save_user_data', data_to_save)

  # Clear the box and notify the user
  self.text_box_1.text = ""
  Notification("Successfully saved to database!").show()


