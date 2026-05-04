import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def get_current_user_info():
  """Returns the current user row or None if not logged in."""
  return anvil.users.get_user()

@anvil.server.callable
def get_goal_progress(goal_row):
  """Calculates progress for a specific goal by checking the tasks table."""
  # 1. Fetch all tasks linked to this goal
  all_tasks = list(app_tables.tasks.search(goal=goal_row))
  total = len(all_tasks)

  # 2. Fetch only completed tasks linked to this goal
  completed_tasks = list(app_tables.tasks.search(goal=goal_row, done=True))
  completed = len(completed_tasks)

  # 3. Calculate percentage safely
  progress = (completed / total * 100) if total > 0 else 0

  return {
    "total": total,
    "completed": completed,
    "progress_percent": progress
  }











  

  

  


  





