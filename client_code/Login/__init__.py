from ._anvil_designer import LoginPageTemplate
from anvil import *
import anvil.users

class LoginPage(LoginPageTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    # Using signup_archived_fields lets new users enter their name during sign-up

    # 2. Check if login was successful
    if user:
      # REDIRECT: Go straight to the EditProfile form
      open_form('EditProfile') 

