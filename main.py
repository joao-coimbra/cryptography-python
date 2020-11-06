from cryptography import CipherMachine

header = '''
    ********************************************
    *     GOVERNO BRASILEIRO                   *
    *         MINISTÉRIO DO MEIO AMBIENTE      *
    *            DEFESA RADIOATIVA             *
    *                                          *
    ********************************************
'''
welcome = '''
    ********************************************
    *     SISTEMA DE ACESSO                    *
    *         AMBIENTE CONTROLADO              *
    *            SOMENTE PESSOAS AUTORIZADAS   *
    * v01                                      *
    ********************************************
'''
msg = '''
    ********************************************
    *     ESCOLHA O MÉTODO DE SEGURANÇA        *
    *                                          *
    *       CODIFICAÇÃO DE CESAR - 1           *
    *       CODIFICAÇÃO DE VIGENERE - 2        *
    ********************************************
'''
error = 'Entrada Inválida!\nTente novamente.'

print(header, welcome)

while True:

  encryptedText = CipherMachine()

  while True:
    try:
      choice = int(input(f'{msg}\n'))
      print('\n')
      break
    except ValueError:
      print(error)
      continue

  if choice == 1:
    print(encryptedText.cesar())
  elif choice == 2:
    print(encryptedText.vigenere())
  else:
    print(error)
    continue

  if input('Deseja continuar? (s/n): ') == 'n':
    break
