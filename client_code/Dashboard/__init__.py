from datetime import date, timedelta
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import date, timedelta
import anvil.users
import anvil.server
from ..Daycard import Daycard 
from ._anvil_designer import DashboardTemplate 


class Dashboard(DashboardTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    # 1. Handle Login
    user = anvil.users.get_user()
    if user is None:
      user = anvil.users.login_with_form()

    # 2. Record Today's Progress & Build the UI
    anvil.server.call('record_login') 
    self.refresh_streak_ui()

  def refresh_streak_ui(self):
    # Fetch the 7-day stats from your Server Module
    stats = anvil.server.call('get_streak_data')

    # Clear the FlowPanel and add your Daycards
    self.flow_panel_streak.clear()
    for day_info in stats:
      self.flow_panel_streak.add_component(Daycard(item=day_info))

  def Goals_click(self, **event_args):
    # This sets a goal variable for your progress circle
    self.goals = 100