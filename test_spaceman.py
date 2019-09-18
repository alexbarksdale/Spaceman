import spaceman
import unittest
import re

"""Checks to see if the load_word() function loaded a word."""


class LoadWordTest(unittest.TestCase):
    def test_load_word(self):
        self.assertIsNotNone(spaceman.load_word(), 'Word was loaded')


"""
THIS TEST WILL FAIL: Checks to see if the win_checker() function will return True and False.
Remove assertFalse for success.
"""


class WinCheckerTest(unittest.TestCase):
    secret_word = 'rabbit'

    def test_win_checker(self):
        self.assertTrue(spaceman.win_checker(self.secret_word),
                        'Secret word returned True')
        self.assertFalse(spaceman.win_checker('falseWord'),
                         'Secret word returned False')


"""
Checks to see if the regex pattern will detect any non-letter characters and numbers.
If it detects a non-letter character it will fail.
"""


class RegexCheckTest(unittest.TestCase):

    def test_regex(self):
        self.assertRegex('a', r'^[a-zA-Z]*$', 'Letter passed regex')


if __name__ == '__main__':
    unittest.main()
