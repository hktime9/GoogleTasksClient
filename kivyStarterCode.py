import kivy  
kivy.require("1.9.1")  
from kivy.app import App  
from kivy.uix.button import Button 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.textinput import TextInput

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

backdrop= """
rectangle:
	orientation: 'vertical'
	canvas: 
		Color: 
			rgb: (51/255,51/255,51/255)
		Rectangle:
			pos: self.pos
			size: self.size
"""

sideBorder= """
rectangle:
	orientation: 'vertical'
	canvas: 
		Color: 
			rgb: (51/255,51/255,51/255)
		Rectangle:
			pos: self.pos
			size: self.size
"""

class rectangle(BoxLayout):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

class BoxLayoutApp(App):
    def build(self):
    	headingBoxSize= 0.15
    	horiBorderSize= 0.01
    	vertiBorderSize= None
    	restBoxSize= 1-headingBoxSize-horiBorderSize
    	mainWindow= BoxLayout(orientation= 'vertical')
    	
    	headingBox= BoxLayout(orientation= 'horizontal', size_hint=(1.0, headingBoxSize))
    	headingRect= Builder.load_string(backdrop)
    	headingTitle= Label(text= "Google Tasks", size_hint= (1.0, 1.0), halign= "center", valign= "center")
    	headingRect.add_widget(headingTitle)
    	headingBox.add_widget(headingRect)
    	mainWindow.add_widget(headingBox)

    	restBox= BoxLayout(orientation= 'horizontal', size_hint=(1.0, restBoxSize))

    	leftBorder= BoxLayout(orientation= 'horizontal', size_hint=(horiBorderSize, 1.0))
    	leftRect= Builder.load_string(sideBorder)
    	leftBorder.add_widget(leftRect)
    	restBox.add_widget(leftBorder)

    	restRect= Builder.load_string(thisRectangle)
    	restBox.add_widget(restRect)

    	rightBorder= BoxLayout(orientation= 'horizontal', size_hint=(horiBorderSize, 1.0))
    	rightRect= Builder.load_string(sideBorder)
    	rightBorder.add_widget(rightRect)
    	restBox.add_widget(rightBorder)

    	mainWindow.add_widget(restBox)
    	return mainWindow
root= BoxLayoutApp()
root.run() 