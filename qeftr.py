import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog as fd
from PIL import ImageTk, Image
from itertools import count
import pygame
from tkvideo import *

arr = []

class ImageLabel(tk.Label):
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image="")
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc +=2
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)

class GUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Message Manager")
        #self.root.eval('tk::PlaceWindow . center')
        self.root.resizable(False, False)
        width = 700
        height = 500
        width_res = self.root.winfo_screenwidth()
        height_res = self.root.winfo_screenheight()
        self.root.geometry(f"{width}x{height}+{width_res // 2 - width // 2}+{height_res // 2 - height // 2}")

        self.root.image_0 = Image.open('C:/Users/User/Pictures/Camera Roll/Dor/kirby.jpg')
        self.root.bck_end = ImageTk.PhotoImage(self.root.image_0)
        self.lbl = tk.Label(self.root, image=self.root.bck_end)
        self.lbl.place(x=0, y=0)

        self.root.img= ImageTk.PhotoImage(file='C:/Users/User/Pictures/Camera Roll/Dor/pumpkin.png')
        self.root.iconphoto(False, self.root.img)

        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Save as", command=self.saveButton)
        self.savemenu = tk.Menu(self.menubar, tearoff=0)
        self.savemenu.add_command(label="save as", command=self.saveButton)

        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.root.config(menu=self.menubar)

        #self.label = tk.Label(self.root, text="Message_Manager", font=('Times New Roman', 20))
        #self.label.pack(padx=10, pady=10)

        self.textBox = tk.Text(self.root, height=6, font=('Times New Roman', 16))
        self.textBox.pack(padx=10,pady=50)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="Show MessageBox", font=('Times New Roman', 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text='Show Message', font=('Times New Roman', 16), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.button2 = tk.Button(self.root, text='Show all messages', font=('Times New Roman', 16), command=self.Arr_Message)
        self.button2.pack(padx=10, pady=10)

        self.button1 = tk.Button(self.root, text='Exit', font=('Times New Roman', 16), command=exit)
        self.button1.pack(padx=10, pady=5)

        self.button3 = tk.Button(self.root, text='Save message', font=('Times New Roman', 16), command=self.Save_Message)
        self.button3.pack(padx=4, pady=7)
        self.button3.place(x=15, y=10)

        self.button4 = tk.Button(self.root, text='Open File', font=('Times New Roman', 16), command=self.openFile)
        self.button4.pack(padx=10, pady=10)
        self.button4.place(x=560, y=10)

        self.btn = tk.Button(self.root, text='Save as file', font=('Times New Roman', 16), command=self.saveButton)
        self.btn.pack(padx=10, pady=20)
        self.btn.place(x=560, y=375)

        self.btn1 = tk.Button(self.root, text='open image', font=('Times New Roman', 16), command=self.openNewWindow)
        self.btn1.pack(padx=10, pady=20)
        self.btn1.place(x=10, y=375)

        self.btn2 = tk.Button(self.root, text='sound', font=('Times New Roman', 16), command=self.show_sound)
        self.btn2.pack(padx=10, pady=20)
        self.btn2.place(x=10, y=330)

        self.btn3 = tk.Button(self.root, text='Video', font=('Times New Roman', 15), command=self.video)
        self.btn3.pack(padx=10, pady=20)
        self.btn3.place(x=10, y=285)
        self.root.mainloop()

    def show_message(self):
        global arr
        if self.check_state.get() != 0:
            messagebox.showinfo(title="Message", message=self.textBox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="Error", message='Error, You did not check the check box' )
    def Save_Message(self):
        arr.append(self.textBox.get('1.0', tk.END)[:-1])
    def Arr_Message(self):
        string = ""
        for s in arr:
            string += f"\n{s}"
        #string = string[:-1]
        messagebox.showinfo(title="All_Messages", message=string)
        wind = tk.Tk()
        wind.title("All saved messages")
        wind.geometry("400x200")
        wind.label = tk.Label(wind, text=string, font=('Times New Roman', 20))
        wind.label.pack(padx=5, pady=5)

    def openFile(self):
        filepath = fd.askopenfilename(title="Open file", filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        text_file = open(filepath, "rt")
        stuff = text_file.read()
        self.textBox.insert(tk.END, stuff)
        text_file.close()
        #filepath = fd.askopenfilename(title="Open file", filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        #file = open(filepath, 'r+')
        #FiR=file.read()
        #print(file.read())
        #file.close()
        #window = tk.Tk()
        #window.title("File text")
        #window.geometry("300x300")
        #window.label = tk.Label(window, text=FiR, font=('Times New Roman', 20))
        #window.label.pack(padx=5, pady=5)

    def saveButton(self):
        filepath = fd.askopenfilename(title="Open file", filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        text_file = open(filepath, 'wt')
        text_file.write(self.textBox.get(1.0, tk.END))

    def openNewWindow(self):
        filepath = fd.askopenfilename(title="Open file", filetypes=(("all files", "*.*"), ("images", "*.png"), ("images", "*.jpg"),
                                                                    ("Gifs", "*.gif")))
        text_file = open(filepath, "rt")
        text_file.close()

        self.newWindow = tk.Toplevel()
        Image_Name = str(filepath).split('/')[-1]
        self.newWindow.title(Image_Name)
        self.newWindow.image_0 = Image.open(filepath)
        width, height = self.newWindow.image_0.size
        width_res = self.newWindow.winfo_screenwidth()
        height_res = self.newWindow.winfo_screenheight()
        self.newWindow.geometry(f"{width}x{height}+{width_res // 2 - width // 2}+{height_res // 2 - height // 2}")
        self.newWindow.label = ImageLabel(self.newWindow)
        self.newWindow.label.pack()
        self.newWindow.label.load(filepath)

    def show_sound(self):
        filepath = fd.askopenfilename(title="Open file", filetypes=(("music", "*.mp3"), ("all files", "*.*")))
        text_file = open(filepath, "rt")
        text_file.close()
        window = tk.Toplevel()
        window.title("sound")
        width = 220
        height = 235
        width_res = window.winfo_screenwidth()
        height_res = window.winfo_screenheight()
        window.geometry(f"{width}x{height}+{width_res // 2 - width // 2}+{height_res // 2 - height // 2}")
        window.resizable(False, False)
        window.image_0 = Image.open('C:/Users/User/Pictures/Camera Roll/Dor/sound.gif')
        window.label = ImageLabel(window)
        window.label.pack()
        window.label.load('C:/Users/User/Pictures/Camera Roll/Dor/sound.gif')
        pygame.mixer.init()
        def play():
            pygame.mixer.music.load(filepath)
            pygame.mixer.music.play()

        def stop():
            pygame.mixer.music.stop()
        window.btn1 = tk.Button(window, text="play", font=("Arial", 17), command=play)
        window.btn1.pack(pady=10)
        window.btn1.place(x=81, y=85)
        window.btn2 = tk.Button(window, text="Stop", font=("Arial", 13), command=stop)
        window.btn2.pack(pady=9)
        window.btn2.place(x=88, y=140)
    def video(self):
        filepath = fd.askopenfilename(title="Open file", filetypes=(("Vidoes", "*.mp4"), ("all files", "*.*")))
        text_file = open(filepath, "rt")
        text_file.close()
        self.new = tk.Toplevel()
        Image_Name = str(filepath).split('/')[-1]
        self.new.title(Image_Name)
        self.my_label = tk.Label(self.new)
        self.my_label.pack()
        self.player = tkvideo(filepath, self.my_label, loop=1, size=(1280, 720))
        self.player.play()

GUI()
