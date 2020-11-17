from tkinter import *
from utilities import removeSpecialCharacters, alphabet
from CipherMachine import CipherMachine
import re

class App:
  def __init__(self, master=None):
    self.titleFont = ("MS Sans Serif", "16", "bold")
    self.subtitleFont = ("MS Sans Serif", "14", "bold")
    self.basicFont = {
      "family": "Arial",
      "size": "10",
      "weight": "normal",
      "slant": "roman",
      "underline": "0",
      "overstrike": "0"
      }

    self.widget1 = Frame(
      master,
      pady=10,
      padx=20
      )
    self.widget1.pack()

    self.widget2 = Frame(
      master,
      pady=10
      )
    self.widget2.pack()

    self.widget3 = Frame(
      master,
      pady=10
      )
    self.widget3.pack()

    self.widget4 = Frame(master)
    self.widget4.pack()

    self.widget5 = Frame(
      master,
      pady=10
      )
    self.widget5.pack()

    self.widget6 = Frame(
      master,
      pady=10
      )
    self.widget6.pack()

    self.widget6 = Frame(
      master,
      pady=10
      )
    self.widget6.pack()

    self.title = Label(
      self.widget1,
      text="GOVERNO BRASILEIRO",
      font=self.titleFont
      ).pack()

    self.subtitle = Label(
      self.widget1,
      text="TERMINAL DE CRIPTOGRAFIA",
      font=self.subtitleFont
      ).pack()

    self.labelPhrase = Label(
      self.widget3,
      text='Frase',
      font=(
        self.basicFont['family'],
        self.basicFont['size']
        )
      ).pack(side=LEFT)
    self.phrase = Entry(self.widget3)
    self.phrase.pack()

    self.labelInput = Label(
      self.widget4,
      font=(
        self.basicFont['family'],
        self.basicFont['size']
        )
      )
    self.error = Label(
      self.widget4,
      fg='red'
      )
    self.input = Entry(self.widget4)

    self.radioChoiceCipher = {
      'César': '1',
      'Vigenère': '2',
      'RSA': '3'
      }
    self.radioChoiceTypeEncrypt = {
      'Criptografar': '1',
      'Descriptografar': '2'
      }

    self.v1 = IntVar()
    self.v2 = IntVar()

    for (text, value) in self.radioChoiceCipher.items():
      Radiobutton(
        self.widget2,
        text=text,
        variable = self.v1,
        value=value,
        command=self.changeChoiceCipher 
      ).pack(side=LEFT)

    for (text, value) in self.radioChoiceTypeEncrypt.items():
      Radiobutton(
        self.widget5,
        text=text,
        variable = self.v2,
        value=value,
        command=self.changeTypeEncrypt
      ).pack(side=LEFT)

    self.submit = Button(
      self.widget6,
      text='Enviar',
      command=self.submit
    ).pack()

  def changeChoiceCipher(self):
    self.labelInput.pack(side=LEFT)
    self.input.pack()
    if self.v1.get() == 1:
      self.labelInput['text'] = 'Parâmetro'
    elif self.v1.get() == 2:
      self.labelInput['text'] = 'Palavra-chave'
    else:
      if self.v2.get():
        self.changeTypeEncrypt()
      else:
        self.labelInput.pack_forget()
        self.input.pack_forget()

  def changeTypeEncrypt(self):
    if self.v1.get():
      self.labelInput.pack(side=LEFT)
      self.input.pack()
    if self.v1.get() == 3:
      if self.v2.get() == 1:
        self.labelInput['text'] = 'Chave Pública'
      else:
        self.labelInput['text'] = 'Chave Privada'

  def submit(self, error=False):

    if self.v2.get() == 0:
      error = True

    phrase = self.phrase.get()
    phrase = removeSpecialCharacters(phrase)

    if self.v1.get() == 1:
      parameter = self.input.get()
      try:
        int(parameter)
        if 0 < int(parameter) < (len(alphabet) - 1):
          pass
        else:
          self.error['text'] = f'insira um número inteiro entre 1 e {len(alphabet)-1}'
          self.error.pack()
          error = True
      except ValueError:
        self.error['text'] = 'insira um número inteiro'
        self.error.pack()
        error = True
    elif self.v1.get() == 2:
      keyword = self.input.get()
      keyword = removeSpecialCharacters(keyword)
      for c in keyword:
        if c in alphabet:
          self.error.pack_forget()
        else:
          self.error['text'] = 'apenas caracteres alfabéticos'
          self.error.pack()
          error = True
          break
      if keyword == '':
        self.error['text'] = 'campo obrigatório'
        self.error.pack()
        error = True
    elif self.v1.get() == 3:
      key = self.input.get()
      x = re.findall(',', key)

      if x:
        if len(x) != 1:
          self.error['text'] = 'verifique se a vírgula está correta'
          self.error.pack()
          error = True
        else:
          key = tuple(key.replace(' ', '').split(','))
          try:
            int(key[0])
            int(key[1])
            self.error.pack_forget()
          except ValueError:
            self.error['text'] = 'utilize apenas números'
            self.error.pack()
            error = True
      else:
        self.error['text'] = 'separe a key por vírgula'
        self.error.pack()
        error = True
    else:
      error = True

    if not error:
      cipherMachine = CipherMachine(
        phrase=phrase,
        encryptType=self.v1.get(),
        choiceType=self.v2.get()
        )
      if cipherMachine.encryptType == 1:
        newText = cipherMachine.cesar(int(parameter))
      elif cipherMachine.encryptType == 2:
        newText = cipherMachine.vigenere(keyword)
      elif cipherMachine.encryptType == 3:
        newText = cipherMachine.rsa(key)

      print(newText)

root = Tk()
App(root)
root.mainloop()