class CaesarCipher:
    """A class for performing Caesar Cipher encryption and decryption"""

    def __init__(self, shift_key) -> None:
        """Initializes a CaesarCipher object with a shift value

        Arguments:
        shift_key (int): shift value (positive for encryption, negative for decryption)
        """
        self.shift_key = shift_key % 26  # Normalize shift value (0-25)
        self.alphabet = list(__import__("string").ascii_lowercase)

    def _shift_char(self, char: str, shift: int, alphabet: list) -> str:
        """Performs actual shifts at character level"""
        index = alphabet.index(char.lower())
        shifted_index = (index + shift) % len(alphabet)
        return alphabet[shifted_index]

    def encrypt(self, message) -> str:
        """Encrypts a message using Caesar Cipher"""
        uppercase = self.uppercase
        lowercase = self.lowercase
        key = self.shift_key
        encrypted_message = ""

        for char in message:
            if char in uppercase:
                index = uppercase.index(char)
                shift = (index + key) % 26
                char = uppercase[shift]

            if char in lowercase:
                index = lowercase.index(char)
                shift = (index + key) % 26
                char = lowercase[shift]

            encrypted_message += char

        return encrypted_message

    def decrypt(self, message) -> str:
        """Decrypts a message using Caesar Cipher"""
        uppercase = self.uppercase
        lowercase = self.lowercase
        key = self.shift_key
        decrypted_message = ""

        for char in message:
            if char in uppercase:
                index = uppercase.index(char)
                shift = (index - key) % 26
                char = uppercase[shift]

            if char in lowercase:
                index = lowercase.index(char)
                shift = (index - key) % 26
                char = lowercase[shift]

            decrypted_message += char

        return decrypted_message
