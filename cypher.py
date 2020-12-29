alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)

def cypher(operation,starting_text,shift_number):
    encryption_list = []
    def encrypt(text,shift):



      for letter in text:
        if letter not in alphabet:
            encryption_list.append(letter)
        else:
            for i in range(len(alphabet)):
                if letter == alphabet[i] and (len(alphabet) - 1) < (i + shift):

                    encryption_list.append(alphabet[(i + shift) % len(alphabet)])

                elif letter == alphabet[i] and (len(alphabet) - 1) >= (i + shift):
                        encryption_list.append(alphabet[i + shift])


      print("The encoded text is:", ''.join(encryption_list))

    def decrypt(text,shift):

        for letter in text:
            if letter not in alphabet:

                encryption_list.append(letter)


            else:
                for i in range(len(alphabet)):

                    if letter == alphabet[i] and ((i - shift) < (1 - len(alphabet))):

                        encryption_list.append(alphabet[(i - shift) % len(alphabet)])

                    elif letter == alphabet[i] and ((i - shift) >= (1 - len(alphabet))):

                        encryption_list.append(alphabet[i - shift])

        print("The decoded text is:", ''.join(encryption_list))


    if direction == "encode":
        encrypt(text = starting_text, shift = shift_number)
    elif direction == "decode":
        decrypt(text = starting_text, shift = shift_number)

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    cypher(operation = direction,starting_text = text,shift_number = shift)
    repeat_input = input("Would you like to go again? Type yes or no\n").lower()
    if repeat_input == "yes":
        print("Continue")
        continue
    elif repeat_input == "no":
        print("Program ended")
        break
