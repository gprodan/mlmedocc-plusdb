import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.media
#import torchxrayvision as xrv
#import skimage, torch, torchvision

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
def classify_image(file, modelname):
  with anvil.media.TempFile(file) as filename:
    #img = load_img(filename)
    img = skimage.io.imread(filename)
    img = xrv.datasets.normalize(img, 255) # convert 8-bit image to [-1024, 1024] range
    img = img.mean(2)[None, ...] # Make single color channel
    transform = torchvision.transforms.Compose([xrv.datasets.XRayCenterCrop(),xrv.datasets.XRayResizer(224)])
    img = transform(img)
    img = torch.from_numpy(img)
    model = xrv.models.DenseNet(weights=modelname)
    outputs = model(img[None,...]) # or model.features(img[None,...]) 
    return str(dict(zip(model.pathologies,outputs[0].detach().numpy())))

@anvil.server.callable
def getSegmentation(file):
  segm = file
  return segm

@anvil.server.callable
def getHeatmap(file):
  hm = file
  return hm
  