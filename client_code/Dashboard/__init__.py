from datetime import date, timedelta
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .Daycard import Daycard 
import anvil.server  

class Dashboard(DashboardTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  #1 Ensure the user is logged in 
  user = anvil.users.get_user() 
  if not user: 
    anvil.users.login_with_form() 

  #2 Record today's login in the database
  anvil.server.call('record_login') 

  #3 Build the seven day streak calendar
  self.build_steak_ui() 

def build_streak_ui(self): 
  # Fetch the 7 days of data from the Server Module 
  streak_data = avnil.server.call('get_streak_data') 

  # Clear your flow panel before adding new cards 
  self.flow_panel_steak.clear() 

  # Create a Daycard for each of the 7 days
  for day_info in streak_data: 
    
    
    