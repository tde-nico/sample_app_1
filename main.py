from srcs import *


class Touch(MDScreen):
	def on_touch_move(self, touch):
		if touch.x - touch.ox > 200:
			if self.ids['nav_drawer'].status == 'closed':
				self.ids['nav_drawer'].set_state("open")
		if touch.y - touch.oy > 1000:
			exit()


class main_app(MDApp):
	def build(self):
		self.title = TITLE
		self.theme_cls.theme_style = SETTINGS["theme"]
		self.theme_cls.primary_palette = SETTINGS["palette"]
		self.info = None
		self.settings = Settings(self)
		self.home = Home(self)
		return Touch()



	def show_info(self):
		if not self.info:
			app_info =	\
				f"App: {TITLE}\n" \
				f"Developer: {DEVELOPER}\n" \
				f"Git: {GIT}\n" \
				f"Version: {VERSION}"
			self.info = MDDialog(
				title='Info',
				text=app_info,
				auto_dismiss=True
				)
		self.info.open()


	def exit(self):
		self.get_running_app().stop()
		exit()



if __name__ == '__main__':
	main_app().run()
