from tkinter import * # chamada da biblioteca tk

janela = Tk() # janela como instância da classe tk

# Parâmetro da janela
janela.title("cadastro")
janela.geometry('800x700')
janela.configure(background= "#11091a")

# label com o texto login
login_txt = Label(janela, text= "Login", font= ('Small Fonts', 40), fg= '#a1ac88', bg= '#11091a')
login_txt.place(x= 340, y=30)

# label nome de usuário
nome_txt = Label(janela, text= "nome de usuário: ", font= ('Small Fonts', 15), fg= '#a1ac88', bg= '#11091a')
nome_txt.place(x= 50, y=250)

#entrada do usuário
entrada_usuario = Entry(janela, font= ('Small Fonts', 15), fg= 'black', bg= 'white')
entrada_usuario.place(x= 212, y=245)


# label senha
senha_txt = Label(janela, text= "senha: ", font= ('Small Fonts', 15), fg= '#a1ac88', bg= '#11091a')
senha_txt.place(x= 145, y=300)

#entrada da senha
entrada_senha = Entry(janela, font= ('Small Fonts', 15), fg= 'black', bg= 'white')
entrada_senha.place(x= 212, y=295)

# função para abrir nova janela enter
def nova_janela1():
    janela.destroy()
    nova_janela1 = Tk()
    # Parâmetro da janela
    nova_janela1.title("cadastro")
    nova_janela1.geometry('800x700')
    nova_janela1.configure(background= "#11091a")


# botão de enter
botao_enter = Button(janela, text= "entrar", command= nova_janela1, font= ('Small Fonts', 15), fg= 'black', bg= '#a1ac88')
botao_enter.place(x= 365, y=400)

# função nova tela de registro
def nova_janela2():
    janela.destroy()
    nova_janela2 = Tk()
    # Parâmetro da janela
    nova_janela2.title("cadastro")
    nova_janela2.geometry('800x700')
    nova_janela2.configure(background= "#11091a")
    login_txt = Label(nova_janela2, text= "registro", font= ('Small Fonts', 40), fg= '#a1ac88', bg= '#11091a')
    login_txt.place(x= 340, y=30)





# botão de registro
botao_registro = Button(janela, text= "registrar", command= nova_janela2, font= ('Small Fonts', 15), fg= 'black', bg= '#a1ac88')
botao_registro.place(x= 355, y=450)


janela.mainloop() # loop da janela