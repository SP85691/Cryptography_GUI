# import tkinter and filedialog
from tkinter import *
from tkinter import filedialog, messagebox

# Import the encryption and decryption functions from cryptomachine.py
from cryptomachine import encrypt, decrypt


# create an app for encryption and decryption
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Encryption and Decryption")
        self.root.iconbitmap("src/encryption.ico")

        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.root.config(bg="white")

        # create a frame
        self.frame = Frame(self.root, bg="#ff0066")
        self.frame.place(x=0, y=0, height=500, width=500)

        # create a label and create a heading 'Encryption and Decryption'
        self.label = Label(self.frame, text="Encryption and Decryption", font=("Consolas", 20, 'bold'), bg="#ff0066", fg="black")
        self.label.place(x=0, y=0, height=50, width=500)

        # create a label 'Open File'
        self.label = Label(self.frame, text="Open File", font=("consolas", 18, 'bold'), bg="#ff0066", fg="white")
        self.label.place(x=-130, y=70, height=50, width=500)

        # open a file using filedialog
        self.file = Button(self.frame, text="Open File", font=("consolas", 18), bg="green", fg="white", command=self.openfile)
        self.file.place(x=235, y=75, height=40, width=200)

        # create a label for the file name
        self.label = Label(self.frame, text="File Name: ", font=("consolas", 15), bg="white", fg="black")
        self.label.place(x=60, y=150, height=40, width=375)

    def openfile(self):
        # open a file using filedialog
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
        self.label.config(text="File Name: " + self.filename)

        # create a button for encryption
        self.encrypt = Button(self.frame, text="Encrypt", font=("times new roman", 15), bg="#009900", fg="white", command=self.encrypt, activebackground="#ff9933", activeforeground="black")
        self.encrypt.place(x=60, y=250, height=40, width=175)

        # create a button for decryption
        self.decrypt = Button(self.frame, text="Decrypt", font=("times new roman", 15), bg="#ff9933", fg="black", command=self.decrypt, activebackground="#009900", activeforeground="white")
        self.decrypt.place(x=260, y=250, height=40, width=175)

    def list_to_string(self, s):
        # initialize an empty string
        str1 = ""

        # traverse in the string
        for ele in s:
            str1 += ele

        # return string
        return str1

    def encrypt(self):
        # encrypt the opened file 'self.filename'
        file = open(self.filename, 'r')
        data = file.read()
        encrypted_data = encrypt(data, 'E')
        # print(encrypted_data)
        file.close()

        # create a new file and write the encrypted data
        new_file = open("encrypted_file.txt", 'w')
        new_file.write(encrypted_data)
        new_file.close()

        # create a new window for the encrypted data
        self.new_window = Toplevel(self.root)
        self.new_window.title("Encrypted Data")
        self.new_window.geometry("500x500")
        self.new_window.resizable(False, False)
        self.new_window.config(bg="white")

        # create a frame
        self.frame = Frame(self.new_window, bg="#ff0066")
        self.frame.place(x=0, y=0, height=500, width=500)

        # create a label and create a heading 'Encryption and Decryption'
        self.label = Label(self.frame, text="Encrypted Data", font=("Consolas", 20, 'bold'), bg="#ff0066", fg="black")
        self.label.place(x=0, y=0, height=50, width=500)

        # create a text box for the encrypted data
        self.text = Text(self.frame, font=("consolas", 15), bg="white", fg="black")
        self.text.place(x=60, y=120, height=250, width=375)
        self.text.insert(END, encrypted_data)



    def decrypt(self):
        # encrypt the opened file 'self.filename'
        file = open(self.filename, 'r')
        data = file.read()
        decrypted_data = decrypt(data, 'D')
        print(decrypted_data)
        file.close()

        # create a new file and write the encrypted data
        new_file = open("decrypted_file.txt", 'w')
        new_file.write(decrypted_data)
        new_file.close()

        # create a new window for the decrypted data
        self.new_window = Toplevel(self.root)
        self.new_window.title("Decrypted Data")
        self.new_window.geometry("500x500")
        self.new_window.resizable(False, False)
        self.new_window.config(bg="white")

        # create a frame
        self.frame = Frame(self.new_window, bg="#ff0066")
        self.frame.place(x=0, y=0, height=500, width=500)

        # create a label and create a heading 'Encryption and Decryption'
        self.label = Label(self.frame, text="Decrypted Data", font=("Consolas", 20, 'bold'), bg="#ff0066", fg="black")
        self.label.place(x=0, y=0, height=50, width=500)

        # create a text box for the decrypted data
        self.text = Text(self.frame, font=("consolas", 15), bg="white", fg="black")
        self.text.place(x=60, y=120, height=250, width=375)
        self.text.insert(END, decrypted_data)
                   

if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()