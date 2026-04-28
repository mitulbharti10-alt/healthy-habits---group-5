from ._anvil_designer import WelcomepageTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.google.auth
import anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Survey import Survey


class Welcomepage(WelcomepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings
    self.init_components(**properties)

    # Load the Survey page by default
    # self.content_panel.add_component(Survey(), full_width_row=True)

    # Check if the user is admin
    anvil.server.call("get_total_responses")

    # if anvil.server.call('check_admin'):
    #   self.report_link.visible = True
    #   self.login_link.visible = False
    #   self.logout_link.visible = True

  def report_link_click(self, **event_args):
    """This method is called when the report link is clicked"""
    if anvil.server.call("check_admin"):
      self.content_panel.clear()
      self.content_panel.add_component(Report(), full_width_row=True)
      self.back_link.visible = True
      self.report_link.visible = False

  def back_link_click(self, **event_args):
    """This method is called when the back link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Survey(), full_width_row=True)
    self.back_link.visible = False
    self.report_link.visible = True

  def logout_link_click(self, **event_args):
    """This method is called when the logout link is clicked"""
    anvil.users.logout()
    self.content_panel.clear()
    self.content_panel.add_component(Survey(), full_width_row=True)
    self.logout_link.visible = False
    self.login_link.visible = True
    self.report_link.visible = False

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    user = anvil.users.login_with_form()
    if user:
      print(f"This user has logged in: ")
      open_form("Survey")
