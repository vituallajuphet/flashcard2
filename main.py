from tkinter import *
from classes.my_data import MyData


class Main:

	def __init__(self, mydata):
		self.data = mydata
		self.main_window = Tk(className="Flashcard Reviewer")
		self.main_window.geometry("600x800")
		self.build()

	def build(self):

		btn_frame = Frame(self.main_window, pady=16)
		btn_frame.pack(expand=True, fill=BOTH)

		var = StringVar()
		label = Label(btn_frame, text="Flashcard Reviewer", relief=FLAT)		
		label.config(font=("Courier", 20))
		label.pack(fill=BOTH)

		self.folder_frame = Frame(btn_frame, pady=(60), padx=5, bg="gray") 
		self.folder_frame.pack(expand=True, fill=BOTH)

		# label.pack(side=LEFT)

		btn_add = Button(self.folder_frame, text="+ Add Folder", command=self.create_folder, padx=20)
		btn_add.place(x=460, y=-55)

		self.build_folder()

		self.main_window.mainloop()
  
	def build_folder(self):
		
		col = 1
		row = 1
		btns = []
		i = 0;
		for dta in self.data:
			btns.append(Button(self.folder_frame, text="Folder {}".format(i+1), command= lambda i = i: self.view_cards(i), padx=20))
			btns[i].grid(row=row, column=col, pady=(0, 5), padx=(0, 5))
			btns[i].config(width=10, font=17)
			i += 1
			col += 1
			if col == 5:
				col = 1
				row += 1


	def goto_notes(self):
		return self

	def create_folder (self):
		self.remove_child_frame_elem()
		dta = MyData()
		self.data.append([])
		dta.set_data(self.data)
		self.data = dta.get_data()
		self.build_folder()

		return self


	def view_cards(self,index):
		from classes.pages import	Pages
		self.main_window.destroy()
		page = Pages(index, self.data)

	
	def remove_child_frame_elem(self):
		i = 0
		for child in self.folder_frame.winfo_children():
			if i == 0:
				i += 1 
				continue
			child.destroy()
			i += 1


if __name__ == '__main__':
	# run main
	
	data = MyData()
	main = Main(data.get_data())


