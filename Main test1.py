from time import sleep
from tkinter import *
from tkinter import font
from tkinter import filedialog
from tkinter import messagebox
import csv
import subprocess
import pandas as pd
from pandas.core.indexes.base import Index
app = Tk()

def start():
    app.minsize(500,250)
    app.maxsize(500,250)
    global main_start_frame
    main_start_frame = Frame(app)
    main_start_frame.pack()
    global file_viewing_info
    file_viewing_info = Label(main_start_frame,text="Select  Option  1  if  you  want  to  view  the  file\n  Select  option  2  if  you  want  to  create  the  attendance  file.")
    file_viewing_info.pack(fill = "both",padx = 22,pady = 22,expand=True)
    file_viewing_info.config(font=('Helvetica bold',12))
    global view_file_btn
    view_file_btn = Button(main_start_frame,text="View File",command=lambda:view_file_file_selection())
    view_file_btn.pack(padx=22,pady=22)
    global create_file_btn
    create_file_btn = Button(main_start_frame,text="Create Attendance file")
    create_file_btn.pack(padx=22,pady=22)

def view_file_file_selection():
    main_start_frame.pack_forget()
    global view_file_file_selection_frame
    view_file_file_selection_frame = Frame(app)
    view_file_file_selection_frame.pack()
    global file_selection_note
    file_selection_note = Label(view_file_file_selection_frame,text="The Selected File Should Only Be A csv File")
    file_selection_note.pack(padx=22,pady=22)
    global file_selection_btn
    file_selection_btn = Button(view_file_file_selection_frame,text="Select A File To View",command=lambda:open_file())
    file_selection_btn.pack(padx=22,pady=22)

def open_file():
    global file
    file = filedialog.askopenfilename(filetypes=(
        ("CSV files", "*.csv*"), ("All Files", "*.*")))
    check_file_selected()
    
def check_file_selected():
    file_selected = False
    if file == "":
        file_selected==False
    elif file != "":
        file_selected = True
    if file_selected == True:
        view_file_content()
    elif file_selected == False:
        show_file_error()

def close_file_data_win():
    csv_file_data_frame.destroy()
    file = None

def view_file_content():
    global csv_file_data_frame
    csv_file_data_frame = Toplevel(app)
    file_csv_read = pd.read_csv(file)
    file_content = pd.DataFrame(file_csv_read)
    file_data = Label(csv_file_data_frame,text=file_content)
    file_data.pack()
    done_btn = Button(csv_file_data_frame,text="Ok",command=lambda:close_file_data_win())
    done_btn.pack()
    view_file_file_selection_frame.pack_forget()
    main_start_frame.pack()
    

    
    
def show_file_error():
    messagebox.showerror("File Selection Error","Please Select A File")
start()
app.mainloop()

