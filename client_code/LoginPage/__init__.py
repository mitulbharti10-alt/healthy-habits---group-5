from ._anvil_designer import LoginPageTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class LoginPage(LoginPageTemplate):
  def __init__(self, **properties):
    # 1. Initialize the UI
    self.init_components(**properties)

    # 2. Show the login form and WAIT for the user to finish
    user = anvil.users.login_with_form()

    # 3. Check if login was successful
    if user:
      # This moves the user to the next screen. 
      # Ensure you have a form named 'Dashboard' in your sidebar!
      open_form('EditProfile') 
    else:
      # Optional: what happens if they close the login box without logging in?
      Notification("Please log in to continue.").show()


   
