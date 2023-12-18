from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users


mlChestx_models = ['densenet121-res224-all', 
                  'densenet121-res224-rsna',
                  'densenet121-res224-nih',
                  'densenet121-res224-pc',
                  'densenet121-res224-chex',
                  'densenet121-res224-mimic_nb',
                  'densenet121-res224-mimic_ch',
                  'resnet50-res512-all']
class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.ddModel.items = mlChestx_models
    self.lblModelIndex.text = 'densenet121-res224-all'
    self.file = None

    # Any code you write here will run before the form opens.

  def ddModel_change(self, **event_args):
    """This method is called when an item is selected"""
    self.lblModelIndex.text = str(self.ddModel.selected_value)

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    self.file = file
    result = anvil.server.call('classify_image', file, modelname=self.lblModelIndex.text)
    print("resp: {}".format(result))
    app_tables.media.add_row(filename=file.name,original=file,result=result)
    
    keysList = list(eval(result).keys())
    print("keysList: {}".format(keysList))
    item_list = [{'vname':name, 'vvalue':eval(result)[name]} for name in keysList]
    print("itemList: {}".format(item_list))
    self.repeating_panel_1.items = item_list
    
    self.image_1.source = file

  def segmentationBtn_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.file is not None:
      f = self.file
      res = anvil.server.call('getHeatmap', f)
      
    else:
      alert('Upload image!')

  def saveBtn_click(self, **event_args):
    """This method is called when the button is clicked"""
    app_tables.media.add_row(filename=file.name,original=file,result=result)
