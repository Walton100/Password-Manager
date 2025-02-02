from tkinter import *
from tkinter import messagebox
from password_generator import password_generator
my_password=None
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()

def generate_password():
    global my_password
    if len(password_entry.get())!=0:
        password_entry.delete(0,END)
        my_password=None
    my_password=password_generator()
    password_entry.insert(END,my_password)


def add():
    new_dict = {
        website_entry.get(): {
            'email': email_entry.get(),
            'password': password_entry.get()
        }
    }

    try:
         with open('password_generator_info.json', 'r') as file:
            data = json.load(file)

    except FileNotFoundError:
        with open('password_generator_info.json', 'w') as file:
            json.dump(new_dict, file, indent=4)
    else:
        data.update(new_dict)
        with open('password_generator_info.json', 'w') as file:
            json.dump(data, file, indent=4)


    if len(website_entry.get())!=0 or len(password_entry.get())!=0:
        ask = messagebox.askokcancel(title='Are You Satisfied',message=f'website:{website_entry.get()}\nemail:{email_entry.get()}\npassword:{password_entry.get()}')
        if ask:

            website_entry.delete(0, END)
            password_entry.delete(0, END)




    elif len(website_entry.get())==0 or len(password_entry.get())==0:
        message=messagebox.showwarning(title='Warning!!',message='Fill all the available entries')



def search():
    my_search=website_entry.get()
    try:
        with open('password_generator_info.json', 'r') as file:
            my_data=json.load(file)
            info=(my_data[my_search])
    except:
        messagebox.showinfo(title='File Error',message='No such file found!')
        website_entry.delete(0,END)
    else:
        email=info['email']
        password=info['password']
        messagebox.showinfo(title=f'{my_search}',message=f'Email:{email}\nPassword:{password}')




window.config(padx=60,pady=50)
window.minsize(500,500)

image=PhotoImage(file='logo.png')

canvas=Canvas(width=200,height=300)

canvas.create_image(130,145,image=image)
canvas.grid(column=1,row=0)

website_label=Label(text='Website:',font=('Times New Roman',10,'bold'))

website_label.grid(column=0,row=1)

email_label=Label(text='Email:',font=('Times New Roman',10,'bold'))
email_label.grid(column=0,row=2)

password_label=Label(text='Password:',font=('Times New Roman',10,'bold'))
password_label.grid(column=0,row=3)

add=Button(text='Add',width=38,command=add)
add.grid(column=1,row=4,columnspan=3)

website_entry=Entry(width=45)
website_entry.grid(column=1,row=1,columnspan=2)
email_entry=Entry(width=45)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0,'waltonemmanuel@yahoo.com')
password_entry=Entry(width=34)
password_entry.grid(column=1,row=3)

generate_password=Button(text='Generate',width=7,command=generate_password)
generate_password.grid(column=2,row=3)

search_button=Button(text='Search',width=7,command=search)
search_button.grid(column=2,row=1)


window.mainloop()