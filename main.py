"""app entry point"""

import argparse
from caesar_cipher import CaesarCipher


def main():
    parser = argparse.ArgumentParser(description="Caesar Cipher Program")
    parser.add_argument("text", help="The text message to encode or decode")
    parser.add_argument("shift", type=int, help="The algorithms's substituition key")
    parser.add_argument(
        "--mode",
        default="encrypt",
        choices=["encrypt", "decrypt"],
        help="The mode of operation (encrypt or decrypt)",
    )

    args = parser.parse_args()

    cipher = CaesarCipher(args.shift)
    if args.mode == "encrypt":
        encrypted_message = cipher.encrypt(args.text)
        return f"Encrypted text is {encrypted_message}"
    elif args.mode == "decrypt":
        decrypted_message = cipher.decrypt(args.text)
        return f"Decrypted text is {decrypted_message}"
    else:
        raise ValueError(
            "Invalid mode. Choose 'encrypt' or 'decrypt'."
        )  # Handle unexpected mode


if __name__ == "__main__":
    print("Executing....")
    print(main())
