import numpy as np

# Setup class to keep track progress, important attributes of word search

class TextGrid:

    # Pass text file to search when initialized
    def __init__(self,input_file):

        # Count overall number of "XMAS"'s found
        self.xmas_count = 0
        self.target = ['X','M','A','S']

        # Keep track of the which "X" we are on
        current_row = 1

        current_column = 1


        # Keep track of which x,y coords you're searching for
        self.search_position = 0

        # Keep track of number of letters in word so far
        self.letter_count = 0

        # Initialize list of current letters in word
        self.word_list = list()
        
        with open(input_file,"r") as text_file:
            # read text file into list of strings
            self.text = text_file.readlines()

        # Create a matrix out of the text file outputs. We want to traverse this grid
        self.create_grid()

        self.current_letter = self.text_grid[1,1]
        self.row = 0
        self.col = 0
        self.x_positions = list()
        self.x = 0 
        self.y = 0
        

    # Create function to create a grid of the 
    def create_grid(self):

        # Number of elements
        n_rows = len(self.text)
        print(f"Number of Rows {n_rows}")

        # remove newline 
        n_letters = len(self.text[1].rstrip())
        # Turn into list
        print(f"Number of letters {n_letters}")

        # Split each line into list of elements, remove newline character
        split_text = list(map(lambda x: list(x.rstrip()) ,self.text))

        self.text_grid = np.array(split_text)
        
        print(f"Matrix Dimension = {self.text_grid.shape}")
        #print(self.text_grid)

    
    # Now let's traverse this grid in search of the 'X', our starting point
    def find_next_x(self):

        possible_x = range(-1,2,1)
        possible_y = range(-1,2,1)

        # Loop thru grid to find X's
        while self.row < self.text_grid.shape[0] and self.col < self.text_grid.shape[1]:
            self.current_letter = self.text_grid[self.row,self.col]
            #print(f"{self.current_letter} - ({self.row},{self.col})")

            if self.current_letter == 'X':
                print(f"X at ({self.row+1},{self.col+1})")
                self.x_positions.append((self.row,self.col))
                # Add X to word list
                self.word_list.append('X')
                self.letter_count+=1
                # Try all direction combinations
                possible_directions = [(x,y) for x in possible_x for y in possible_y]
                # Apply 'find_word' function to list
                xmas_finds = [self.find_word(x = self.row, y= self.col,x_dir=  direction[0],y_dir = direction[1]) for direction in possible_directions]
            
                # Add to count 
                self.xmas_count += len(xmas_finds)
            # if it's the end of the row, move down 1 row and reset column index
            if self.col >= self.text_grid.shape[1]-1:
                self.row += 1
                self.col = 0           
                self.word_list.clear()
                self.letter_count = 0

            else:
                self.col += 1
                self.word_list.clear()
                self.letter_count = 0

    
         

    def find_word(self,x,y,x_dir, y_dir):
        print(f"Direction ({x_dir},{y_dir})")

        # If target hits
        if  self.word_list == self.target:
            print(self.word_list)
            return(self.word_list)
        # Check that we're on the way the 'XMAS'
        elif self.word_list != self.target[len(self.word_list):]: 
            # Clear word list tracker
            print(f"Not on track w/ {self.word_list}")

        else:
            x += x_dir
            y += y_dir
            try:
                next_letter = self.text_grid[x,y]
                print(f"Next Letter {next_letter}")
                self.letter_count += 1
                print(self.letter_count)
                # Add letter to word count
                self.word_list.append(next_letter)
                # Recurse
                self.find_word(x,y,x_dir,y_dir)
            except Exception as E:
                print(f"Index ({x,y}) Not in test grid")




        

        

            
        



def main():
# Main body of code. Other functions and class methods are called from main.
    obj = TextGrid('sample_text.txt')
    obj.find_next_x()
    print(obj.xmas_count)

    #obj.find_word(x = obj.x_positions[0][0],y = obj.x_positions[0][1],x_dir=-1,y_dir=0)

if __name__ == "__main__":
    main()