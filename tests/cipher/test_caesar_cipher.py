import unittest
from src.cipher.caesar_cipher import CaesarCipher


class TestCaesarCipher(unittest.TestCase):

    def test_encrypt(self):
        cipher = CaesarCipher(3)
        encrypted_message = cipher.encrypt("hello world")
        self.assertEqual(encrypted_message, "khoor zruog")


if __name__ == "__main__":
    unittest.main()
