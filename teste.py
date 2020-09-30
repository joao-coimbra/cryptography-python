alphabet = list(map(chr, range(97, 123)))

phrase = 'souojoaozinho'
keyWord = 'limao'

newPhrase = ''
n = 1

lengthPhrase = len(phrase)

for x in range(0, lengthPhrase):
    if x >= len(keyWord) * n:
        i = x - len(keyWord) * n
        try:
            newPhrase += keyWord[i]
        except IndexError:
            n += 1
            i = x - len(keyWord) * n
            newPhrase += keyWord[i]
    else:
        newPhrase += keyWord[x]

print(newPhrase)


# # for i, c in enumerate(x):

# #     print(i)
