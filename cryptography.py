# define alphabet list
alphabet = list(map(chr, range(97, 123)))

# crypt césar
def cesar(phrase, n, typeEncrypt, result = ''):

    if typeEncrypt == 'encrypt':

        for letter in phrase:
            if letter in alphabet:
                p = alphabet.index(letter)
                c = p + n
                if c > 25:
                    c -= 26

                result += alphabet[c]

            else:
                result += letter

        result = result.upper()

    elif typeEncrypt == 'decrypt':

        for letter in phrase:
            if letter in alphabet:
                c = alphabet.index(letter)
                p = c - n
                if p < 0:
                    p += 26

                result += alphabet[p]

            else:
                result += letter

    else:
        return 'Error typeEncrypt'

    return result

# crypt vigenère
def vigenere(phrase, keyword, typeEncrypt, n = 1, z = 0, newPhrase = '', result = ''):

    for x in range(len(phrase)):
        if phrase[x] in alphabet:
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
            newPhrase += phrase[x]

    if typeEncrypt == 'encrypt':
        for x in range(len(phrase)):
            if phrase[x] in alphabet:
                p = alphabet.index(phrase[x])
                k = alphabet.index(newPhrase[x])
                c = p + k

                if c > 25:
                    c -= 26

                result += alphabet[c]

            else:
                result += phrase[x]

        result = result.upper()
    
    elif typeEncrypt == 'decrypt':
        for x in range(len(phrase)):
            if phrase[x] in alphabet:
                c = alphabet.index(phrase[x])
                k = alphabet.index(newPhrase[x])
                p = c - k

                if p < 0:
                    p += 26

                result += alphabet[p]

            else:
                result += phrase[x]

    else:
        return 'Error typeEncrypt'

    return result