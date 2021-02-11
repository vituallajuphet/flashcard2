from tkinter import *
from classes.my_data import MyData
from tkinter import messagebox
from time import sleep
from tkinter import ttk


class Viewall:

  def __init__(self, folderindex, alldata):
    
    self.folderindex = folderindex
    self.alldata = alldata
    self.main_window = Tk(className="All Flashcards")
    self.main_window.geometry("600x850")
    self.build()

  def build(self):
    btn_frame = Frame(self.main_window, pady=16)
    btn_frame.pack(side=TOP, fill=BOTH, expand=0)

    var = StringVar()
    self.label = Label(btn_frame, text="All Flashcards", relief=FLAT)
    self.label.config(font=("Courier", 20))
    self.label.pack(fill=BOTH)    

    self.folder_frame = Frame(btn_frame, pady=(60), padx=5, height=50) 
    self.folder_frame.pack(side=TOP, fill=BOTH, expand=0)

    btn_back = Button(self.folder_frame, text="Back", command=self.back_folder, padx=20)
    btn_back.place(x=20, y=-55)

    self.show_all_cards()

    self.main_window.mainloop()

  def show_all_cards(self):

    canFrame = Frame(self.main_window)
    canFrame.pack(fill=BOTH, expand=1)

    my_canvas = Canvas(canFrame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(canFrame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

    self.lastframe = Frame(my_canvas)
    my_canvas.create_window((0,0), window=self.lastframe, anchor="nw")

    datas = self.alldata[self.folderindex]["cards"]
    txt=[]
    self.lbl=[]
    btns=[]
    row=0
    i=0

    y= 150

    for dta in datas:
      txt.append(Text(self.lastframe, height=6))
      txt[i].grid(row=row, column=0, pady=(0, 70), padx=10)
      txt[i].config(font=("Courier", 16), width=43,)
      txt[i].delete(1.0,"end")
      txt[i].insert(1.0, dta["content"])
      row += 1
      btns.append(Button(self.lastframe, text="-->", command= lambda ans = {'index': i, "ans": dta["title"]}: self.show_answer(ans)))
      # btns[i].grid(row=row, column=0, pady=(0, 5), padx=(0, 5))
      btns[i].place(y=y, x=10)
      btns[i].config(width=4, font=13)
      self.lbl.append(Label(self.lastframe, text="", relief=FLAT))
      self.lbl[i].place(y=y+5, x=90)
      self.lbl[i].config(font=("Courier", 15))
      y+=208

      row += 1
      i += 1

  def show_answer(self, ans):
    self.lbl[ans['index']].config(text=ans["ans"])
    return self

  def back_folder(self):
    from classes.pages import Pages
    self.main_window.destroy()
    page = Pages(self.folderindex, self.alldata)
    
    return self



