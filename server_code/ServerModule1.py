import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def get_current_user_info():
  # This returns the current user row or None
  return anvil.users.get_user()
  
def get_goal_progress(goal_row): # fuction code for the goal tracking feature
  tasks = app_tables.tasks.tasks.search(goal=goal_row) # finds the specific goal
  total = len(lists(tasks)) 
  completed = lens ({})
  


@anvil.server.callable
def update_user_profile(name):
  user = anvil.users.get_user()
  if user:
    user['name'] = name # Assumes you added a 'name' column to Users table 

@anvil.server.callable 
def record_login(): 
  user = anvil.users.get_user() 
  if user: 
    today = date.today() 
    # Checks for if a login for today already exists. 
    existing = app_tables.loginhistory.get(user=user, login_date=today) 
    if not existing: 
      app_tables.loginhistory.add_row(user=user, login_date=today) 

@anvil.server.callable
def get_streak_data(): 
  user = anvil.users.get_user() 
  if not user: 
    return[] 

today = date.today() 
# Get last 7 days (including today) 
week_dates = [today - timedelta(days=i) for i in range(6, -1, -1)] 

stats = [] 
for d in week_dates: 
  logged = app.tables.loginhistory 






  

  

  


  





