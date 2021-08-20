import tkinter as tk

class GameWindow():
    def __init__(self):
        self.start()

    def create_quit_button(self):
        self.quit_button = tk.Button(self.window, command = self.quit, text = 'quit')
        self.quit_button.pack()

    def start(self):
        self.window = tk.Tk()
        self.create_quit_button()
        self.window.mainloop()

    def quit(self):
        self.window.destroy()

    def create_myhand_frame():
        self.myhand_frame = tk.Frame(self.window)
        self.myhand_frame.place()
