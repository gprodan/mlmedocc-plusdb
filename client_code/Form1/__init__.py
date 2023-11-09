from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users

mlChestx_models = ['PSPNet', 'cx']
class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.ddModel.items = mlChestx_models

    # Any code you write here will run before the form opens.

  def ddModel_change(self, **event_args):
    """This method is called when an item is selected"""
    self.lblModelIndex.text = str(self.ddModel.selected_value)

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    result = anvil.server.call('classify_image', file)
    print("resp: {}".format(result))
    self.label_2.text = "{}".format(result)
    self.image_1.source = file
