from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.timer_1.interval=0.1
    self.counter=0
    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def text_box_1_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if (self.counter>self.oldcounter):
      self.text_box_2.text=self.text_box_1.text+str(self.counter)

    self.old
   
    
    pass

  def timer_1_tick(self, **event_args):
    "This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    self.counter=self.counter+0.5
    
    
    pass
