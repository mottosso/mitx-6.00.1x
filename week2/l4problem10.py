def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    if char.lower() == 'a':
      return True
    if char.lower() == 'e':
      return True
    if char.lower() == 'i':
      return True
    if char.lower() == 'o':
      return True
    if char.lower() == 'u':
      return True
    return False
