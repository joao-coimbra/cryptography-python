# Title
print('\n\tCifra de Vigenère\n')

# vars
# alphabet list
alphabet = list(map(chr, range(97, 123)))

# use in remove special characters
x = ''

# functions
def phrase(x):
    phrase = input(f'\nDigite a frase que deseja {x}\n-> ').lower()
    return phrase

def encrypt(x, n, result = ''):
    # C = P + K (mod 26)
    for c in x:
        if c in alphabet:
            i = alphabet.index(c)
            if i+n > 25:
                i = i - 26 + n
                result += alphabet[i]
            else:
                result += alphabet[i+n]
        else:
            result += c

    return result.upper()

def decrypt(x, n, result = ''):]
    # P = C - K + 26 (mod 26)
    for c in x:
        if c in alphabet:
            i = alphabet.index(c)
            if i-n < 0:
                i = i + 26 - n
                result += alphabet[i]
            else:
                result += alphabet[i-n]
        else:
            result += c

    return result

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

# remove special characters
for c in phrase(choice):
    if c == 'ã' or c == 'á' or c == 'à' or c == 'â' or c == 'ä':
        x += 'a'
    elif c == 'é' or c == 'è' or c == 'ê' or c == 'ë':
        x += 'e'
    elif c == 'í' or c == 'î' or c == 'ï' or c == 'ì':
        x += 'i'
    elif c == 'ó' or c == 'ò' or c == 'ô' or c == 'ö':
        x += 'o'
    elif c == 'ú' or c == 'ù' or c == 'ü':
        x += 'u'
    else:
        x += c

# script
if choice == 'criptografar':
    print(f'\n{encrypt(x, n)}\n')
else:
    print(f'\n{decrypt(x, n)}\n')