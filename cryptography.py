# define alphabet list
alphabet = list(map(chr, range(97, 123)))

def cesar(x, n, typeEncrypt, result = ''):

    if typeEncrypt == 'encrypt':

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

        result = result.upper()

    elif typeEncrypt == 'decrypt':

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

    else:
        return 'Error typeEncrypt'

    return result