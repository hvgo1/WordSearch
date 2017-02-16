class Puzzle(object):
    def __init__(self, fileName, grid = [], words = [], answer = []):
        self.fileName = fileName
        self.grid = grid
        self.words = words
        self.answer = answer

    def set_puzzle(self, fileName):
        ''' Creates a 2-dimensional grid of the search puzzle
         and a list of words to find in the puzzle

        :param fileName: input file in .pzl
        '''
        file = open(fileName, 'r')

        # Extract 2D grid from the file
        for line in file:
            if line == '\n':
                break
            self.grid.append(list(line.upper().strip('\n')))
        # Check if grid is present
        if not self.grid:
            return False, "ERROR! Missing grid."

        rowCount = 1
        for row in self.grid:
            # Check if grid has equal dimensions
            if not len(row) == len(self.grid):
                return False, "ERROR! Grid has unequal dimensions."
            #Check if grid has spaces or missing letters
            rowStr = ''.join(row).strip(' ').replace(' ', '')

            if not len(rowStr) == len(self.grid):
                return False, "ERROR! Grid has missing letter/s at row {}.".format(
                    rowCount)
            rowCount += 1

        # Extract words from the file
        for line in file:
            self.words.append(list(line.replace(" ", "").upper().strip('\n')))
        # Close file to free up system resources
        file.close()
        #Check if the input contains a list of words
        if not self.words:
            return False, "ERROR! Missing list of words."

        return True, ""

    def get_file_name(self):
        ''' Returns the file name without the file extension

        :return fileName:
        '''
        fileName = self.fileName.split(".")[0]
        return fileName

    def print_puzzle(self):
        ''' Prints the word search puzzle in the terminal

        :return:
        '''
        for x in range(len(self.grid)):
            print ''
            for y in range(len(self.grid)):
                print self.grid[x][y],
        print'\n'

    def clear_values(self):
        ''' Clears the values of the lists for multiple instantiation
        of Puzzle class

        :return:
        '''
        self.grid = []
        self.words = []
        self.answer = []

class Word(object):
    def __init__(self, name, startCoord = (-1, -1), endCoord = (-1, -1)):
        self.name = name
        self.startCoord = startCoord
        self.endCoord = endCoord

    def getStartCoord(self):
        ''' Returns the starting coordinates of the word wherein
        the location of the top left corner to be at (1,1)

        :return startCoord:
        '''
        xCoord = self.startCoord[0] + 1
        yCoord = self.startCoord[1] + 1
        startCoord = (xCoord, yCoord)
        return startCoord

    def getEndCoord(self):
        ''' Returns the end coordinates of the word wherein the
        location of the top left corner to be at (1,1)

        :return endCoord:
        '''
        xCoord = self.endCoord[0] + 1
        yCoord = self.endCoord[1] + 1
        endCoord = (xCoord, yCoord)
        return endCoord

