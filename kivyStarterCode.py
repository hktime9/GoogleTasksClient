import kivy  
kivy.require("1.9.1")  
from kivy.app import App  
from kivy.uix.button import Button 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.textinput import TextInput

thisBorder= """
border:
    orientation: 'vertical'
    
    canvas:
        Color:    
            rgb: (0/255,0/255,0/255)
        
        Line: 
        	rectangle: (self.pos[0], self.pos[1], self.size[0], self.size[1])
"""

thisRectangle= """
rectangle:
    orientation: 'vertical'
    
    canvas:
        Color:
            rgb: (235/255,185/255,3/255)
        
        Rectangle:
        	pos: self.pos
        	size: self.size
""" 

class border(BoxLayout):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

class rectangle(BoxLayout):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

class BoxLayoutApp(App):
    def build(self): 
        mainWindow= BoxLayout(orientation= 'vertical')
        tasksWindow= BoxLayout(orientation= 'vertical')
        headingBox= BoxLayout(orientation= 'horizontal', size_hint=(1.0, 0.5))
        label= Label(text= "Google Tasks", size_hint= (1.0, 1.0), halign= "center", valign= "center")
        headingBox.add_widget(label)
        tasksWindow.add_widget(headingBox)
        numTasks= 20
        for i in range(numTasks):
        	task= BoxLayout(orientation= 'horizontal')
        	buttons= BoxLayout(orientation= 'vertical', size_hint=(None, 1))
        	border= Builder.load_string(thisBorder, size_hint=(0.75,1.0)) #this might be something
        	inner= Builder.load_string(thisRectangle)
        	border.add_widget(inner)
        	editBtn= Button(text= "Edit", size_hint=(None,0.3333))
        	deleteBtn= Button(text= "Delete", size_hint=(None,0.3333))
        	buttons.add_widget(editBtn)
        	buttons.add_widget(deleteBtn)
        	task.add_widget(border)
        	task.add_widget(buttons)
        	tasksWindow.add_widget(task)
        mainWindow.add_widget(tasksWindow)
        return mainWindow
root= BoxLayoutApp()
root.run() 