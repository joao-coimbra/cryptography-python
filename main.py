from utilities import removeSpecialCharacters
import cifraCesar, cifraVigenere

cont = 's'

hello = '''
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

while cont == 's':
    print(hello)
    print(welcome)
    qualCifra = int(input('''
    ********************************************
    *     ESCOLHA O MÉTODO DE SEGURANÇA        *
    *                                          *
    *       CODIFICAÇÃO DE CESAR - 1           *
    *       CODIFICAÇÃO DE VIGENERE - 2        *
    ********************************************
    '''))

    if qualCifra == 1:
        cifraCesar.cifraCesar()
    elif qualCifra == 2:
        cifraVigenere.cifraVigenere()
    else:
        print('Entrada Inválida!')
    cont = input('Deseja continuar? (S/N) ')
