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

    def encrypt(self, message: str) -> str:
        """Encrypts a message using Caesar Cipher"""
        encrypted_message = ""

        for char in message:
            if char.isalpha():
                alphabet = (
                    self.alphabet
                    if char.islower()
                    else list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                )
                encrypted_message += self._shift_char(char, self.shift_key, alphabet)
            else:
                encrypted_message += char

        return encrypted_message

    def decrypt(self, message) -> str:
        """Decrypts a message using Caesar Cipher"""
        decrypted_message = ""
        for char in message:
            if char.isalpha():
                alphabet = (
                    self.alphabet
                    if char.islower()
                    else list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                )
                decrypted_message += self._shift_char(char, -self.shift_key, alphabet)
            else:
                decrypted_message += char

        return decrypted_message
