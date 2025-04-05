# import customtkinter
# from tkinter import *

# customtkinter.set_appearance_mode('dark')
# customtkinter.set_default_color_theme('dark-blue') #cor do botao enviar

# janela = customtkinter.CTk()
# janela.geometry('700x400') #tamanho da tela
# janela.title('Sistema de login')
# janela.iconbitmap('logo.ico') #logo na barra da pagina
# janela.resizable(False, False) #nao deixa mudar o tamanho da tela

# #trabalhando com o foguete
# img = PhotoImage(file='rocket.png')
# label_img = customtkinter.CTkLabel(master = janela, image = img)
# label_img.place(x = 5, y = 45)


# janela.mainloop()


#codigo deepseek pra ver como funciona
import customtkinter as ctk

# Configuração da janela principal
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

janela = ctk.CTk()
janela.geometry("500x400")
janela.title("Sistema de Login")
janela.resizable(False, False)

# Frame principal
frame = ctk.CTkFrame(master=janela, width=400, height=360)
frame.pack(pady=20, padx=20)

# Título principal
label_titulo = ctk.CTkLabel(
    master=frame, 
    text="Entre na sua conta e tenha a plataforma!",
    font=("Arial", 16, "bold")
)
label_titulo.pack(pady=10)

# Subtítulo
label_subtitulo = ctk.CTkLabel(
    master=frame, 
    text="Sistema de Login",
    font=("Arial", 14)
)
label_subtitulo.pack(pady=5)

# Campo Username
label_username = ctk.CTkLabel(
    master=frame, 
    text="Username *",
    font=("Arial", 12),
    anchor="w"
)
label_username.pack(pady=(15, 0), padx=40, fill="x")

entry_username = ctk.CTkEntry(master=frame, width=320)
entry_username.pack(pady=5, padx=40)

# Campo Password
label_password = ctk.CTkLabel(
    master=frame, 
    text="Password *",
    font=("Arial", 12),
    anchor="w"
)
label_password.pack(pady=(15, 0), padx=40, fill="x")

entry_password = ctk.CTkEntry(master=frame, width=320, show="*")
entry_password.pack(pady=5, padx=40)

# Checkbox Lembrar-me
checkbox = ctk.CTkCheckBox(
    master=frame, 
    text="Me lembrar sempre"
)
checkbox.pack(pady=15)

# Botão de Login
botao_login = ctk.CTkButton(
    master=frame, 
    text="Login", 
    width=320,
    fg_color="#1e90ff",
    hover_color="#0066cc"
)
botao_login.pack(pady=10)

janela.mainloop()