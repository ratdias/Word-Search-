import random
from random import randrange
import string
RIGHT = (1, 0)
DOWN = (0, 1)
RIGHT_DOWN = (1, 1)
RIGHT_UP = (1, -1)
DIRECTIONS = (RIGHT, DOWN, RIGHT_DOWN, RIGHT_UP)
grid = [
    ['p', 'c', 'n', 'd', 't', 'h', 'g'],
    ['w', 'a', 'x', 'o', 'a', 'x', 'f'],
    ['o', 't', 'w', 'g', 'd', 'r', 'k'],
    ['l', 'j', 'p', 'i', 'b', 'e', 't'],
    ['f', 'v', 'l', 't', 'o', 'w', 'n']
]

solution = {'cat': ((1, 0), (0, 1)),'dog': ((3, 0), (0, 1)),'art': ((4, 1), (1, 1)),'town': ((3, 4), (1, 0)),'den': ((4, 2), (1, 1)),'wolf': ((0, 1), (0, 1))}

def get_size(grid):
    #define the variables and return the tuple containing the height and length
    height = len(grid)
    width = len(grid[0])
    return (width, height)

def print_word_grid(grid):
    line = ""
    #iterate through the loop and print each line separately
    for i in grid:
        for letter in i:
            line += letter
        print(line)
        line = ""

def copy_word_grid(grid):
    copied_grid = grid.copy()
    temp_grid = []
    for i in copied_grid:
        copy_cat= i.copy()
        temp_grid.append(copy_cat)
        copy_cat = []
    return temp_grid

def extract(grid, position, direction, max_len):
    #initialize variables
    palavra = ''
    size = get_size(grid)
    (x, y) = position
    #iterate through the loop
    for i in range(0, max_len):
        #if x and y do not go out of bounds
        if 0 <= x < size[0] and 0 <= y < size[1]:
            #add the letter on the coordinates of the grid to the word
            palavra += grid[y][x]
            #apply the direction determined by the input to change the next coordinates
            y += direction[1]
            x += direction[0]
    return palavra

    #helper function to separate an string into a list of letters
def separate(word):
    separated_word = []
    #iterate through the word, and append every letter to the list
    for i in word:
        separated_word.append(i)
        #return list
    return separated_word

    #helper function to capitalize each letter found in the show solution function
def upper_grid(position, grid, direction, length):
    #initialize variables
    temp_grid = copy_word_grid(grid)
    (y, x) = position
    #iterate through the length of the input word of the show_solution function
    for i in range(length):
        #make each letter capitalized and change the coodinates accoding to the direction given by the dictionary of solutions
        temp_grid[x][y] = temp_grid[x][y].upper()
        x += direction[1]
        y += direction[0]
        #return the grid with capital letters
    return temp_grid
def show_solution(grid, word, solution):
    if solution == False:
        print(word, "is not found in this word search")
        return False
    #check if the word written as input is an element of the dictionary of solutions
    if extract(grid, solution[0],solution[1], len(separate(word))) == word:
        #print the capitalized word and use the helper function to print the capitalized grid
        print(word.upper(), "can be found as below")
        print_word_grid(upper_grid(solution[0], grid, solution[1],len(separate(word))))
    else:
        #if the word is not found, print the not found message and return the boolean false
        print(word, "is not found in this word search")
        return False

#helper function to test if the word can be found on every possible direction
def test_direction(grid, place, word, divided_word):
    #using the extract function, if the output is equal to the word, return the direction from which it was found
    if extract(grid, place, RIGHT, len(divided_word)) == word:
        return RIGHT
    elif extract(grid, place, DOWN, len(divided_word)) == word:
        return DOWN
    elif extract(grid, place, RIGHT_DOWN, len(divided_word)) == word:
        return RIGHT_DOWN
    elif extract(grid, place, RIGHT_UP, len(divided_word)) == word:
        return RIGHT_UP
    else:
        return

