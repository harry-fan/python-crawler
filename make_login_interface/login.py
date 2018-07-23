import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('小赖带我去成都逛窑子')
window.geometry('650x350') #指定主窗体大小

canvas = tk.Canvas(window, height=550, width=650)  # 绘图组件
image_file = tk.PhotoImage(file = 'welcome.gif')
image= canvas.create_image(0,0,anchor='nw',image=image_file)
canvas.pack(side='top')

tk.Label(window, text='User name:').place(x=150, y=180)
tk.Label(window, text='Password:').place(x=150, y=220)

var_usr_name = tk.StringVar()
var_usr_name.set('example@python.com')
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)

entry_usr_name.place(x=260, y=180)
var_usr_pwd=tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=260,y=220)
def hit_me():
    tk.messagebox.showinfo(title='HAHA', message='走，去逛窑子')

button = tk.Button(window, text='点击我你就知道了', width=13, height=2, command=hit_me)
button.pack()
#tk.Button(window, )

def usr_login():
    pass
def usr_sign_up():
    pass


btn_login = tk.Button(window, text='Login', command=usr_login)
btn_login.place(x=260, y=270)
btn_sign_up = tk.Button(window, text='Sing up', command=usr_sign_up)
btn_sign_up.place(x=350, y=270)

window.mainloop()