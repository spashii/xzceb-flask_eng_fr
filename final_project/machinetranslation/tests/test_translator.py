import unittest

from translator import englishToFrench, frenchToEnglish

from ibm_cloud_sdk_core.api_exception import ApiException

class TestTranslator(unittest.TestCase):
    def test_englishToFrench_null(self):
        with self.assertRaises(ApiException):
            englishToFrench("")

    def test_frenchToEnglish_null(self):
        with self.assertRaises(ApiException):
            frenchToEnglish("")

    def test_englishToFrench(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

if __name__ == "__main__":
    unittest.main()