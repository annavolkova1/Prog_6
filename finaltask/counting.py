def generator_function(str):
    for word in str.split():
        yield word


def count_letters(str):
    for item in generator_function(str):
        print({item: len(item)})


def count_words(words):
    return words.count(' ') + 1


words = "Hello World"
print(count_letters(words))
print(count_words(words))

import unittest


class TestStatisticalFunctions(unittest.TestCase):
    def test_count_word(self):
        self.assertEqual(count_words('Hello World'), 2)

    def test_count_false_word(self):
        self.assertNotEqual(count_words('Hello dear friend'), 5)

    def test_count_letters(self):
        self.assertEqual(count_letters('Hello World'), None, None)

    def test_count_letters_false(self):
        self.assertNotEqual(count_letters('Hello dear friend'), 5)


if __name__ == '__main__':
    unittest.main()
