from ._anvil_designer import toolbarTemplate
from anvil import *
from ... import widgets

class toolbar(toolbarTemplate):
  
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    

  def widget_control(self, **event_args):
    """This method is called when the link is clicked"""
    widgets.widget_control(comp)
    
    
