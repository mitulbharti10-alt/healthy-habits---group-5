from ._anvil_designer import Form1Template
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):  
  def __init__(self, **properties): 
    # Set Form properties and Data Binding. 
    self.init_components(**properties) 
  
  def update_progress(self,percentage): 
    # This sends the percentage to your Javascript function
    self.call_js('setProgress', percentage) 
    
  
  def form_show(self, **event_args): 
    """This method is called when the form is shown on the page""" 
  # Set initial progress to 00000085% 
    self.update_progress(85) 
  
  


