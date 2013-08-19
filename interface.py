import npyscreen
class Facebook(npyscreen.NPSApp):
	def main(self):
		form = npyscreen.FormBaseNew(name = "Facebook")
		post = form.add(npyscreen.TitleText, name = "Post:")
		postbn = form.add(PostPress, name = "Post!")
		form.edit()
		
class PostPress(npyscreen.ButtonPress):
	def whenPressed(self):
		popup = npyscreen.notify_confirm("Posted!", title="Status", wide=False, editw=1)

if __name__ == "__main__":
	App = Facebook()
	App.run()
