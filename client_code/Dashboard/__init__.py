from ._anvil_designer import DashboardTemplate  # <--- THIS WAS MISSING
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
from datetime import date, timedelta
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Dashboard(DashboardTemplate):
  def __init__(self, **properties):
    # Ensure user is logged in before doing anything else
    self.check_user()

    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Load the streak data
    self.load_streak()

  def check_user(self):
    """Ensures the user is logged in."""
    user = anvil.users.get_user() 
    if user is None: 
      user = anvil.users.login_with_form() 

  def Goals_click(self, **event_args):
    self.goals = 100 

  def load_streak(self):
    user = anvil.users.get_user() 
    today = date.today()
    week_start = today - timedelta(days=today.weekday())

    # Fetch or create the streak row for this week
    row = app_tables.streaks.get(user=user, week_start=week_start) 

    if not row:
      row = app_tables.streaks.add_row(
        user=user,
        week_start=week_start,
        mon=False, tue=False, wed=False, thu=False, 
        fri=False, sat=False, sun=False
      )

    self.row = row
