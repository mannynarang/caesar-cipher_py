import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def ceaser(text,shift,direction):
  shifted_msg=""
  if direction =="decode":
    shift=shift*-1
  for character in text :
    if character not in alphabet:
      shifted_msg+=character
    else:
      index = (alphabet.index(character) + shift) % len(alphabet)
      shifted_msg+=(alphabet[index]) 
  print(f"You {direction}d msg is {shifted_msg}")



again = "y"
while again == "y":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  if direction =="encode" or direction == "decode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(text,shift,direction)
    again = input("Would you like to encode or decode another messsage (y) or (n):\n").lower()
  else:
    print("Incorrect input!")

