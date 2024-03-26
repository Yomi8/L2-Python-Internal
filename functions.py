'''
  Name: Amanda Henderson and Cameron Labes
  James Hargest College
  Programming Internal Python for 2.7 & 2.8 ~ 10 credits
  Due Date: 12 April
'''
import tkinter as tk
import gui

def process_text(widget):
  text = widget.get()
  return text

def process_shift(widget):
  shift = widget.get()
  return shift

# shifts message over by the number of the shift
def encrypt(message, shift):
  output = []
  for character in message:
    if character.isdigit():
      output.append(str(int(character) + shift))
    else:
      if character.isalpha():
        if character.isupper():
          output.append(chr((ord(character) + shift - 65) % 26 + 65))
        else:
          output.append(chr((ord(character) + shift - 97) % 26 + 97))
      else:
        output.append(character)
  output = ''.join(output)
  return output


def decrypt(message, shift):
  return encrypt(message, -shift)

# writing a file from the new decrypted message
def file_write(file_name, message):
  with open(file_name, 'w') as file:
    file.write(message)
    file.close()

def file_save_dialog():
  # File Saving Prompt
  global file_saving
  file_saving = tk.Tk()
  file_saving.title("Caesar Cipher - File Saving")
  file_saving.geometry("0x0")
  gui.create_file_saving_dialog(file_saving)

# read the file from the user input
def file_read(file_name):
  with open(file_name, 'r') as file:
    message = file.readline()
    file.close()
  return message

# shift value input (for checking the number is integer)
def get_shift(message):
  while True:
    try:
        shift = int(input(message))
        break
    except ValueError:
        print("Shift value must be an integer. Please try again.")
  return shift


def file_import(text_entry_box):
  # Input File Prompt
  input_file = tk.Tk()
  input_file.title("Caesar Cipher - Input from File")
  input_file.geometry("400x50")
  gui.create_file_import_dialog(input_file, text_entry_box)

def create_error_dialoge(title, message):
  error_dialoge = tk.Tk()
  error_dialoge.title(title)
  error_dialoge.geometry("400x100")
  error_dialoge.attributes('-topmost',True)

  error_message = tk.Label(
    error_dialoge,
    text=message
  )
  error_message.place()

  user_confirm = tk.Button(
    error_dialoge,
    text = "Ok",
    command = error_dialoge.destroy
  )
  user_confirm.place()
