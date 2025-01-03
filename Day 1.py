import pandas as np
import numpy as np

def sort():
    pass


def main():

    sim_dict = dict()
    with open("input_day1.txt", "r") as file:
        #lines = file.readlines()  # Returns a list of lines
        left = []
        right = []
        for line in file:
        # Split each line into two parts
            col1, col2 = line.split()
            left.append(int(col1))                
            right.append(int(col2))
            left.sort()
            right.sort()
    diffs = [abs(left[i] - right[i]) for i in range(0,len(left))]
    sims = [left[i] * len(list(filter(lambda x: x  == left[i], right))) for i in range(0,len(left))]
    diffs.sort()

    

    print(sum(diffs))
    print(f"Similarity Score: {sum(sims)}")


if __name__ == "__main__":
    main()
