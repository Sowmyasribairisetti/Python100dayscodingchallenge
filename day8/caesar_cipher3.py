'''TODO-1:
Import and print the logo from art.py when the program starts.

TODO-2:
What happens if the user enters a number/symbol/space that's not in the List alphabet?

Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?

e.g.

original_text = "meet me at 3!"
cipher_text = "XXXX XX XX 3!"
 Hint 1 
TODO-3:
Can you figure out a way to restart the cipher program?

e.g.

Type 'yes' if you want to go again. Otherwise, type 'no'.

If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again.

 Hint 2 '''
import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")


