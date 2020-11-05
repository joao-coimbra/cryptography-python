# imports
from utilities import removeSpecialCharacters
from cryptography import cesar

def cifraCesar():
# Title
    print('\n\tCifra de César\n')

    # data requirement
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

    while True:
        try:
            n = int(input('\nEscolha o parâmetro que será utilizado [1-25]:\n-> '))
            if 1 <= n <= 25:
                break
            else:
                print('Digite um parâmetro entre 1 e 20')
                continue
        except ValueError:
            print('Digite um valor inteiro')

    # define phrase
    phrase = input(f'\nDigite a frase que deseja {choice}\n-> ').lower()

    # remove special characters
    phrase = removeSpecialCharacters(phrase)

    # script
    if choice == 'criptografar':
        typeEncrypt = 'encrypt'
        print(f'\n{cesar(phrase, n, typeEncrypt)}\n')
    else:
        typeEncrypt = 'decrypt'
        print(f'\n{cesar(phrase, n, typeEncrypt)}\n')