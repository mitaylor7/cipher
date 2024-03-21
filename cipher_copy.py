
# declare variables here so we avoid a case of coding magic numbers
FIRST_CHAR_CODE = ord("A") 
LAST_CHAR_CODE = ord("Z")
CHAR_RANGE = LAST_CHAR_CODE - FIRST_CHAR_CODE + 1
# in ASCII code uppercase and lowercase letters have different ranges of numbers, so in this we're just taking their uppercase position
# ord (ordinal) recognizes the character and assigns it to the ASCII code/unicode position
# to get the range of the characters input and have it loop back around, we subtract the Z position from A and add 1 so it starts at A again

# setting this up as a function so we can then decrypt messages if we wanted without having to write that shit all over again
def caesar_shift(message, shift):
    # result placeholder
    result = ""

    # set up the for loop that reads through each character in the message and converts it to uppercase
    for char in message.upper():
        if char.isalpha(): #checks if character is in the alphabet
            # convert to ASCII
            char_code = ord(char)
            new_char_code = char_code + shift
            # takes the unicode position of the entered character and adds the shift amount, getting a new unicode number and therefore a new character

            #if statements that allow us to loop through the unicode ranges so that if we have a z in our message, it doesn't go outside the bounds of the alphabet
            if new_char_code > LAST_CHAR_CODE:
                new_char_code -= CHAR_RANGE

            if new_char_code < FIRST_CHAR_CODE:
                new_char_code += CHAR_RANGE

            new_char = chr(new_char_code)
            result += new_char
        else: #if the character isnt in the alphabet, we just add it as is
            result += char

    return result

#collecting user input
user_message = input("Message to Encrypt: ")
user_shift_key = int(input("Shift Key (integer): ")) # user input, no matter what it is, is taken as a string so we have to convert it to an int to shift it
cipher_text = caesar_shift(user_message, user_shift_key) # calling on the cipher function we made earlier
print(f"Cipher Text: {cipher_text}") # printing the encrypted message