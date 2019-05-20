import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
    
    def create_widgets(self):
        self.hi_btn = tk.Button(self)
        self.hi_btn["text"] = 'SayHi!'
        self.hi_btn["command"] = self.say_hi
        self.hi_btn.pack(side="top")

        self.quit_btn = tk.Button(self, text='QUIT', command=self.master.destroy)
        self.quit_btn.pack(side="bottom")


    def say_hi(self):
        print("Hello world!")



if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()        