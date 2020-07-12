from ._anvil_designer import text_areaTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class text_area(text_areaTemplate):
  def __init__(self, section, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    
    from ..toolbar import toolbar
    toolbar=toolbar(align='left', section=section, parent=self)
    self.add_component(toolbar)