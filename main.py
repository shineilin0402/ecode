def encode_password(password):
    encoded_password = ""
    for digit in password:
        shifted_digit = str((int(digit) + 3) % 10)  # shift each digit up by 3 numbers
        encoded_password += shifted_digit
    return encoded_password


def decode_password(encoded_password):
    password = ""
    for digit in encoded_password:
        shifted_digit = str((int(digit) - 3) % 10)  # shift each digit down by 3 numbers
        password += shifted_digit
    return password


# main program loop
while True:
    print("Menu")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    choice = input("Please enter an option: ")

    if choice == "1":
        password = input("Please enter your password to encode: ")
        encoded_password = encode_password(password)
        print("Your password has been encoded and stored!")
    elif choice == "2":
        if not encoded_password:
            print("Please encode a password first.")
        else:
            print(
                f"The encoded password is {encoded_password}, and the original password is {decode_password(encoded_password)}.")
    elif choice == "3":
        break
    else:
        print("Invalid option. Please try again.")