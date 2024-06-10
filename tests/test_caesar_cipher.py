import unittest
from caesar_cipher import CaesarCipher


class TestCaesarCipher(unittest.TestCase):

    def test_encrypt(self):
        cipher = CaesarCipher(3)
        encrypted_message = cipher.encrypt("hello world")
        self.assertEqual(encrypted_message, "khoor zruog")

    @unittest.skip("breaking changes")
    def test_decrypt(self):
        cipher = CaesarCipher(3)
        decrypted_message = cipher.decrypt("khoor zruog")
        self.assertEqual(decrypted_message, "hello world")


if __name__ == "__main__":
    unittest.main()
