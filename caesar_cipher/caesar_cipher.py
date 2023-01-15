# Importing required modules
import art


# Main logic of code
''' 
This code defines a function called caesar which takes three parameters as inputs: start_text, shift_amount, and cipher_direction. The function uses the Caesar Cipher technique for encryption and decryption of the text.

The Caesar Cipher is a simple encryption technique in which each letter in the plaintext is shifted a certain number of places down the alphabet.

The function first creates an empty string called end_text which will be used to store the result of the encryption or decryption.

Then, it checks the value of the cipher_direction parameter. If the value is "decode", it multiplies the shift_amount by -1 to reverse the shift for decryption.

Then it enters a for loop, in each iteration it checks if the current character (char) is in the alphabet list or not. If the character is not in the alphabet list, it is added to the end_text without any changes. If the character is in the alphabet list, the function finds the index of that character in the alphabet list and adds the shift_amount to the index. To handle the scenario where the shifted index exceeds the length of the alphabet list, the modulus operator is used to wrap around to the beginning of the list. The shifted character is then added to the end_text string.

Finally, the function prints the result of the encryption or decryption with a message indicating the direction of the operation.

This function allows the user to either encode or decode the text by providing the input text, shift amount, and the direction of the operation.
'''


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""

    if cipher_direction == "decode":
        shift_amount *= -1

    for char in start_text:
        if char not in alphabet:
            end_text += char
        else:
            position = alphabet.index(char)
            new_position = position + shift_amount
            # modulus operator used to wrap around the alphabet list - so that even if the index exceeds limit, it will go around in the list
            end_text += alphabet[new_position % len(alphabet)]

    print(f"Here's the {cipher_direction}d result: {end_text}")


def main():
    looping = True
    while looping:
        # Taking inputs from user
        direction = input(
            "Type 'encode' to encrypt, type 'decode' to decrypt: ")
        text = input("Type your message: ").lower()
        shift = int(input("Type the shift number: "))
        # Modifying shift to be in the range of the alphabet list
        shift = shift % len(alphabet)

        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

        looping_condition = input("\nDo you want to continue? (y/n): ")
        if looping_condition == 'y':
            continue
        elif looping_condition == 'n':
            looping = False
            print("Thank you for using our service.")
        else:
            print("Invalid looping condition")
            looping_condition = input("Do you want to continue? (y/n): ")


if __name__ == '__main__':
    # Initialization of basic variables
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # Pre-requisite before calling the main function
    print(art.logo)

    main()
