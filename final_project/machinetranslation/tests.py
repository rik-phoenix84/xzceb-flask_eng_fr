import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslation(unittest.TestCase):
    def test_french_translation(self):
        text = 'Hello'
        result=englishToFrench(text)

        self.assertEqual(result, 'Bonjour')

    def test_english_translation(self):
        text = 'Bonjour'
        result=frenchToEnglish(text)

        self.assertEqual(result, 'Hello')
    

    if __name__ == '__main__':
        unittest.main()