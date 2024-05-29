from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.timer_1.interval=1
    self.counter=0
    self.oldcounter=0
    self.increm=0
    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def text_box_1_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if (self.counter>self.oldcounter):
      self.text_box_2.text=self.text_box_1.text+str(self.counter)

    self.oldcounter=self.counter
   
    
    pass

  def timer_1_tick(self, **event_args):
    "This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    self.counter=self.counter+1
    
    
    pass

  def text_box_3_change(self, **event_args):
    
    self.increm=0
    while (self.increm<0):  
      
      try:
        self.increm=1
        self.timer_1.interval=float(self.text_box_3.text)
        break
      except ValueError:
        pass
    
    pass
