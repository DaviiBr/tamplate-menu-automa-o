import customtkinter
from PIL import Image, ImageTk
import time
import excel_window

def get_data():
    email = textboxName.get()
    senha = textboxPassword.get()
    print("Email", email)
    print("Senha", senha)
    time.sleep(1)
    app_input.destroy()
    excel_window.open_excel_window()

def open_input_window():

    global app_input
    app_input = customtkinter.CTk()
    app_input.geometry('600x300')
    app_input.title('Login')
    app_input.configure(fg_color='#22303C') 
    app_input.iconbitmap('interfaces/icons/logo_engeselt2.ico')

    icone_original = Image.open('interfaces/icons/iconeDCI.png')
    icone_redimensionado = icone_original.resize((128, 128), Image.LANCZOS)
    icone = ImageTk.PhotoImage(icone_redimensionado)

    label_icone = customtkinter.CTkLabel(app_input, image=icone, text="")
    label_icone.place(relx=1.0, rely=1.0, anchor='se')

    titulo = customtkinter.CTkLabel(app_input, text='Login do eControl', font=('Arial', 18, 'bold'), text_color='#F1F1F1')
    titulo.pack(pady=20, anchor='center')

    input_frame = customtkinter.CTkFrame(app_input, fg_color='#1A242E', border_color='#3C3F47', border_width=2, corner_radius=15)  
    input_frame.pack(pady=20, padx=20, anchor='center')

    email_text = customtkinter.CTkLabel(input_frame, text='Email', font=('Arial', 12, 'bold'), text_color='#f1f1f1')
    email_text.grid(row=0, column=0, padx=(10, 20), pady=(20, 5), sticky='w')

    global textboxName
    textboxName = customtkinter.CTkEntry(input_frame, width=300)
    textboxName.grid(row=0, column=1, padx=(10, 20), pady=(20, 5))

    password_text = customtkinter.CTkLabel(input_frame, text="Senha", font=('Arial', 12, 'bold'), text_color='#F1F1F1')
    password_text.grid(row=1, column=0, padx=(10, 20), pady=(10, 20), sticky='w')

    global textboxPassword
    textboxPassword = customtkinter.CTkEntry(input_frame, width=300)
    textboxPassword.grid(row=1, column=1, padx=(10, 20), pady=(10, 20))

    botao_submit = customtkinter.CTkButton(app_input, text='Enviar', command=get_data, font=('Arial', 12, 'bold'), fg_color='#007BFF', hover_color='#0056b3')
    botao_submit.pack(pady=20)

    app_input.mainloop()
