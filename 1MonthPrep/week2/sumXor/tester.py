from sumXor import sumXor

n = int(input())

for i in range(n):
  # print('i:', i)
  correct = 0
  for j in range(i):
    # print(f'{j} ^ {i} = {j ^ i}')
    if j + i == j ^ i:
      correct += 1
      
  sumXor_result = sumXor(i)
  # print(f'hypothetic_correct: {correct}, test_result: {sumXor_result}')
  if correct != sumXor_result:
    print(f'problem!: {i}')
  
      
# print(f'correct: {correct}')
  