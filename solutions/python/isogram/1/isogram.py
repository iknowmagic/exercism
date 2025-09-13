def is_isogram(string):
   letters = [c for c in string.lower() if c not in (' ', '-')]
   return len(set(letters)) == len(letters)
      