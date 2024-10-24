# Password Encoder/Decoder Program

# Encoder Function
def encode(password):
    encoded_password = ""
    for digit in password:
        encoded_password += str((int(digit) + 3) % 10)  # Shift each digit by 3
    return encoded_password

# Main function with menu
def main():
    encoded_password = ""

    while True:
        print("\nMenu\n-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = input("Please enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            if len(password) == 8 and password.isdigit():
                encoded_password = encode(password)
                print("Your password has been encoded and stored!")
            else:
                print("Invalid input. Please enter an 8-digit password.")

        elif option == "2":
            if encoded_password:
                decoded_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
            else:
                print("No encoded password found. Please encode a password first.")

        elif option == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
