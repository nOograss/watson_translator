import unittest
from . import translator


class TestTranslator(unittest.TestCase):

    def test_english_to_french(self):
        self.assertEqual(translator.englishToFrench(
            "Hello, how are you today?"),
            "Bonjour, comment vous êtes aujourd'hui?")

    def test_english_to_french_not(self):
        self.assertNotEqual(translator.englishToFrench(
            "Hello, how are you today?"),
            "Au revoir, comment vous êtes aujourd'hui?")

    def test_french_to_english(self):
        self.assertEqual(translator.frenchToEnglish(
            "Ca va bien, merci"),
            "Well, thank you")
            
    def test_french_to_english_not(self):  
        self.assertNotEqual(translator.frenchToEnglish(
            "Comment allez vous ?"),
            "Well, thank you")


if __name__ == '__main__':
    unittest.main()
