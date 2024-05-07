import customtkinter 
import string

class Application(): 
    def __init__(self):
        super().__init__()
        self.abrir_janela1()

    def abrir_janela1(self):
        customtkinter.set_appearance_mode("Dark")
        self.janela1 = customtkinter.CTk()
        self.janela1.geometry("500x400")
        self.abrir_janelasla()
        self.janela1.mainloop()

    def abrir_janelasla(self):
        texto1 = customtkinter.CTkLabel(self.janela1, text="Welcome, Sign Up!") 
        texto1.pack(padx=20, pady=20) 
        self.usuario = customtkinter.CTkEntry(self.janela1, placeholder_text="Insert your username") 
        self.usuario.pack(padx=20, pady=20)
        self.senha = customtkinter.CTkEntry(self.janela1, placeholder_text="Insert your password", show="*") 
        self.senha.pack(padx=20, pady=20)
        showPassword = customtkinter.CTkCheckBox(self.janela1, text="Show Password") 
        showPassword.pack(padx=20, pady=20)
        botao1 = customtkinter.CTkButton(self.janela1, text="Login", command=self.clique) 
        botao1.pack(padx=20, pady=20)   

    def abrir_janela2(self):
        janela2 = customtkinter.CTk()
        janela2.geometry("900x600")
        botaologout = customtkinter.CTkButton(janela2, text="Logout")
        botaologout.pack(padx=30, pady=10)
        janela2.mainloop()

       
    def abrir_janela3(self):
        janela3 = customtkinter.CTk()
        janela3.geometry("500x300")
        textowarning = customtkinter.CTkLabel(janela3, text="Wrong user or password")
        textowarning.pack(padx=120, pady=80)
        botao2 = customtkinter.CTkButton(janela3, text="Return", command=janela3.destroy)
        botao2.pack(padx=20, pady=5)
        janela3.mainloop()

    def clique(self): 
        usuario_input = self.usuario.get() 
        senha_input = self.senha.get()     

        if usuario_input == "admin" and senha_input == "admin":
            self.janela1.destroy()
            self.abrir_janela2()
        else:
            self.abrir_janela3()
       
if __name__ == '__main__':
   app = Application()
  