def caesarCipher(s, k):
  """ASCII Guide 
  
  ord(char) -> num
  
  chr(num) -> char

  """
  
  s = list(s)

  for i in range(len(s)):
    char = ord(s[i])
    
    if char >= 65 and char <= 90:   
      char -= 65
      char = (char + k) % 26
      char += 65
    elif char >= 97 and char <= 122:   
      char -= 97
      char = (char + k) % 26
      char += 97
    
    s[i] = chr(char)
    
  s = str(s)
  print(s)

  
s = 'middle-Outz'
caesarCipher(s, 2)