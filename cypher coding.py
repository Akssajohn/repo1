pt = input("Please enter your plaintext: ")
shift = input("Please enter your key: ")
alph = "abcdefghijklmnopqrstuvwxyz"
ciphertext = ""
while isinstance(int(shift), int) == False:
   shift = input("Please enter your key (integers only!): ")
shift = int(shift)
new_ind = 0 
for i in pt:
  if i.lower() in alph:
    new_ind = alph.index(i) + shift
    ciphertext += alph[new_ind % 26]
  else:
    ciphertext += i    
print("The ciphertext is: " + ciphertext)
