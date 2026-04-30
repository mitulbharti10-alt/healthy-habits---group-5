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

Class Form1 
      