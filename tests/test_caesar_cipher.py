import unittest
from caesar_cipher import CaesarCipher


class TestCaesarCipher(unittest.TestCase):

    def test_encrypt(self):
        cipher = CaesarCipher(3)
        encrypted_message = cipher.encrypt("hello world")
        self.assertEqual(encrypted_message, "khoor zruog")

    def test_decrypt(self):
        cipher = CaesarCipher(3)
        decrypted_message = cipher.decrypt("khoor zruog")
        self.assertEqual(decrypted_message, "hello world")

    def test_encrypt_empty_message(self):
        cipher = CaesarCipher(3)
        encrypted_message = cipher.encrypt("")
        self.assertEqual(encrypted_message, "")

    def test_decrypt_empty_message(self):
        cipher = CaesarCipher(3)
        decrypted_message = cipher.decrypt("")
        self.assertEqual(decrypted_message, "")

    def test_punctuation(self):
        cipher = CaesarCipher(3)
        encrypted_message = cipher.encrypt("hello world!")
        self.assertEqual(encrypted_message, "khoor zruog!")

    def test_digits(self):
        cipher = CaesarCipher(3)
        encrypted_message = cipher.encrypt("hello 2024!")
        self.assertEqual(encrypted_message, "khoor 2024!")

    def test_encrypt_mixed_character_case(self):
        cipher = CaesarCipher(3)
        encrypted_message = cipher.encrypt("Hello world")
        self.assertEqual(encrypted_message, "Khoor zruog")

    def test_decrypt_mixed_character_case(self):
        cipher = CaesarCipher(3)
        encrypted_message = cipher.encrypt("Khoor Zruog")
        self.assertEqual(encrypted_message, "Hello World")


if __name__ == "__main__":
    unittest.main()
