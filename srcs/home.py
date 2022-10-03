from srcs.settings import *

class Home:
	def __init__(self, app):
		self.app = app


	def open(self):
		self.app.root.ids['screen_manager'].current = "home"
		self.app.root.ids['nav_drawer'].set_state("close")
