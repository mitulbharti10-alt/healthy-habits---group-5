from ._anvil_designer import DaycardTemplate
from anvil import *
import anvil.server
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Daycard(DaycardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # 'self.item' will contain the data for one day

    if self.item: 
      # set the number on the card 
      self.label_date.text = self.item['date'].day 

    # Change colour based on if the user logged in ('active') 
    if self.item['active']: 
      self.background = "#2ecc71" #Emrald Green
     self.label_date.foreground = "white" 
    else: 
     self.background = "#eeeeee"  # Light Grey 
     self.label_date.foreground = "#777777"






