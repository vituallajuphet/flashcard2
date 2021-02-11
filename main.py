from tkinter import *
from classes.my_data import MyData
from tkinter import messagebox

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


		self.text_desc = Text(self.folder_frame, width=19, height=1)
		self.text_desc.config(font=("Courier", 12))
		self.text_desc.insert(1.0, "Folder name")
		self.text_desc.place(x=250, y=-53)

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
    		
			btns.append(Button(self.folder_frame, text=dta["folder_name"], command= lambda i = i: self.view_cards(i), padx=20))
			btns[i].grid(row=row, column=col, pady=(0, 5), padx=(0, 5))
			btns[i].config(width=10, font=("courier", 11))
			i += 1
			col += 1
			if col == 5:
				col = 1
				row += 1


	def goto_notes(self):
		return self

	def create_folder (self):
		foldername = self.text_desc.get("1.0","end-1c")
		if foldername == "":
			messagebox.showerror("Error", "Fields must not be empty!")
			return
		self.remove_child_frame_elem()
		dta = MyData()

		self.data.append({
			"folder_name": foldername,
			"cards": []
		})
		dta.set_data(self.data)
		self.data = dta.get_data()
		self.build_folder()
		self.text_desc.delete(1.0,"end")
		return self


	def view_cards(self,index):
		from classes.pages import	Pages
		self.main_window.destroy()
		page = Pages(index, self.data)

	
	def remove_child_frame_elem(self):
		i = 0
		for child in self.folder_frame.winfo_children():
			if i == 0 or i == 1:
				i += 1 
				continue
			child.destroy()
			i += 1


if __name__ == '__main__':
	# run main
	
	data = MyData()
	main = Main(data.get_data())


