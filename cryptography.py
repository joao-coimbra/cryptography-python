import utilities as ut

class CipherMachine:

  def __init__(self):
    self.encryptType = self.defineEncryptType()
    self.phrase = self.defineText()

  def defineText(self):
    # define phrase
    phrase = input(f'\nDigite a frase que deseja {self.encryptType}\n-> ').lower()

    # remove special characters
    phrase = ut.removeSpecialCharacters(phrase)

    return phrase

  def defineEncryptType(self):
    while True:
      choice = input('Deseja [c]criptografar ou [d]descriptografar?\n-> ')

      if choice == 'c' or choice == 'd':
          if choice == 'c':
              choice = 'criptografar'
          else:
              choice = 'descriptografar'
          break
      else:
          print('\nEscolha inválida\n')

    return choice

  # césar cipher
  def cesar(self):

    def parameter():
      while True:
        try:
          parameter = int(input('\nEscolha o parâmetro que será utilizado [1-25]:\n-> '))
          if 1 <= parameter <= 25:
            break
          else:
            print('Digite um parâmetro entre 1 e 20')
            continue
        except ValueError:
          print('Digite um valor inteiro')
      return parameter

    def encrypt(parameter, result = ''):

      for letter in self.phrase:
        if letter in ut.alphabet:
          p = ut.alphabet.index(letter)
          c = p + parameter
          if c > 25:
            c -= 26

          result += ut.alphabet[c]

        else:
          result += letter

      return result.upper()

    def decrypt(parameter, result = ''):

      for letter in self.phrase:
        if letter in ut.alphabet:
          c = ut.alphabet.index(letter)
          p = c - parameter
          if p < 0:
            p += 26

          result += ut.alphabet[p]

        else:
          result += letter

      return result

    cryptography = lambda encryptType: encrypt(parameter()) if (encryptType == 'criptografar') else decrypt(parameter())
    return cryptography(self.encryptType)

  # vigenère cipher
  def vigenere(self):

    def keyword(error = False):
      while True:
        keyword = input(f'\nDigite a palavra-chave que deseja\n[não coloque espaços nem números]\n-> ').lower()
    
        for i in range(len(keyword)):
          try:
            int(keyword[i])

            error = True
            print('Digite uma palavra-chave sem espaços ou números.')
            break
          except:
            if keyword[i] == chr(32):
              print('Digite uma palavra-chave sem espaços ou números.')

              error = True
              break
            else:
              pass
          error = False

        if not error:
          break

      return ut.removeSpecialCharacters(keyword)

    def newPhrase(keyword = keyword(), n = 1, z = 0, newPhrase = ''):
      for x in range(len(self.phrase)):
        if self.phrase[x] in ut.alphabet:
          if z >= len(keyword) * n:
            i = z - len(keyword) * n
            try:
              newPhrase += keyword[i]
            except IndexError:
              n += 1
              i = z - len(keyword) * n
              newPhrase += keyword[i]
          else:
            newPhrase += keyword[z]
            
          z += 1
        else:
          newPhrase += self.phrase[x]

      return newPhrase

    def encrypt(result = ''):

      for x in range(len(self.phrase)):
        if self.phrase[x] in ut.alphabet:
          p = ut.alphabet.index(self.phrase[x])
          k = ut.alphabet.index(newPhrase[x])
          c = p + k

          if c > 25:
            c -= 26

          result += ut.alphabet[c]

        else:
          result += self.phrase[x]

      return result.upper()

    def decrypt(result = ''):

      for x in range(len(self.phrase)):
        if self.phrase[x] in ut.alphabet:
          c = ut.alphabet.index(self.phrase[x])
          k = ut.alphabet.index(newPhrase[x])
          p = c - k

          if p < 0:
            p += 26

          result += ut.alphabet[p]

        else:
          result += self.phrase[x]

      return result

    newPhrase = newPhrase()

    cryptography = lambda encryptType: (encrypt(), decrypt())[encryptType == 'descriptografar']
    return cryptography(self.encryptType)