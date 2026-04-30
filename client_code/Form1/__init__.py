from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    def update_progress(self, perrcentage) : 
      # This sends the percentage (e.g. 75) to your Javascript function 
      self.call_js('setProgress', percentage)  

  @handle("", "show")
  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    Class Form1
def _init_(self, **properties):
  # Set Form properties and Data Binding. 
  self.init_components(**properties) 

  # Set initial progress to 75%
  self.call_js('setProgress', 85) 

Class Form1
def _init_(self, **properties):
  # Set Form properties and Data Binding. 
  self.init_components(**properties) 

  # Set initial progress to 75%
  self.call_js('setProgress', 85) 
  
  


