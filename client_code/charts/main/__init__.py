from ._anvil_designer import mainTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import widgets
from ... import build
from ... import form

class main(mainTemplate):
  def __init__(self, row=None, **properties):

    self.init_components(**properties)
    
    self.tag.row=row
    self.tag.form_dict={}
    save_button=Button(text='save', role='primary-color')
    save_button.set_event_handler('click', self.save_click)
    self.add_component(save_button)
    
    if row:
      self.tag.id=row['form_id']
      #self.share_link_click.url=anvil.server.get_app_origin() + '#' + row['form_id']
      self.tag.num_widgets=row['schema']['num_widgets']
      self.text_box_title.text=row['title']
      #build.build_form(row['schema'], self.column_panel)
      
    else:
      self.tag.id=None
      self.tag.num_widgets=0
      
  def save_click(self, **event_args):
    #schema=build.build_schema(self.column_panel)
    #form_id=anvil.server.call('save_schema', self.tag.id, schema)
    #self.tag.id=form_id
    #self.share_link_click.url=anvil.server.get_app_origin() + '#' + form_id
    pass

  def form_show(self, **event_args):
    
    if not self.tag.row:
      self.section_widget_click()
      
    else:
      
      for section in self.column_panel.get_components():
        self.color_rows(section)
        
      section.section_select()
    
    
  def section_widget_click(self, **event_args):
    section=widgets.section()
    self.column_panel.add_component(section)
    section.label_id.text=self.tag.num_widgets
    self.tag.num_widgets+=1
    self.tag.form_dict[section.label_id.text]=section
    
  def color_rows(self, section, **event_args):
            
    for i, comp in enumerate(section.column_panel.get_components()):

      if not i%2:
        comp.background='theme:Gray 100'
        
      else:
        comp.background='white'
          
  def link_landing_click(self, **event_args):
     open_form('landing.select_form')

  def share_link_click(self, **event_args):
    
    if not self.share_link_click.url:
      Notification('',title='Please save the form first').show()

    else:
      #schema=build.build_schema(self.column_panel)
      #anvil.server.call('save_schema', self.tag.id, schema)
      pass
    
  def markdown_widget_click(self, **event_args):
    """This method is called when the link is clicked"""
    comp=widgets.markdown(section=self.tag.active_section)
    self.tag.active_section.column_panel.add_component(comp)
    self.color_rows(self.tag.active_section)
    comp.label_id.text=self.tag.num_widgets
    self.tag.num_widgets+=1
    self.tag.form_dict[comp.label_id.text]=comp








