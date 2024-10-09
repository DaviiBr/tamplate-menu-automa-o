import customtkinter
from PIL import Image, ImageTk
import input_window
import time


def onclick_button():
    time.sleep(1)
    app.destroy()
    input_window.open_input_window()

customtkinter.set_appearance_mode("dark")
app = customtkinter.CTk()
app.geometry('800x400')
app.title('Menu')

app.configure(fg_color='#22303C') 
app.iconbitmap('interfaces/icons/logo_engeselt2.ico')

icone_original = Image.open('interfaces/icons/iconeDCI.png')
icone_redimensionado = icone_original.resize((128, 128), Image.LANCZOS)
icone = ImageTk.PhotoImage(icone_redimensionado)

label_icone = customtkinter.CTkLabel(app, image=icone, text="")
label_icone.place(relx=1.0, rely=1.0, anchor='se')

titulo = customtkinter.CTkLabel(app, text="Tela Inicial", 
                                font=("Arial", 32, 'bold'), 
                                text_color='white'
                                )
titulo.pack(side='top', anchor='nw', padx=20, pady=(10, 0))

description = customtkinter.CTkLabel(app, text=" Bem vindo(a), fulano, escolha uma automação.",
                                     font=("Arial", 12, 'bold'),
                                     text_color='white'
                                     )
description.pack(side='top', anchor='nw', padx=20, pady=(5, 0))

# Container para os botões
button_frame = customtkinter.CTkFrame(app, 
                                      fg_color='#1A242E', 
                                      border_color='#3C3F47',  
                                      border_width=2,  
                                      corner_radius=15
                                      )
button_frame.place(relx=0.5, rely=0.5, anchor='center')

# Botões grandes
button1 = customtkinter.CTkButton(button_frame, text="Automação Reprovas", width=150, height=50, command=onclick_button)
button1.pack(side='left', padx=10, pady=30)

button2 = customtkinter.CTkButton(button_frame, text="Automação 2", width=150, height=50)
button2.pack(side='left', padx=10, pady=30)

button3 = customtkinter.CTkButton(button_frame, text="Automação 3", width=150, height=50)
button3.pack(side='left', padx=10, pady=30)

app.mainloop()