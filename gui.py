import tkinter as tk
import functions


global mode
mode = 0

def create_main_window(root):
  def go():
    text = text_entry_box.get("1.0", "end-1c")
    try:
      shift = int(shift_box.get())
      if -27 < shift < 27:
        if mode == 0:
          result = functions.encrypt(text, shift)
        else:
          result = functions.decrypt(text, shift)
        output_box.config(state="normal")
        output_box.delete(1.0, tk.END)
        output_box.insert(tk.END, result)
        output_box.config(state="disabled")
      else:
        functions.create_error_dialoge("Error! Number out of range.", "Please enter a shift number between -26 and 26.")
        shift_box.delete(1, tk.END)
        
    except(TypeError, ValueError):
      functions.create_error_dialoge("Error! Invalid input.","Please enter a number between -26 and 26.")
      shift_box.delete(1, tk.END)
      

  def set_mode_encrypt():
    global mode
    mode = 0

  def set_mode_decrypt():
    global mode
    mode = 1

  menubar = tk.Menu()
  settings_menu = tk.Menu(menubar, tearoff=False)
  theme_menu = tk.Menu(menubar, tearoff=False)
  theme_menu.add_radiobutton(
      label="Encrypt",
      command=set_mode_encrypt
  )
  theme_menu.add_radiobutton(
      label="Decrypt",
      command=set_mode_decrypt
  )
  settings_menu.add_cascade(menu=theme_menu, label="Type")
  menubar.add_cascade(menu=settings_menu, label="Mode")
  root.config(menu=menubar)
  
  text_entry_box = tk.Text(
    root,
    width=30,
    height=15
  )
  text_entry_box.pack()
    
  output_box = tk.Text(
    root,
    state="disabled",
    width=30,
    height=15
  )
  
  output_box.pack()
  
  shift_box_label = tk.Label(
    root,
    text="Shift:"
  )
  
  shift_box = tk.Entry(
    root,
    width=10
  )
  shift_box.pack()
  
  letter_shift_value_label = tk.Label(
    root,
    text="Current Shift Value:"
  )
  
  digit_shift_value_label = tk.Label(
    root,
    text="Current Shift Value:"
  )
  
  file_button = tk.Button(
    root,
    text="Enter text from file",
    width=24,
    height=1,
    command=lambda: functions.file_import(text_entry_box)
  )
  file_button.pack()
  
  go_button = tk.Button(
    root,
    text="Go!",
    width=10,
    height=2,
    command=go
  )
  go_button.pack()
  
  text_entry_box.place(x=30,y=10)
  file_button.place(x=30,y=250)
  go_button.place(x=560,y=300)
  output_box.place(x=540,y=10)
  shift_box_label.place(x=30,y=305)
  shift_box.place(x=70,y=305)

def create_setup_window(root):
  def window_close():
    global mode
    mode_choice = default.get()
    if mode_choice == 'Decrypt':
      mode = 1
    else:
      mode = 0
    root.destroy()
  
  mode_label = tk.Label(
    root,
    text="Mode",
  )
  
  default = tk.StringVar(root)
  choices = {'Encrypt','Decrypt'}
  default.set('Encrypt')

  modeMenu = tk.OptionMenu(root, default, *choices)

  def change_dropdown(*args):
      print(default.get())

  default.trace_add('write', change_dropdown)
  
  close_button = tk.Button(
    root,
    text="Close",
    command=window_close
  )
  
  # Options Window Element Positions
  mode_label.place(x=180,y=10)
  modeMenu.place(x=150,y=50)
  close_button.place(x=170,y=150)


def create_file_saving_dialog(root):

  file_name_label = tk.Label(
    root,
    text="Would you like to save the result to a file?"
  )
  file_name_label.pack()

  yes_file_button = tk.Button(
    root,
    text="Yes",
    width=25,
    height=5,
  )
  yes_file_button.pack()

  no_file_button = tk.Button(
    root,
    text="No",
    width=25,
    height=5,
  )
  no_file_button.pack()

  # File Saving Window Element Positions
  yes_file_button.place(x=200,y=200)
  no_file_button.place(x=200,y=250)

def create_file_import_dialog(root, text_entry_box):
  def import_file():
    file_name = file_name_entry.get()
    message = functions.file_read(file_name)
    text_entry_box.delete(1.0, tk.END)
    text_entry_box.insert(tk.END, message)
    root.destroy()

  file_name_label = tk.Label(
    root,
    text="Enter the file name of the text you would like to enter:"
  )
  file_name_label.pack()

  file_name_entry = tk.Entry(
    root,
    width=15
  )
  file_name_entry.pack()

  file_entry_confirmation = tk.Button(
    root,
    text="Enter",
    width=5,
    command=import_file
  )
  file_entry_confirmation.place(x=250,y=20)


