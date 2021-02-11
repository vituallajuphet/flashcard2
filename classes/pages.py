from tkinter import *
from classes.my_data import MyData

class Pages:

  def __init__(self, index, alldata):
    
    self.index = index
    self.alldata = alldata
    self.num = index + 1
    self.main_window = Tk(className="Folder {}".format(self.num))
    self.main_window.geometry("600x850")
    self.build()

  def build(self):
    print("running...")
    btn_frame = Frame(self.main_window, pady=16)
    btn_frame.pack(expand=True, fill=BOTH)

    var = StringVar()
    label = Label(btn_frame, text="Folder {}".format(self.num), relief=FLAT)
    label.config(font=("Courier", 20))
    label.pack(fill=BOTH)

    self.folder_frame = Frame(btn_frame, pady=(60), padx=5, bg="gray") 
    self.folder_frame.pack(expand=True, fill=BOTH)

    # label.pack(side=LEFT)

    btn_add = Button(self.folder_frame, text="+ Add Flashcard", command=self.create_folder, padx=20)
    btn_add.place(x=400, y=-55)

    btn_back = Button(self.folder_frame, text="Back", command=self.back_home, padx=20)
    btn_back.place(x=20, y=-55)

    self.build_folder()
    self.main_window.mainloop()
  
  def build_folder(self):

    col = 1
    row = 1
    btns = []
    i = 0;
    for dt in self.alldata[self.index]:
      btns.append(Button(self.folder_frame, text="Flashcard {}".format(i+1), command= lambda i = i: self.view_cards(i), padx=20))
      btns[i].grid(row=row, column=col, pady=(0, 5), padx=(0, 5))
      btns[i].config(width=9, font=17)
      i += 1
      col += 1
      if col == 5:
        col = 1
        row += 1


  def goto_notes(self):
    return self

  def create_folder (self):
    self.remove_child_frame_elem()
    obj = {"title":"", "content":""}
    self.alldata[self.index].append(obj)
    dta = MyData()
    dta.set_data(self.alldata)
    self.alldata = dta.get_data()

    self.build_folder()

    return self
  
  def view_cards(self, index):
    from classes.viewcard import ViewCard
    self.main_window.destroy()
    viewcard = ViewCard(index, self.index, self.alldata)
    return self
	
  def remove_child_frame_elem(self):
    i = 0
    for child in self.folder_frame.winfo_children():
      if i == 0 or i == 1:
        i += 1 
        continue
      child.destroy()
      i += 1
  def back_home(self):
    from main import Main
    self.main_window.destroy()
    main = Main(self.alldata)
    
    return self



