from ._anvil_designer import DashboardTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Dashboard(DashboardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("Goals", "click")
  def Goals_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass  # Write Code Here

    self.goals = 100 

from datetime import date, timedelta
from anvil.tables import app_tables
import anvil.users 

# the weekly streak function code goes here 
def get_week_start(): 
    today = date.today() 
   return today - timedelta(days=today.weekday()) # Monday 
 
def load_streak(self):
  user = anivl.user.get_users() 
  week_start = get_week_start() 

  row = app_tables.streaks.get(user=user, week_start=week_start) 

  if not row:
    row = app_tables.streaks.add.row(
      user=user
      week_start=week_start,
      mon = False,
      tue = False,
      wed = False,
      thu = False, 
      fri = False
      sat = False, 
      sun = False
    )

self.row = row  
    




   




    