class WordSearch (object):
    def main(self, fileName):
        ''' This is where it all starts and ends.
        Calls different methods to process the given input, then searches
        for the given words in a 2-dimensional matrix. The results are
        written to an output file (*.out)

        :param fileName:
        :return:
        '''
        print "Word Searching..."
        # Create an instance of the puzzle
        puzzleObj = Puzzle(fileName)
        puzzleObj.clear_values()

        # @Step 1: Create grid and get words from input file
        isPuzzleValid, resultsText = puzzleObj.set_puzzle(fileName)

        if isPuzzleValid:
            # @Step 2: Find words in the puzzle
            self.__search_puzzle(puzzleObj)

        # @Step 3: Write answers to an output file
        print resultsText
        self.create_output_file(resultsText,puzzleObj)

        print "Done!"

    def __search_puzzle(self, puzzleObj):
        ''' Finds each word from the list in the puzzle's 2-dimensional
        grid

        :param puzzleObj:
        :return:
        '''
        isWordFound = False

        for word in puzzleObj.words:
            wordObj = Word(word)

            isWordFound = self.__find_word(puzzleObj.grid, wordObj)

            if isWordFound:
                print "{} {} {}".format(''.join(word), \
                                        wordObj.getStartCoord(), \
                                        wordObj.getEndCoord())
            else:
                print "{} not found".format(''.join(word))
            answer = [wordObj.getStartCoord(), wordObj.getEndCoord()]
            puzzleObj.answer.append(answer)

    def __find_word(self, grid, wordObj):
        ''' Find the specific word in the grid

        :param grid:
        :param wordObj:
        :return:
        '''
        gridLen = len(grid)
        startLetter = wordObj.name[0]
        isWordFound = False
        direction = {1:"ACROSS", 2:"BACKWARDS", 3:"DOWN", 4:"UP"}

        for yCoord in range(gridLen):
            for xCoord in range(gridLen):
                if startLetter == grid[yCoord][xCoord]:
                    wordObj.startCoord = (xCoord, yCoord)
                    for directionKey in direction:
                        isWordFound = self.__find_word_in_direction(
                            grid, wordObj, direction[directionKey])
                        if isWordFound:
                            break
                if isWordFound:
                    return True
        return False

    def __find_word_in_direction(self, grid, wordObj, direction):
        ''' Looks for the word depending on the direction

        :param grid:
        :param wordObj:
        :param direction: can be either of the following
                            ACROSS, BACKWARDS, DOWN, or UP
        :return:
        '''
        wordLen = len(wordObj.name)
        gridLen = len(grid)

        # Reset starting coordinates in every change of direction
        xCoord = wordObj.startCoord[0]
        yCoord = wordObj.startCoord[1]
        xCoordEnd = xCoord
        yCoordEnd = yCoord

        # Get the coordinates of the last letter in a specific direction
        if direction == "ACROSS":
            xCoordEnd = xCoord + (wordLen - 1)
        elif direction == "BACKWARDS":
            xCoordEnd = xCoord - (wordLen - 1)
        elif direction == "DOWN":
            yCoordEnd = yCoord + (wordLen - 1)
        elif direction == "UP":
            yCoordEnd = yCoord - (wordLen - 1)

        if xCoordEnd < 0 or xCoordEnd > gridLen - 1 or \
                        yCoordEnd < 0 or yCoordEnd > gridLen - 1:
            # Check that browsing through the grid in a specific
            #  direction will not cause an out-of-bound error
            return False
        elif not (grid[yCoordEnd][xCoordEnd] == wordObj.name[-1]):
            # Check if the last letter of the word is the same the
            # as the computed end coordinates
            return False
        else:
            # Find the word in the specific direction
            for wordPtr in range(1, wordLen - 1):
                if direction == "ACROSS":
                    xCoord += 1
                elif direction == "BACKWARDS":
                    xCoord -= 1
                elif direction == "DOWN":
                    yCoord += 1
                elif direction == "UP":
                    yCoord -= 1

                if wordObj.name[wordPtr] == grid[yCoord][xCoord]:
                    # Check if pointer is at the second to the last letter of the word
                    if wordPtr == wordLen - 2:
                        wordObj.endCoord = (xCoordEnd, yCoordEnd)
                        return True
                else:
                    return False

    def create_output_file(self, resultsText, puzzleObj):
        ''' Writes the results of the word search to a file

        :param resultsText:
        :param puzzleObj:
        :return:
        '''
        # Create new file with write capability
        fileName = puzzleObj.get_file_name() + ".out"
        file = open(fileName, "w")

        if not resultsText:
            for i in range(len(puzzleObj.words)):
                startCoord = puzzleObj.answer[i][0]
                endCoord = puzzleObj.answer[i][1]
                # Check if word is found
                if startCoord == (0,0) or endCoord == (0,0):
                    line = "{} not found".format(''.join(puzzleObj.words[i]))
                else:
                    line = "{} {} {}".format(''.join(puzzleObj.words[i]),
                                             startCoord, endCoord)
                # Write output to file
                file.write(line + "\n")

        file.write(resultsText)
        file.close()

if __name__ == "__main__":
    import sys
    WordSearch().main(sys.argv[1])
