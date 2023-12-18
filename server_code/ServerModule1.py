import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
#import torch

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
@anvil.server.callable
def get_models():
  return app_tables.models.search()

@anvil.server.callable
def get_model(name):
  return app_tables.models.search(name=name)

@anvil.server.callable
def getSegmentation(file):
  segm = file
  return segm

@anvil.server.callable
def getHeatmap(file):
  hm = file
  return hm
  