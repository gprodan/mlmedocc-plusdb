from ._anvil_designer import Form2Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def ddModel_change(self, **event_args):
    """This method is called when an item is selected"""
    res = anvil.server.call("get_model")
    self.modelDescr.text = res['description']
    
