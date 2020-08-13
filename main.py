import itertools, string

# get the possible ascii pswrds
three_ints_perms = list(itertools.permutations(list(range(97,123)), 3))

# open the encrypted text
f = open('encryptedASCIIvalues.txt')
ASCIIValsList = f.read().split(',')

# go through each
for pswrd in three_ints_perms:
  XORdVals = []
  i = 0
  while i < len(ASCIIValsList):
    intXOR = int(ASCIIValsList[i])^pswrd[i%3]
    XORdVals.append(chr(intXOR))
    i += 1
  completedDecryption = ''.join(XORdVals)
  if('An extract taken from ' in completedDecryption):
    sumOfAscii = sum(list(map(lambda x:int(ord(x)), list(completedDecryption))))
    input('----------------\n\n{}\n\nPassword: {}\nSum of ASCII: {}'.format(completedDecryption, pswrd, sumOfAscii))