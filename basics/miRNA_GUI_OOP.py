# A GUI for fetch and update record in our miRBase

# define the class for a record
class Mirna:
	def __init__(self,name,length,target):
		self.name = name
		self.length = length
		self.target = target
	
	def get_species(self,sep):
		return(self.name.split(sep=sep)[0])

	def fetch(self):
		keys = ['name','length','target']
		for key in keys:
			print(getattr(self,key))

	def update(self,key,value):
		try: 
			oldvalue = getattr(self,key)
		except:
			print('No such key in my miRBase')
		else:
			setattr(self,key,value)
			print('The %s of has changed from %s to %s' % (key,oldvalue,value))

# record data
let7a = Mirna('human let7a',22,100) 
let7b = Mirna('human let7b',20,500) 
let7c = Mirna('human let7c',25,300) 

# use shelve to store the data
import shelve
# initialize
db = shelve.open('miRNA_GUI_OOP_shelve')
db['let7a'] = let7a
db['let7b'] = let7b
db['let7c'] = let7c
db.close()

# here comes the GUI part
from tkinter import *
from tkinter.messagebox import showerror
db = shelve.open('miRNA_GUI_OOP_shelve')
keys = ['name','length','target']

# open the main widget
def Make_widget():
	# entries: get the input, show the output
	global entries
	window = Tk()
	# create a widget instance
	window.title('My miRBase')
	# a method for widget class
	form = Frame(window)
	form.pack()
	entries = {}
	# a dict instance to store the entries
	for(ix,lable) in enumerate 
	
