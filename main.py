import tkinter as tk
import gui

main = tk.Tk()
main.title("Caesar Cipher - Main")
main.geometry("800x400")
gui.create_main_window(main)



first_time_setup = True

if first_time_setup:
  setup = tk.Tk()
  setup.title("Caesar Cipher - Setup")
  setup.geometry("400x200")
  setup.attributes('-topmost',True)
  gui.create_setup_window(setup)

main.mainloop()