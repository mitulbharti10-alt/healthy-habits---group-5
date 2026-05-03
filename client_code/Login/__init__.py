from ._anvil_designer import LoginPageTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class LoginPage(LoginPageTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    # 1. Show the login form
    # signup_archived_fields allows new users to enter their name
    user = anvil.users.login_with_form(signup_archived_fields={'username': 'Full Name'})

    # 2. Redirect to EditProfile only if login is successful
    if user:
      open_form('EditProfile')
    else:
      # Optional: message if they close the popup without logging in
      Notification("Login required to continue.").show()




