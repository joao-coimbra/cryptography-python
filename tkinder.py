from tkinter import *
from tkinter import filedialog
from cryptography import CipherMachine

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ('arial','10')

        #Primeiro Container --> Título
        self.primeiroContainer = Frame(master)
        self.primeiroContainer['pady'] = 10
        self.primeiroContainer.pack()

        #Segundo Container --> Nome do usuário + label
        self.segundoContainer = Frame(master)
        self.segundoContainer['padx'] = 20
        self.segundoContainer.pack()

        #Terceiro Container
        self.terceiroContainer = Frame(master)
        self.terceiroContainer['padx'] = 20
        self.terceiroContainer.pack()

        #Quarto Container
        self.quartoContainer = Frame(master)
        self.quartoContainer['pady'] = 20
        self.quartoContainer.pack()

        #Quinto Container
        self.quintoContainer = Frame(master)
        self.quintoContainer['pady'] = 20
        self.quintoContainer.pack()

        #Sexto Container
        self.sextoContainer = Frame(master)
        self.sextoContainer['pady'] = 20
        self.sextoContainer.pack()

        #1º container tem a informação do título
        self.titulo = Label(self.primeiroContainer, text='TERMINAL DE CRIPTOGRAFIA')
        self.titulo['font'] = ('arial','10','bold')
        self.titulo.pack()

        #2º container tem a informação do Nome do usuário
        self.nomeLabel = Label(self.segundoContainer, text='Nome',font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        #3º container permite inserir a senha
        self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        #self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        #4º container contém botão de ação (Button)        
        self.cesar = Radiobutton(self.quartoContainer)
        self.cesar["text"] = "Cifra de Cesar"
        self.cesar["font"] = ("Calibri", "8")
        self.cesar["width"] = 12
        self.cesar["command"] = self.clickCesar
        self.cesar["value"] = 0
        self.cesar.pack(side=LEFT)

        self.vig = Radiobutton(self.quartoContainer)        
        self.vig["text"] = "Cifra de Vigenère"        
        self.vig["font"] = ("Calibri", "8")
        self.vig["width"] = 12
        #self.vig["command"] = self.clickVig
        self.vig["value"] = 1
        self.vig.pack(side=LEFT)

        self.rsa = Radiobutton(self.quartoContainer)
        self.rsa["text"] = "RSA"
        self.rsa["font"] = ("Calibri", "8")
        self.rsa["width"] = 12
        #self.rsa["command"] = self.verificaSenha
        self.rsa["value"] = 2
        self.rsa.pack(side=LEFT)

        #5º Container
        # self.lblIncrementoCesar = Label(self.quintoContainer, text="Deslocamento", font=self.fontePadrao)
        # self.lblIncrementoCesar.pack(side=LEFT)
        # self.incrementoCesar = Entry(self.quintoContainer)
        # self.incrementoCesar["width"] = 30
        # self.incrementoCesar["font"] = self.fontePadrao        
        # self.incrementoCesar.pack(side=LEFT)

        self.labelPasse = Label(self.quintoContainer, text="Palavra-Chave", font=self.fontePadrao)        
        self.labelPasse.pack(side=LEFT)
        self.palavraPasse = Entry(self.quintoContainer)
        self.palavraPasse["width"] = 30
        self.palavraPasse["font"] = self.fontePadrao               
        self.palavraPasse.pack(side=LEFT)

        #6º Container exibe a mensagem cifrada
        self.mensagem = Label(self.sextoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

        self.abrirArquivo = Button(self.sextoContainer)
        self.abrirArquivo["text"] = "Escolha o Arquivo"
        self.abrirArquivo["font"] = ("Calibri","8","bold")
        self.abrirArquivo["width"] = 12
        self.abrirArquivo["command"] = self.openFile
        self.abrirArquivo.pack(side=LEFT)
        
        self.salvar = Button(self.sextoContainer)
        self.salvar["text"] = "Salvar a Cripto"
        self.salvar["font"] = ("Calibri","8","bold")
        self.salvar["width"] = 12
        self.salvar["command"] = self.save
        self.salvar.pack(side=LEFT)

        self.limpar = Button(self.sextoContainer)
        self.limpar["text"] = "Limpar"
        self.limpar["font"] = ("calibri","8","bold")
        self.limpar['width'] = 12        
        #self.limpar['command'] = self.apagar
        self.limpar.pack(side=RIGHT)

    #Método salvar criptografia
    def save(self):       
        name = filedialog.asksaveasfile(mode='w', defaultextension=".txt", title="Salve o arquivo criptografado")
        print(name)

    #Método abrir arquivo para criptografar
    def openFile(self):
        arquivo = filedialog.askopenfile(mode="r", initialdir = "/", title="Escolha o arquivo")
        print(arquivo)

    def clickCesar(self):        
        self.lblIncrementoCesar = Label(self.quintoContainer, text="Deslocamento", font=self.fontePadrao)
        self.lblIncrementoCesar.pack(side=LEFT)

        self.incrementoCesar = Entry(self.quintoContainer)
        self.incrementoCesar["width"] = 30
        self.incrementoCesar["font"] = self.fontePadrao        
        self.incrementoCesar.pack(side=LEFT)

        self.labelPasse.pack_forget()
        self.palavraPasse.pack_forget()        
        
    #     self.incrementoCesar.wait_visibility()

    def clickVig(self):
        self.labelPasse = Label(self.quintoContainer, text="Palavra-Chave", font=self.fontePadrao)
        self.labelPasse.pack(side=LEFT)

        self.palavraPasse = Entry(self.quintoContainer)
        self.palavraPasse["width"] = 30
        self.palavraPasse["font"] = self.fontePadrao        
        self.palavraPasse.pack(side=LEFT)
        self.lblIncrementoCesar.destroy()
        self.incrementoCesar.destroy()
   
        
   
        

root = Tk()
Application(root)
root.mainloop()

