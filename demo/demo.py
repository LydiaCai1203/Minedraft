import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()    # 窗口的顶部是两个按钮
        self.draw_rectangle()    # 按钮下面是一个矩形
    
    def create_widgets(self):
        self.hi_btn = tk.Button(self)
        self.hi_btn["text"] = 'SayHi!'
        self.hi_btn["command"] = self.say_hi
        self.hi_btn.pack(side="top")

        self.quit_btn = tk.Button(self, text='QUIT', command=self.master.destroy)
        self.quit_btn.pack(side="bottom")

    def say_hi(self):
        print("Hello world!")

    def draw_rectangle(self):
        cv = tk.Canvas(self.master, bg='white')
        cv.create_rectangle(10, 10, 110, 110)
        cv.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()        