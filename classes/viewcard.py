from tkinter import *
from classes.my_data import MyData
from tkinter import messagebox
from time import sleep
class ViewCard:

  def __init__(self, card_index, folderindex,  alldata):
    
    self.card_index = card_index
    self.folderindex = folderindex
    self.shown_answer = False
    self.alldata = alldata
    self.num = card_index + 1
    self.main_window = Tk(className="Flashcard {}".format(self.num))
    self.main_window.geometry("600x850")
    self.build()

  def build(self):
    print("running...")
    btn_frame = Frame(self.main_window, pady=16)
    btn_frame.pack(expand=True, fill=BOTH)

    var = StringVar()
    self.label = Label(btn_frame, text="Flashcard {}".format(self.num), relief=FLAT)
    self.label.config(font=("Courier", 20))
    self.label.pack(fill=BOTH)    

    self.folder_frame = Frame(btn_frame, pady=(60), padx=5, bg="gray") 
    self.folder_frame.pack(expand=True, fill=BOTH)

    self.label2 = Label(self.folder_frame, text="The Content", bg="gray")
    self.label2.config(font=("Courier", 16, "bold"))
    self.label2.place(x=428, y=-30)

    # label.pack(side=LEFT)

    btn_back = Button(self.folder_frame, text="Back", command=self.back_folder, padx=20)
    btn_back.place(x=20, y=-55)


    self.text_desc = Text(self.folder_frame, width=40, height=25)
    self.text_desc.config(font=("Courier", 16))
    self.text_desc.place(x=20, y=30)
    self.text_desc.pack()

    self.text_ans = Text(self.folder_frame, width=40, height=25)
    self.text_ans.config(font=("Courier", 16))
    # self.text_ans.place(x=20, y=30)

    txtdata = self.alldata[self.folderindex]['cards'][self.card_index]["content"]
    answer = self.alldata[self.folderindex]['cards'][self.card_index]["title"]

    self.set_text(txtdata, answer)

    btn_save = Button(self.folder_frame, text="Save / Update", command=self.save_card, padx=20)
    btn_save.place(x=20, y=600)

    self.btn_switch = Button(self.folder_frame, text="-->", command=self.switch_card, padx=20)
    self.btn_switch.place(x=478, y=520)

    btn_prev = Button(self.folder_frame, text="<", command=self.prev_page, padx=20)
    btn_prev.place(x=210, y=600)

    btn_next = Button(self.folder_frame, text=">", command=self.next_page, padx=20)
    btn_next.place(x=290, y=600)  

    self.main_window.mainloop()
  
  def goto_notes(self):
    return self

  def set_text(self, txt, answer):
    self.text_desc.delete(1.0,"end")
    self.text_desc.insert(1.0, txt)
    self.text_ans.delete(1.0,"end")
    self.text_ans.insert(1.0, answer)

  def next_page(self):

    if self.card_index == len(self.alldata[self.folderindex]["cards"]) - 1:
      messagebox.showerror("Error", "There's no more card")
      return
    
    self.card_index +=1
    txtdata = self.alldata[self.folderindex]['cards'][self.card_index]["content"]
    answer = self.alldata[self.folderindex]['cards'][self.card_index]["title"]
    self.set_text(txtdata, answer)
    self.shown_answer = True
    self.switch_card()
    self.label.config(text=("Flashcard {}".format(self.card_index + 1)))

  def prev_page(self):
    if self.card_index == 0:
      messagebox.showerror("Error", "There's no more card")
      return

    self.card_index -=1
    txtdata = self.alldata[self.folderindex]['cards'][self.card_index]["content"]
    answer = self.alldata[self.folderindex]['cards'][self.card_index]["title"]
    self.set_text(txtdata, answer)
    self.shown_answer = True
    self.switch_card()
    self.label.config(text=("Flashcard {}".format(self.card_index + 1)))
    
  def save_card(self):
    from classes.my_data import MyData
    txt = self.text_desc.get("1.0","end-1c")
    ans = self.text_ans.get("1.0","end-1c")
    if txt == "":
      messagebox.showerror("Error", "Fields must not be empty!")
      return
    
    the_data = {
      "title": ans,
      "content": txt
    }

    self.alldata[self.folderindex]['cards'][self.card_index] = the_data
    mydata = MyData()
    mydata.set_data(self.alldata)
    messagebox.showinfo("Success", "Saved Successfully!")
  
  def view_cards(self, dta):
    print(dta)
    return self

  def switch_card(self):
    if self.shown_answer:
      self.shown_answer = False
      # self.text_desc.place(x=20, y=30) 
      self.text_desc.pack()
      self.text_ans.pack_forget()
      self.label2.config(text="The Content")
      self.btn_switch.config(text="-->")
    else:
      self.shown_answer = True
      self.text_desc.pack_forget() 
      # self.text_ans.place(x=20, y=30) 
      self.text_ans.pack()
      self.label2.config(text="The Answer")
      self.btn_switch.config(text="<--")
      
    return self

  def back_folder(self):
    from classes.pages import Pages
    self.main_window.destroy()
    page = Pages(self.folderindex, self.alldata)
    
    return self



