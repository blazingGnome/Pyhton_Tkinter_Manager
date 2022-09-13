import tkinter as tk
from  tkinter import  messagebox
from tkinter import filedialog as fd
from PIL import ImageTk, Image

arr = []

class GUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("tkinter window")
        self.root.geometry("700x500")
        self.root.resizable(False, False)
        self.root.image_0 = Image.open('C:/Users/User/Pictures/Camera Roll/Dor/Plar.jpg')
        self.root.bck_end = ImageTk.PhotoImage(self.root.image_0)
        self.lbl = tk.Label(self.root, image=self.root.bck_end)
        self.lbl.place(x=0, y=0)

        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Save as", command=self.saveButton)
        self.savemenu = tk.Menu(self.menubar, tearoff=0)
        self.savemenu.add_command(label="save as", command=self.saveButton)

        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.root.config(menu=self.menubar)

        self.label = tk.Label(self.root, text="Message_Manager", font=('Times New Roman', 20))
        self.label.pack(padx=10, pady=10)

        self.textBox = tk.Text(self.root, height=6, font=('Times New Roman', 16))
        self.textBox.pack(padx=10,pady=10)

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
        self.root.mainloop()

    def show_message(self):
        #print(self.check_state.get())
        global arr
        if self.check_state.get() != 0:
            #print(self.textBox.get("1.0", tk.END))
            messagebox.showinfo(title="Message", message=self.textBox.get('1.0', tk.END))
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
#my_text = tk.Text(tk.Tk(), width=40, height=10,)
#my_text.pack(pady=20)
GUI()
