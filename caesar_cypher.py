alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, original_text, shift_amount):

    if direction == "decode":
        shift_amount *= -1

    output_text = ''

    for character in original_text:
        if character not in alphabet:
            output_text += character
        else:
            original_position = alphabet.index(character)
            new_position = (original_position + shift_amount) % (len(alphabet))
            output_text += alphabet[new_position]
    print(f"Here's the result: {output_text}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction=direction, original_text=text, shift_amount=shift)

    rerun_caesar = input("Type 'yes' if you want to go again. Otherwise, type 'no'. \n").lower()
    if rerun_caesar == "no":
        should_continue = False
        print("Goodbye")
