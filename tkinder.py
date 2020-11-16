from tkinter import *
from tkinter import filedialog
from cryptography import CipherMachine
import utilities as ut

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

        #Sétimo Container
        self.setimoContainer = Frame(master)
        self.setimoContainer['pady'] = 20
        self.setimoContainer.pack()

        #Oitavo Container
        self.oitavoContainer = Frame(master)
        self.oitavoContainer['pady'] = 20
        self.oitavoContainer.pack()

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

        #4º container contém botão para escolher o método de criptografia           
        valor_a = IntVar()
        self.button1 = Radiobutton(self.quartoContainer, text='Cifra de Cesar', variable=valor_a, width=12, value=1, command=self.clickCesar)
        self.button2 = Radiobutton(self.quartoContainer, text='Cifra de Vigenère', variable=valor_a, width=12, value=2, command=self.clickVig)
        self.button3 = Radiobutton(self.quartoContainer, text='RSA', variable=valor_a, width=12, value=3, command=self.clickRsa)
        self.button1.pack(side=LEFT)
        self.button2.pack(side=LEFT)
        self.button3.pack(side=LEFT)   

        #5º Container permite digitar o deslocamento/palavra-chave
        self.labelPasse = Label(self.quintoContainer, text="Deslocamento: ", font=self.fontePadrao)        
        self.labelPasse.pack(side=LEFT)
        self.palavraPasse = Entry(self.quintoContainer)
        self.palavraPasse["width"] = 30
        self.palavraPasse["font"] = self.fontePadrao               
        self.palavraPasse.pack(side=LEFT)

        #6º Container exibe botões para criptografar ou descriptografar
        self.cripto = Button(self.sextoContainer)
        self.cripto["text"] = "CRIPTOGRAFAR"
        self.cripto["font"] = ("Calibri","8","bold")
        self.cripto["width"] = 16
        #self.cripto["command"] = self.criptografar
        self.cripto.pack(side=LEFT)
        
        self.descripto = Button(self.sextoContainer)
        self.descripto["text"] = "DESCRIPTOGRAFAR"
        self.descripto["font"] = ("Calibri","8","bold")
        self.descripto["width"] = 16
        #self.descripto["command"] = self.decript
        self.descripto.pack(side=LEFT)        

        #7º Container exibe a mensagem cifrada
        msg = StringVar()
        msg = 'felipe'
        self.mensagem = Label(self.setimoContainer, text=msg, font=self.fontePadrao)
        self.mensagem.pack()

        #8º Container exibe botões para salvamento
        self.abrirArquivo = Button(self.oitavoContainer)
        self.abrirArquivo["text"] = "UPLOAD"
        self.abrirArquivo["font"] = ("Calibri","8","bold")
        self.abrirArquivo["width"] = 12
        self.abrirArquivo["command"] = self.openFile
        self.abrirArquivo.pack(side=LEFT)
        
        self.salvar = Button(self.oitavoContainer)
        self.salvar["text"] = "SALVAR"
        self.salvar["font"] = ("Calibri","8","bold")
        self.salvar["width"] = 12
        self.salvar["command"] = self.save
        self.salvar.pack(side=LEFT)

        self.limpar = Button(self.oitavoContainer)
        self.limpar["text"] = "LIMPAR"
        self.limpar["font"] = ("calibri","8","bold")
        self.limpar['width'] = 12        
        #self.limpar['command'] = self.apagar
        self.limpar.pack(side=RIGHT)

    #Método salvar criptografia
    def save(self):
        senha = self.senha.get()
        mensagem = self.mensagem['text']           
        name = filedialog.asksaveasfile(mode='w', defaultextension=".txt", title="Salve o arquivo criptografado")
        
        if name:
            name.write(f'A senha informada é: {senha} \n')
            name.write(f'A criptografia ou descriptografia é: {mensagem}')            
        print(name)
        print(senha)        

    #Método abrir arquivo para criptografar
    def openFile(self):
        arquivo = filedialog.askopenfile(mode="r", initialdir = "/", title="Escolha o arquivo")
        print(arquivo)

    def clickCesar(self):        
        if self.button1.select:
            self.labelPasse["text"] = "Deslocamento: "
            self.palavraPasse['state'] = NORMAL

    def clickVig(self):
       if self.button2.select:
            self.labelPasse["text"] = "Palavra-Chave"
            self.palavraPasse['state'] = NORMAL
        
    def clickRsa(self):
        if self.button3.select:
            self.labelPasse["text"] = ""
            self.palavraPasse['state'] = DISABLED

    # def criptografar(self):
    #     senha = self.senha.get()
    #     parametro = self.palavraPasse.get()
        
    #     if self.button1.select:
    #         cifraCesar = CipherMachine.cesar(senha, parametro)
    #         self.mensagem['text'] = cifraCesar

root = Tk()
Application(root)
root.mainloop()

