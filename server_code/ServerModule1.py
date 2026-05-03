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
week_dates = [today - timedelta(days=i) for i in range(29, -1, -1)]  

stats = [] 
for d in week_dates: 
  logged = app_tables.loginhistory.get(user=user, login_date=d) is not None 
  stats.append ({
    "day": d.strftime("%a"), #e.g. "Mon"
    "active": logged 
  })
  return stats    

@anvil.server.callable
def get_current_streak():
  user = anvil.users.get_user() 
if not user:
  return 0 
today = date.today()
streak = 0 
check_date = today 

# Loops backwards: check today, then yesterday, etc.
while True: 
  found = app_tables.loginhistory.get(user=user, login_date=check_date) 
if found: 
  streak += 1
  check_date -= timedelta(days=1) # Move back one day 
else: 
  break # Stop counting as soon as a day is missed

return streak  

















