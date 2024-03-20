import tkinter as tk
from typing import Text
from functions import encrypt, decrypt, file_write, file_read, get_shift
from time import sleep



main = tk.Tk()
main.title("Caesar Cipher - Main")
main.geometry("800x400")

text_entry_box = tk.Text(
  main,
  width=30,
  height=15
)

text_entry_box.pack()

output_box = tk.Text(
  main,
  state="disabled",
  width=30,
  height=18
)

output_box.pack()

shift_box_label = tk.Label(
  main,
  text="Shift:"
)

shift_box = tk.Entry(
  main,
  width=10
)
shift_box.pack()





letter_shift_value_label = tk.Label(main, text="Current Shift Value:")


digit_shift_value_label = tk.Label(main, text="Current Shift Value:")





options_button = tk.Button(
  main,
  text="Options",
  width=10,
  height=2,
)
options_button.pack()

file_button = tk.Button(
  main,
  text="Enter text from file",
  width=24,
  height=1,
)
file_button.pack()

go_button = tk.Button(
  main,
  text="Go!",
  width=10,
  height=2,
)
go_button.pack()

# Main Window Element Positions
text_entry_box.place(x=30,y=10)
file_button.place(x=30,y=250)
options_button.place(x=30,y=300)
go_button.place(x=650,y=300)
output_box.place(x=540,y=10)
shift_box_label.place(x=260,y=305)
shift_box.place(x=300,y=305)



# options window
options = tk.Tk()
options.title("Caesar Cipher - Options")
options.geometry("0x0")

mode_label = tk.Label(options, text="Mode", fg="white", bg="black")

decrypt_button = tk.Button(
    options,
    text="Decrypt",
    width=25,
    height=5,
)
decrypt_button.pack()

encrypt_button = tk.Button(
  options,
  text="Encrypt",
  width=25,
  height=5,
)
encrypt_button.pack()


# Options Window Element Positions
encrypt_button.place(x=200,y=200)
decrypt_button.place(x=200,y=250)

# File Saving Prompt
file_saving = tk.Tk()
file_saving.title("Caesar Cipher - File Saving")
file_saving.geometry("0x0")

file_name_label = tk.Label(
  file_saving,
  text="Would you like to save the result to a file? "
)

yes_file_button = tk.Button(
  file_saving,
  text="Yes",
  width=25,
  height=5,
)
yes_file_button.pack()

no_file_button = tk.Button(
  file_saving,
  text="Encrypt",
  width=25,
  height=5,
)
no_file_button.pack()

# File Saving Window Element Positions
yes_file_button.place(x=200,y=200)
no_file_button.place(x=200,y=250)


# Input File Prompt
input_file = tk.Tk()
input_file.title("Caesar Cipher - Input from File")
input_file.geometry("0x0")

file_name_label = tk.Label(
  file_saving,
  text="Enter the file name of the text you would like to enter: "
)

file_name_entry = tk.Entry(
  file_saving,
  width=5
)

main.mainloop()




