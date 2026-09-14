from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % 26
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Large shift handle
    shift = shift % 26
    
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if result == "no":
        should_continue = False
        print("Goodbye")

# art.py ka content agar alag file nahi hai to ye upar add kar lo:
# logo = ''' 
#  .d8888b.  8888b.  8888888888 .d8888b.   8888b.  8888888b.  
# d88P  Y88b    "88b 888       d88P  Y88b     "88b 888   Y88b 
# 888    888.d888888 88888888  Y88b.  d88P.d888888 888    888 
# 888    888888  888 888          "Y888P"  888  888 888   d88P 
# 888    888"Y888888 888       888888888888 "Y888888 8888888P"  
# '''