  """Improvement Ideas
    

    """

def sherlockAndAnagrams(s):
  def is_anagram(s1, s2):
    hash_table = {}
    for letter in s1:
      hash_table[letter] = 0
    for letter in s1:
      hash_table[letter] += 1

    for letter in s2:
      if letter in s1 and hash_table[letter] > 0:
        hash_table[letter] -= 1
      else:
        return False
    return True
        
  # return is_anagram("fart", "raft")
  
  anagram_pairs = 0

  # For each possible length of subarray (nothing to test against once it's half of len(s))
  for i in range(1, (len(s) // 2) + 1):
    # For each location of the subarray to test
    for j in range(1, len(s) - i):
      test_array = s[j:j+i+1] # TEST THIS ON PAPER PLZ
      # For each subarray that I test the one at j against
      for k in range(i):
        if is_anagram(test_array, s[j + k:j + k + i]): # TEST THIS ON PAPER PLZ
          anagram_pairs += 1
          
          
# print(sherlockAndAnagrams("shite"))