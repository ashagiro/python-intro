import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)

def caesar(text, shift, direction):
    shift = shift%26 +1
    crypt = ""
    for letter in text:
        if not letter.isalpha():
            crypt+=letter
            continue
        index = alphabet.index(letter)
        if direction == "encode":
            if index < (len(alphabet)-shift):
                crypt+=alphabet[index+shift]
            else:
                crypt+=alphabet[(index+shift)-27]
        elif direction == "decode":    
            if index < shift+1:
                crypt+=alphabet[(27-shift)+index]
            else:
                crypt+=alphabet[index-shift]    
    print(f"The {direction}d text is {crypt}")

again = True
while again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    restart = input("Do you want to restart again? Type 'yes' to restart, 'no' otherwise. ")
    if not restart == "yes":
        again = False

# def caesar(text, shift, direction):
#     crypt = ""
#     if direction == "decode":
#         shift*=-1
#     for letter in text:
#         index = alphabet.index(letter)
#         if index < (len(alphabet)-shift) and index :
#             crypt+=alphabet[index+shift]
#             print(letter)
#         else:
#             crypt+=alphabet[(index+shift)-27] 
#             # print(letter)
#     print(f"The {direction}d text is {crypt}")
