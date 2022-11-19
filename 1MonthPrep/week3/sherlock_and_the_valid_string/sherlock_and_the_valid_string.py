def isValid(s):
  if len(s) == 0:
    return "YES"
  
  freq_dict = {}
  for char in s:
    if char not in freq_dict:
      freq_dict[char] = 1
    else:
      freq_dict[char] += 1
  
  freqs = []
  for freq in freq_dict.values():
    freqs.append(freq)
  print("freqs: ", freqs)
    
  mx = max(freqs)
  mn = min(freqs)  
  # if mx == mn:
  #   return "YES"
  # elif freqs.count(mn) == 1 and mn == 1:
  #   return "YES"
  # elif mx - mn > 1 or freqs.count(mx) != 1:
  #   return "NO"
  
  # return "YES"
  print('mx: ', mx, 'mn: ', mn)
  
  if mx - mn > 0:
    if freqs.count(mn) == 1 and mn == 1:
      return "YES"
    elif freqs.count(mx) > 1 or mx - mn > 1:
      return "NO"
    
  return "YES"
  
  
string1 = 'jack' # YES
string2 = 'jaack' # YES
string3 = 'jaaack'  # NO
string4 = 'jjaack'  # NO
string5 = 'jjacckk' # YES
string6 = 'jjjaaaccckkkk' #YES
string7 = 'bbbbbaaaaccccc'
print(isValid(string7))