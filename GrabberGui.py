__author__ = 'Abdullah AA'

import tkinter as tk
import GrabAndSave


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.thread_link = tk.Entry(self)
        self.thread_link.pack(side='left')

        self.grab_em = tk.Button(self)
        self.grab_em["text"] = "Grab Images"
        self.grab_em["command"] = self.grab_images
        self.grab_em.pack(side="right")

    def grab_images(self):
        link_string = self.thread_link.get()
        GrabAndSave.ImageGrabber.grab_images(link_string)

root = tk.Tk()
app = Application(master=root)
app.mainloop()