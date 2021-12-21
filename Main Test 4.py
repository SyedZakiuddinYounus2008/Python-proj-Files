from tkinter import *
from tkinter import filedialog
from tkcalendar import Calendar
from tkinter import messagebox
import os
import csv
import pandas as pd


app = Tk()
app.iconbitmap("logo.ico")
File_selected = False
Folder_selected = False


def start():
    global cal
    global select_date
    cal = Calendar(app, selectmode="day")
    cal.pack()
    select_date = Button(app, text="Select Date",
                         command=lambda: collect_date())
    select_date.pack(pady=20)
    global exit_btn
    exit_btn = Button(app, text="Exit App", command=lambda: app.destroy())
    exit_btn.pack(side=["bottom"])


def start_again():
    reselect_date.destroy()
    continue_with_selected_date.destroy()
    show_date.destroy()
    cal.destroy()
    exit_btn.destroy()
    app.geometry("400x400")
    start()


def get_options():
    cal.destroy()
    select_date.destroy()
    app.geometry("400x400")
    global reselect_date
    global continue_with_selected_date
    reselect_date = Button(app, text="Reselect Date",
                           command=lambda: start_again())
    continue_with_selected_date = Button(
        app, text="Continue", command=lambda: show_settings_btn())
    reselect_date.pack()
    continue_with_selected_date.pack()


def show_settings_btn():
    show_date.destroy()
    reselect_date.destroy()
    continue_with_selected_date.destroy()
    app.geometry("400x400")
    global settings
    settings = Button(app, text="Settings", command=lambda: settings_option())
    settings.pack()


def settings_option():
    settings.destroy()
    global select_file
    global select_folder
    select_file = Button(
        app, text="Select File To View", command=lambda: open_file())
    select_file.pack()
    select_folder = Button(
        app, text="Select folder To Save File In", command=lambda: open_folder())
    select_folder.pack()


def open_folder():
    global folder
    folder = filedialog.askdirectory()
    check_folder()


file = ''


def open_file():
    global file
    file = filedialog.askopenfilename(filetypes=(
        ("CSV files", "*.csv*"), ("All Files", "*.*")))
    check_file()


def check_file():
    global File_selected
    if file == "":
        show_empty_file_error()
        File_selected = False
    else:
        File_selected = True
    check_file_folder()


def show_empty_file_error():
    messagebox.showerror("Select A File To Continue",
                         message="Select A File To Open")


def check_folder():
    global Folder_selected
    if folder == "":
        show_empty_folder_error()
        Folder_selected = False
    else:
        Folder_selected = True
        check_file_folder()


def check_file_folder():
    if Folder_selected == True & File_selected == True:
        show_create_file_option()
    elif Folder_selected == False & File_selected == True:
        show_empty_folder_error()
    elif Folder_selected == True & File_selected == False:
        show_empty_file_error()

    

def show_create_file_option():
    select_file.destroy()
    select_folder.destroy()
    global File_name_type
    File_name_type = Label(app, text="Write The Name Of The File In The Box below And press The Button ")
    File_name_type.pack()
    global file_name
    file_name = Entry(width=40)
    file_name.pack()
    global create_file_btn
    create_file_btn = Button(app, text="Create Attendance File in The Selected Folder", command=lambda: create_file())
    create_file_btn.pack()
    global replace_file_btn
    replace_file_btn = Button(app, text="", command=lambda: replace_file())


def destroy_options():
    create_file_btn.destroy()
    file_name.destroy()
    File_name_type.destroy()
    replace_file_btn.destroy()


def create_file():
    global name_of_file
    name_of_file = file_name.get()
    global save_file_in_folder
    save_file_in_folder = str(folder + "\\" + name_of_file + ".py")
    global file_dir
    file_dir = str(folder + "\\" + name_of_file + ".py")
    if name_of_file == "":
        messagebox.showerror("File Name Error", "File Name Cannot Be Empty")
    elif os.path.exists(file_dir):
        file_already_exists_error()
    else:
        Create_File()


def Create_File():
    global Create_f
    Create_f = open(save_file_in_folder, "w")
    messagebox.showinfo("File Selection Info",
                        "The Attendance File Has Been Created In The Directory You Have Selected")
    global show_date_in_f
    show_date_in_f = "    show_date = tkinter.Label(app,text='The File Was Created On The Selected date: '" + clear_date + ")\n    show_date.pack()\n"
    global file_path
    file_path = '"' + file + '"'
    take_next_action()
    read_and_write_in_file()


def replace_file():
    os.remove(file_dir)
    Create_File()


def take_next_action():
    destroy_options()
    actioning = Label(app, text="To Be Able To Open The Attendance File You Have To First Close This App")
    actioning.pack()

def read_and_write_in_file():
    global file_read
    global txt_file
    file_read = csv.reader(str(file_path))
    


def write_code_in_file():
    Code_to_be_written_file = str("""""")
    Created_File = Create_f
    created_file = Created_File
    created_file.write(Code_to_be_written_file)


def show_empty_folder_error():
    messagebox.showerror("Folder Slelection error",
                         message="Select A Folder To Save The File")


def collect_date():
    global clear_date
    global date
    date = cal.get_date()
    clear_date = "" + date + ""
    show_date.config(text="Selected Date Is : " + cal.get_date())
    get_options()


def file_already_exists_error():
    messagebox.showerror("File Existance",
                         "The Attendance File With Same Name Exists In The Directory You Have Selected")
    show_file_save_options()


def show_file_save_options():
    create_file_btn.config(text="Rename The File")
    replace_file_btn.config(text="Replace The File With Other")
    replace_file_btn.pack()


def File_Folder_error():
    messagebox.showerror()


show_date = Label(text="")
show_date.pack()
start()
app.mainloop()
