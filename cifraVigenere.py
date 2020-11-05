# imports
from utilities import removeSpecialCharacters
from cryptography import vigenere

def cifraVigenere():
# Title
    print('\n\tCifra de Vigenère\n')

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

    # define phrase
    phrase = input(f'\nDigite a frase que deseja {choice}\n-> ').lower()

    # define keyword
    error = False
    while True:
        keyword = input(f'\nDigite a palavra-chave que deseja [não coloque espaços nem números]\n-> ').lower()
        
        for i in range(len(keyword)):
            try:
                int(keyword[i])

                error = True
                print('Digite uma palavra-chave sem espaços ou números.')
                break
            except:
                if keyword[i] == ' ':
                    print('Digite uma palavra-chave sem espaços ou números.')

                    error = True
                    break
                else:
                    pass
            error = False

        if not error:
            break

    # remove special characters
    phrase = removeSpecialCharacters(phrase)
    keyword = removeSpecialCharacters(keyword)

    # script
    if choice == 'criptografar':
        typeEncrypt = 'encrypt'
        print(f'\n{vigenere(phrase, keyword, typeEncrypt)}\n')
    else:
        typeEncrypt = 'decrypt'
        print(f'\n{vigenere(phrase, keyword, typeEncrypt)}\n')