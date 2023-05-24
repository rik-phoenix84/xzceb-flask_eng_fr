"""
This module test the translation function
"""
import unittest
from translator import english_to_french, french_to_english

class TestTranslation(unittest.TestCase):
    def test_french_translation(self):
        text = 'Hello'
        result=english_to_french(text)

        self.assertEqual(result, 'Bonjour')

    def test_english_translation(self):
        text = 'Bonjour'
        result=french_to_english(text)

        self.assertEqual(result, 'Hello')
    

    if __name__ == '__main__':
        unittest.main()
        