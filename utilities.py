alphabet = list(map(chr, range(97, 123)))

def removeSpecialCharacters(phrase, result = ''):
  for c in phrase:
    if c == 'ã' or c == 'á' or c == 'à' or c == 'â' or c == 'ä':
      result += 'a'
    elif c == 'é' or c == 'è' or c == 'ê' or c == 'ë':
      result += 'e'
    elif c == 'í' or c == 'î' or c == 'ï' or c == 'ì':
      result += 'i'
    elif c == 'ó' or c == 'ò' or c == 'ô' or c == 'ö':
      result += 'o'
    elif c == 'ú' or c == 'ù' or c == 'ü':
      result += 'u'
    elif c == 'ç':
      result += 'c'
    else:
      result += c
  return result