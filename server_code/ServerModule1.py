import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def create_goal (user, title, subject, goal_type, target_value):
  app_tables.goals.add_row(
    user=user, 
    title=title,
    subject=subject, 
    goal_type=goal_type,
    target_value=target_value, 
    current_value=0
    created_data=datetime.now()   
  )  

  

  

  


  





