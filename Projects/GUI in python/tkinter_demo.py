from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

# create main app Window
root = Tk()

# replace title of GUI
root.title("My first GUI")



# replace Icon
# root.iconbitmap(default='favicon.ico')

# set size
# root.minsize(100,100)
# root.maxsize(400,400)
root.geometry("350x500")

# change background color
root.config(bg="#000000")

# add image to background
img = Image.open("flipkart.png")
resized_img = img.resize((80, 80))
img_set = ImageTk.PhotoImage(resized_img)

# place in GUI
img_label = Label(root, image=img_set)
# add padding top
img_label.pack(pady=(10,10))

# handling login form data
def handle_login():
    email = email_input.get()
    password = password_input.get()
    # print(f"Email: {email}, Password: {password}")

    if email == "admin@123" and password == "admin":
        messagebox.showinfo("Login Success", "Welcome to Flipkart")
    else:
        messagebox.showerror("Login Failed", "Invalid email or password")


# add text
text_label = Label(root, text="Welcome to Flipkart",fg='white',bg='black')
text_label.pack(pady=(10,10))
text_label.config(font=("Arial", 14))

email_label = Label(root, text=" Enter Email",fg='white',bg='black')
email_label.pack(pady=(20,5))
email_label.config(font=("Arial", 12))

email_input = Entry(root, width=30, borderwidth=2)
email_input.pack(ipady=6,pady=(1,15))


# password
password_label = Label(root, text=" Enter Password",fg='white',bg='black')
password_label.pack(pady=(20,5))
password_label.config(font=("Arial", 12))

password_input = Entry(root, width=30, borderwidth=2)
password_input.pack(ipady=6,pady=(1,15))

# button
login_btn = Button(root, text="Login", width=20, bg='white', fg='black',command=handle_login)
login_btn.pack(pady=(20,10))
login_btn.config(font=("Arial", 12))


root.mainloop()


