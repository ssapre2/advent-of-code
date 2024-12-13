import numpy as np
from datetime import datetime


# Setup class to keep track progress, important attributes of word search

class TextGrid:

    # Pass text file to search when initialized
    def __init__(self,input_file):

        # Count overall number of "XMAS"'s found
        self.xmas_count = 0

        # Initialize list of current letters in word
        self.current_word =  list()
        
        with open(input_file,"r") as text_file:
            # read text file into list of strings
            self.text = text_file.readlines()

        # Create a matrix out of the text file outputs. We want to traverse this grid
        self.create_grid()

        # Initialize 
        # Keeps track of current letter
        self.current_letter = self.text_grid[1,1]
        # Indices
        self.row = 0
        self.col = 0
        # Position of important pivot letter
        self.x_positions = list()
        self.x = 0 
        self.y = 0
        self.list_A = {}
        

    # Create function to create a grid of the 
    def create_grid(self):

        # Number of elements
        n_rows = len(self.text)

        # remove newline 
        n_letters = len(self.text[1].rstrip())
        # Turn into list

        # Split each line into list of elements, remove newline character
        split_text = list(map(lambda x: list(x.rstrip()) ,self.text))

        self.text_grid = np.array(split_text)

        # list to track all words created
        self.word_list = list()




    # Define movable directions    
    def find_possible_directions(self,poss_x,poss_y):
        # These are the directions to be moved in
        self.possible_directions = [(x,y) for x in poss_x for y in poss_y]
        

    def find_next_

    
    # Now let's traverse this grid in search of the pivot or starting point and target word
    def find_pivot_letter(self,pivot,target_word):




        # Loop thru grid to find X's
        while self.row < self.text_grid.shape[0] and self.col < self.text_grid.shape[1]:
            self.current_letter = self.text_grid[self.row,self.col]

            if self.current_letter == pivot:
                # Store pivot Positions
                self.x_positions.append((self.row,self.col))

             # if it's the end of the row, move down 1 row and reset column index
            if self.col >= self.text_grid.shape[1]-1:
                self.row += 1
                self.col = 0           
                self.current_word.clear()

            else:
                self.col += 1
                self.current_word.clear()

        print("Finished Traversal")

    def find_next_s(self):
        pass
         

    def find_xmas(self,x_coord,y_coord,x_dir, y_dir,target):

        # Update function to find A counts
        

        # If we get to 'XMAS' return word
        if  self.current_word == target:
            # Add to word list
            self.word_list.append(self.current_word)

            self.xmas_count += 1

            self.current_word.clear()
            #return(self.current_word)
            if self.a_coords in self.list_A:
                self.list_A[self.a_coords] += 1
            else:
                self.list_A[self.a_coords] = 1
                self.current_word.clear()
                # Clear 'A' tracker
                self.current_a = None
        # Check that we're on the way the to target 'XMAS' or 'MMASS'
        elif (x_coord < 0 or y_coord < 0):
            assert("index out of bounds on grid")
            self.current_word.clear()
            self.current_a = None

        elif self.current_word != target[:len(self.current_word)]: 

            # Clear word list tracker
            self.current_word.clear()
            self.current_a = None

        else:
            # Increment coords in specified direction
            x = x_coord + x_dir
            y = y_coord + y_dir
            try:
                # Grab current letter on grid
                current_letter = self.text_grid[x_coord,y_coord]
                
                # Add X to word list
                self.current_word.append(current_letter)

                # If A is the current letter find it's coordinate points
                if current_letter == "A":
                    self.current_a = current_letter
                    a_coords = (x_coord+1,y_coord + 1)
                    self.a_coords = a_coords
                
                # Recursively find next words
                self.find_xmas(x_coord=x,y_coord = y,x_dir= x_dir,y_dir = y_dir,target = target)


            except Exception as e:

                self.current_word.clear()
                self.current_a = None





def main():
    # Problem 1
    start = datetime.now()
    obj1 = TextGrid('input1.txt')
    obj1.find_pivot_letter('X',target_word=['X','M','A','S'])
    obj1.find_possible_directions(range(-1,2,1),range(-1,2,1))
    
    # Apply 'find_word' function to list
    trials = [obj1.find_xmas(x_coord = letter_coords[0], y_coord= letter_coords[1],x_dir=  direction[0],y_dir = direction[1],target = ['X','M','A','S']) for direction in obj1.possible_directions for letter_coords in obj1.x_positions]
    end = datetime.now()
    print(f"Part 1 Answer: {obj1.xmas_count} - {end - start} seconds")

    # Problem 2
    start = datetime.now()
    obj2 = TextGrid('input1.txt')
    obj2.find_pivot_letter('S',target_word=['S','A','M'])
     # Apply 'find_word' function to list
    obj2.find_possible_directions((-1,1),(-1,1))
    trials = [obj2.find_xmas(x_coord = letter_coords[0], y_coord= letter_coords[1],x_dir=  direction[0],y_dir = direction[1],target = ['S','A','M']) for direction in obj2.possible_directions for letter_coords in obj2.x_positions]
    # Get Elements of dictionary that have > 1 'A' aka get number of 'A's overlapped when searching for 'SAM'
    overlapping_a = {k: v for k, v in obj2.list_A.items() if v > 1}
    end =  datetime.now()
    print(f"Part 1 Answer: {len(overlapping_a)} - {end - start} seconds")



if __name__ == "__main__":
    main()