from ._anvil_designer import SettingsTemplate
from anvil import *
import anvil.server
import anvil.users
from anvil.js.window import document # Helps change the entire page background

class Settings(SettingsTemplate):
  def __init__(self, **properties):
    # 1. Initialize components
    self.init_components(**properties)

    # 2. Get the current user and their saved theme
    user = anvil.users.get_user()
    if user:
      # Set the checkbox to match the database (defaults to False if empty)
      self.theme_switch.checked = user['dark_mode'] or False

    # 3. Apply the correct colors as soon as the page loads
    self.apply_theme()

  def apply_theme(self):
    """This function handles the visual change on the screen"""
    if self.theme_switch.checked:
      # Dark Mode Colors
      color = "#2c2c2c"
      text_color = "white"
      document.body.style.backgroundColor = color # Changes the whole browser tab
    else:
      # Light Mode Colors
      color = "white"
      text_color = "black"
      document.body.style.backgroundColor = color

    # Apply to the form and the toggle itself
    self.background = color
    self.theme_switch.foreground = text_color

  def theme_switch_change(self, **event_args):
    """This runs every time you click the checkbox/toggle"""
    # 1. Securely save the choice to the database via Server Module
    anvil.server.call('update_user_theme', self.theme_switch.checked)

    # 2. Immediately update the UI colors
    self.apply_theme()

  def back_btn_click(self, **event_args):
    """Navigates back to the ToDo list"""
    # Reset the background color before leaving if necessary
    document.body.style.backgroundColor = "white"
    open_form('ToDo')