def find(grid, word):
    #create a list of all the letter in the word
    separated_word = separate(word)
    #iterate through the loop
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            #if the letter in a specific position of the grid is the same as the first letter of the word, save the position and use helper function to find the direction
            if grid[i][j] == separated_word[0]:
                position = (j, i)
                direction = test_direction(grid, (j, i), word, separated_word)
                #if the output of test_direction is different than None (meaning the correct position and direction were found), return the position and direction
                if direction != None:
                    return (position, direction)
                #if the loop hit the end of the grid and fails to find the word, return False
            elif i == len(grid) and j == len(i):
                return False
    return False

def find_all(grid, word_lst):
    #create dictionary of solutions
    sol_dict = {}
    #initialize every value with false and make the keys of the dictionary be the words to be found
    for i in word_lst:
        sol_dict[i] = False
    #if word is found by using the find function, associate the key with position and direction where the word was found (if the word is not found, the value will be False)
    for word in sol_dict:
        sol_dict[word] = find(grid, word)
        #return the dictionary
    return sol_dict

#helper function to write an empty grid
def write_grid(width, height):
    #initialize a grid and fill it with "" by iterating through the grid
    temp_grid = [["" for i in range(width)] for j in range(height)]
    return temp_grid
#helper function to write the words on the grid   
def write_words(grid, position, direction, word):
    #use get_size function to define the dimensions of the grid and initialize the variables
    (width, height) = get_size(grid)
    separated_word = separate(word)
    (y, x) = position
    #iterate over the length of the word to be written
    for i in range(len(word)):
        #if the position go over the border of the grid break the loop
        if x >= width or y >= height:
            break
        if x < 0 or y < 0:
            break
            #write each letter of the word at the correct posistion and change the coordinates by adding the direction for the next letter
        grid[y][x] = separated_word[i]
        x += direction[0]
        y += direction[1]
    return grid

#helper function based of the find all function (same first steps)
def find_all_boolean(grid, word_lst):
    truth_list = []
    sol_dict = {}
    for i in word_lst:
        sol_dict[i] = False
    for word in sol_dict:
        sol_dict[word] = find(grid, word)
    #use the values of the solution dictionary to check if the words can be found at the grid
    for value in list(sol_dict.values()):
        #since the grid might be empty, if the value is none also append true to the truth list
        if value == None or value != False:
            truth_list.append(True)
    #if all the elements of the truth list are true, return true else false
    for item in truth_list:
        if item == True:
            continue
        else:
            return False
    return True

#helper function to fill the empty space of the grid
def fill_grid(grid):
    #iterate through the loop
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            #if the value of the loop at a specific position is the '' character fill it with a random lower case letter
            if grid[i][j] == '':
                grid[i][j] = (random.choice(string.ascii_letters)).lower()
    #return grid
    return grid

#helper function to find the possible positions and direction
def possible_places(word, width, height):
    #initialize variables
    possible_places = []
    grid = write_grid(width, height)
    direction_lst = [RIGHT, DOWN, RIGHT_DOWN, RIGHT_UP]
    #test random positions and directions 100 times
    for i in range(100):
        position = (random.randint(0, height), random.randint(0, width))
        direction = random.choice(direction_lst)
        written_grid = write_words(grid, position, direction, word)
        #use the extract function to test if a position/direction is viable. If that is the case, append it to a list of possible places
        if len(extract(written_grid, position, direction, len(word))) == len(word):
            possible_places.append((position, direction))
            #choose a random index from zero to the length of the list and return the list at that index
    random_index = randrange(len(possible_places))
    return possible_places[random_index]


def generate(width, height, word_lst):
    #initilize variables
    true_word_lst = []
    grid2 = write_grid(width, height)
    grid = write_grid(width, height)
    #loop will iterate untill a grid and the words found on the grid return
    while True:
        #iterate through the word list
        for word in word_lst:
            #use to possible places function to set pos and dir to a random viable position and direction
            (pos, dir) = possible_places(word, width, height)
            #write the word at that position and direction on the grid
            write_words(grid, pos, dir, word)
            #if all the words are found and we are sure that the words are written, fill the empty spaces of the grid with trandom letters
        if find_all_boolean(grid, word_lst) == True and grid != grid2:
            grid = fill_grid(grid)
            #check what words were written
        for word in word_lst:
            #if the word was found, append the word to the true word list
            if find(grid, word) != None or find(grid, word) != False:
                true_word_lst.append(word)
            #return the grid and the words written on them
            return (grid)





