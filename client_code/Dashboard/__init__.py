from datetime import date, timedelta
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Dashboard(DashboardTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    
    self.load_streak()

  def Goals_click(self, **event_args):
    self.goals = 100 

  def load_streak(self):
   
    user = anvil.users.get_user() 

    
    today = date.today()
    week_start = today - timedelta(days=today.weekday())

    
    row = app_tables.streaks.get(user=user, week_start=week_start) 

    
    if not row:
      row = app_tables.streaks.add_row(
        user=user,
        week_start=week_start,
        mon=False,
        tue=False,
        wed=False,
        thu=False, 
        fri=False,
        sat=False, 
        sun=False
      )

    
    self.row = row
