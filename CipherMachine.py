import utilities as ut

class CipherMachine:

  def __init__(self, phrase, encryptType, choiceType):
    self.phrase = phrase
    self.encryptType = encryptType
    self.choiceType = choiceType

  # césar cipher
  def cesar(self, parameter):

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

    cryptography = lambda encryptType: encrypt(parameter) if (self.choiceType == 1) else decrypt(parameter)
    return cryptography(self.choiceType)

  # vigenère cipher
  def vigenere(self, keyword):

    def newPhrase(keyword, n = 1, z = 0, newPhrase = ''):
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

    def encrypt(newPhrase, result = ''):

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

    def decrypt(newPhrase, result = ''):

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

    cryptography = lambda encryptType: (encrypt(newPhrase(keyword)), decrypt(newPhrase(keyword)))[self.choiceType == 2]
    return cryptography(self.encryptType)

  # rsa cipher
  def rsa(self, key):

    def encrypt(publicKey, newText=''):
      for letter in self.phrase:
        if letter in ut.simpleCharacters:
          iletter = (ut.simpleCharacters.index(letter))

          c = iletter ** int(publicKey[1]) % int(publicKey[0])

          newText += str(c) + chr(32)

      return newText

    def decrypt(privateKey, newText=''):
      listEncrypted = self.phrase.split()
      for i in listEncrypted:
        c = int(i) ** int(privateKey[1]) % int(privateKey[0])
        newText += ut.simpleCharacters[c]

      return newText

    cryptography = lambda encryptType: encrypt(key) if (self.choiceType == 1) else decrypt(key)
    return cryptography(self.choiceType)