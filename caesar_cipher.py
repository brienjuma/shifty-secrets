class CaesarCipher:
    """A class for performing Caesar Cipher encryption and decryption"""

    uppercase = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    lowercase = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]

    def __init__(self, shift_key) -> None:
        """Initializes a CaesarCipher object with a shift value

        Argments:
        shift_key -shift value(positive for encryption, negative for decryption)
        """
        self.shift_key = shift_key % 26  # Normalize shift value (0-25)

    def encrypt(self, message) -> str:
        """Encrypts a message using Caesar Cipher"""
        uppercase = self.uppercase
        lowercase = self.lowercase
        key = self.shift_key
        encrypted_message = ""

        for char in message.lower():
            if char in uppercase:
                index = uppercase.index(char)
                shift = (index + key) % 26
                char = uppercase[shift]

            if char in lowercase:
                index = uppercase.index(char)
                shift = (index + key) % 26
                char = lowercase[shift]

            encrypted_message += char

        return encrypted_message
