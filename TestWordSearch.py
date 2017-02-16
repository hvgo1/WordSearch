import unittest
import WordSearch
from WordSearch import Puzzle
from WordSearch import Word
from WordSearch import WordSearch

class TestWordSearch(unittest.TestCase):

    def test_word_found_in_every_direction(self):
        # Test setup
        grid = puzzleObj1.grid
        words = ["NUM", "SYLLABLES", "SIMILE", "DIAMONTE"]
        startCoordinates = [(5, 0), (8, 8), (7, 1), (9, 7)]
        endCoordinates = [(7, 0), (0, 8), (7, 7), (9, 0)]
        for i in range(len(directions)):
            wordName = list(words[i])
            wordObj = Word(wordName)
            wordObj.startCoord = startCoordinates[i]
            expr = wordSearchObj._WordSearch__find_word_in_direction(
                grid, wordObj, directions[i])
            self.assertTrue(expr, "{} found in {} {}.".format(
                wordObj.name, wordObj.startCoord, wordObj.endCoord))

    def test_word_not_found_in_every_direction(self):
        # Test setup
        grid = puzzleObj2.grid
        wordName = list("POETRY")
        wordObj = Word(wordName)
        wordObj.startCoord = (5, 5)
        for i in range(len(directions)):
            expr = wordSearchObj._WordSearch__find_word_in_direction(
                grid, wordObj, directions[i])
            self.assertFalse(expr, "{} not found {}.".format(
                wordObj.name, directions[i]))

    def test_find_word_out_of_bounds(self):
        grid = puzzleObj2.grid
        wordName = list("OSLO")
        wordObj = Word(wordName)
        startCoordinates = [(1, 1), (1, 1), (9, 9), (9, 9)]
        for i in range(len(directions)):
            wordObj.startCoord = startCoordinates[i]
            expr = wordSearchObj._WordSearch__find_word_in_direction(
                grid, wordObj, directions[i])
            self.assertFalse(expr, "{} starting at {}-{} is out of bounds.".format(
                wordObj.name, wordObj.startCoord, directions[i]))

    def test_last_letter_not_found(self):
        grid = puzzleObj2.grid
        wordName = list("MOOD")
        wordObj = Word(wordName)
        startCoordinates = [(1, 1), (9, 9), (1, 1), (9, 9)]
        for i in range(len(directions)):
            wordObj.startCoord = startCoordinates[i]
            expr = wordSearchObj._WordSearch__find_word_in_direction(
                grid, wordObj, directions[i])
            self.assertFalse(expr, "Last letter of {}(direction: {})" \
                " was not found at the computed end coordinates.".format(
                wordObj.name, directions[i]))

    def test_word_found_in_puzzle(self):
        grid = puzzleObj1.grid
        words = ["BALL", "COUPLETS", "RHYME", "POETRY"]
        for i in range(len(words)):
            wordName = list(words[i])
            wordObj = Word(wordName)
            expr = wordSearchObj._WordSearch__find_word(grid, wordObj)
            self.assertTrue(expr, "{} {} {}".format(
                wordObj.name, wordObj.startCoord, wordObj.endCoord))

    def test_word_not_found_in_puzzle(self):
        grid = puzzleObj1.grid
        words = ["DISNEY", "MOUSE", "RHYMES", "PATTERNS"]
        for i in range(len(words)):
            wordName = list(words[i])
            wordObj = Word(wordName)
            expr = wordSearchObj._WordSearch__find_word(grid, wordObj)
            self.assertFalse(expr, "{} not found.".format(
                wordObj.name))

    def test_word_with_multiple_instance_found_in_puzzle(self):
        grid = puzzleObj1.grid
        words = ["TIC", "CIT"]
        for i in range(len(words)):
            wordName = words[i]
            wordObj = Word(wordName)
            expr = wordSearchObj._WordSearch__find_word(grid, wordObj)
            self.assertTrue(expr, "{} has multiple instances.".format(
                wordObj.name))

    def test_term_with_two_words_found_in_puzzle(self):
        grid = puzzleObj1.grid
        words = puzzleObj1.words
        for i in range(len(words)):
            wordName = words[i]
            wordObj = Word(wordName)
            expr = wordSearchObj._WordSearch__find_word(grid, wordObj)
            self.assertTrue(expr, "{} is composed of two words.".format(
                wordObj.name))

    def test_term_in_lower_case_found_in_puzzle(self):
        grid = puzzleObj3.grid
        words = puzzleObj3.words
        for i in range(len(words)):
            wordName = words[i]
            wordObj = Word(wordName)
            expr = wordSearchObj._WordSearch__find_word(grid,wordObj)
            self.assertTrue(expr, "{} cannot be found.".format(
                i + 1, wordObj.name))

    def test_input_file_has_no_grid(self):
        expr, text = puzzleObj4.set_puzzle(test4_input_path)
        self.assertFalse(expr, "{} (Input file: {})".format(
            text, test4_input_path))

    def test_grid_has_unequal_dimensions(self):
        expr, text = puzzleObj5.set_puzzle(test5_input_path)
        self.assertFalse(expr, "{} (Input file: {})".format(
            text, test5_input_path))

    def test_input_file_has_no_list_of_words(self):
        expr, text = puzzleObj6.set_puzzle(test6_input_path)
        self.assertFalse(expr, "{} (Input file: {})".format(
            text, test6_input_path))

    def test_grid_contains_missing_letters(self):
        expr, text = puzzleObj7.set_puzzle(test7_input_path)
        self.assertFalse(expr, "{} (Input file: {})".format(
            text, test7_input_path))

if __name__ == '__main__':
    wordSearchObj = WordSearch()
    directions = ["ACROSS", "BACKWARDS", "DOWN", "UP"]

    # Test Input 1 - Input has grid and list of words
    test1_input_path = "test\\test1.pzl"
    puzzleObj1 = Puzzle(test1_input_path)
    puzzleObj1.clear_values()
    puzzleObj1.set_puzzle(test1_input_path)

    # Test Input 2 - Input has grid and list of words
    test2_input_path = "test\\test2.pzl"
    puzzleObj2 = Puzzle(test2_input_path)
    puzzleObj2.clear_values()
    puzzleObj2.set_puzzle(test2_input_path)

    # Test Input 3 - Words are in lower case
    test3_input_path = "test\\test3.pzl"
    puzzleObj3 = Puzzle(test3_input_path)
    puzzleObj3.clear_values()
    puzzleObj3.set_puzzle(test3_input_path)

    # Test Input 4 - Test input does not have a grid
    test4_input_path = "test\\test4.pzl"
    puzzleObj4 = Puzzle(test4_input_path)
    puzzleObj4.clear_values()

    # Test Input 5 - Grid has unequal dimensions
    test5_input_path = "test\\test5.pzl"
    puzzleObj5 = Puzzle(test5_input_path)
    puzzleObj5.clear_values()

    # Test Input 6 - Test input does not contain a list of words
    test6_input_path = "test\\test6.pzl"
    puzzleObj6 = Puzzle(test6_input_path)
    puzzleObj6.clear_values()

    # Test Input 7 - Grid has missing letters
    test7_input_path = "test\\test7.pzl"
    puzzleObj7 = Puzzle(test7_input_path)
    puzzleObj7.clear_values()

    unittest.main()