class CaesarCipher:
    """A class for performing Caesar Cipher encryption and decryption"""

    def __init__(self, shift_key) -> None:
        """Initializes a CaesarCipher object with a shift value

        Argments:
        shift_key -shift value(positive for encryption, negative for decryption)
        """
        self.shift_key = shift_key % 26  # Normalize shift value (0-25)
