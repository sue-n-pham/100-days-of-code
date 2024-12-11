alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs. ✔️
def encrypt(text, shift, alphabet):
    # TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
    #  by the shift amount and print the encrypted text. ✔️
    code = ""
    for letter in text:
        index = alphabet.index(letter)
        try:
            shifted_letter = alphabet[index + shift]
        except IndexError:
            exception = shift - (26 - index)
            shifted_letter = alphabet[exception]
        code += shifted_letter


    print(code)

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code? ✔️

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message. ✔️
encrypt(text, shift, alphabet)

# CONCEPT CODE
# fruits = ["Apple", "Pear", "Orange"]
# index = fruits.index("Pear") #1
#
# plain_text = "hello"
# shift_amount = int(input("What's the shift number? "))
#
# output = fruits[index + shift_amount]
# print(output)