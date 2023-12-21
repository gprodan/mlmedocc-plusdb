from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ItemTemplate1(ItemTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    self.vname.text = self.item['vname']
    self.vvalue.text = self.item['vvalue']
    self.add_event_handler("x-select", self.select_item)
  
  def select_item(self):
    print("Item selected")
    pass
    
