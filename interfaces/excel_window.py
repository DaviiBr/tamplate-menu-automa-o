import customtkinter
from tkinter import filedialog, PhotoImage
from PIL import Image, ImageTk

def selecionar_arquivo():
    arquivo = filedialog.askopenfilename(
        title="Selecione um arquivo Excel",
        filetypes=(("Arquivos Excel", "*.xlsx;*.xls"), ("Todos os arquivos", "*.*"))
    )
    if arquivo:
        label_arquivo.configure(text=f"{arquivo.split('/')[-1]}")
        if not botao_automacao:
            criar_botao()
    else:
        label_arquivo.configure(text="Nenhum arquivo selecionado.")

def criar_botao():
    global botao_automacao
    botao_automacao = customtkinter.CTkButton(app_excel,
                                              text='Iniciar Automação',
                                              font=('Arial', 12, 'bold'),
                                              command=automação,
                                              fg_color='#4CAF50',  # Cor verde
                                              hover_color='#45A049')  # Cor verde mais escura ao passar o mouse
    botao_automacao.pack(pady=20)

def automação():
    print('Automatizando papai!')

def open_excel_window():
    customtkinter.set_appearance_mode("dark")
    global app_excel
    app_excel = customtkinter.CTk()
    app_excel.geometry("600x300")
    app_excel.title("Inicializar automação")

    app_excel.configure(fg_color='#22303C') 
    app_excel.iconbitmap('interfaces/icons/logo_engeselt2.ico')

    icone_original = Image.open('interfaces/icons/iconeDCI.png')
    icone_redimensionado = icone_original.resize((128, 128), Image.LANCZOS)
    icone = ImageTk.PhotoImage(icone_redimensionado)

    label_icone = customtkinter.CTkLabel(app_excel, image=icone, text="")
    label_icone.place(relx=1.0, rely=1.0, anchor='se')

    titulo = customtkinter.CTkLabel(app_excel, 
                                    text='Selecione uma planilha', 
                                    font=('Arial', 24, 'bold'),
                                    text_color='#F1F1F1')  # Cor de texto clara
    titulo.pack(pady=20, anchor='center')

    botao = customtkinter.CTkButton(app_excel, 
                                    text="Selecionar",
                                    font=('Arial', 12, 'bold'), 
                                    command=selecionar_arquivo,
                                    fg_color='#2196F3',  # Azul
                                    hover_color='#1976D2')  # Azul mais escuro ao passar o mouse
    botao.pack(pady=10)

    global label_arquivo
    label_arquivo = customtkinter.CTkLabel(app_excel, 
                                            text="", 
                                            font=('Arial', 12, 'bold'),
                                            text_color='#F1F1F1')  # Cor de texto clara
    label_arquivo.pack(pady=10)

    global botao_automacao
    botao_automacao = None

    app_excel.mainloop()
