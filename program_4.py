# Programmer: Mai Lillie
# Date: 10/18/24
# Program #4: Coordinates
import math

# Gets two coordinates from the user and finds the distance between
def main():
    coordinate_a = int(input("What is the first number of your first coordinate?: "))
    coordinate_b = int(input("What is the second number of your first coordinate?: "))
    coordinate_c = int(input("What is the third number of your first coordinate?: "))
    coordinate_d = int(input("What is the first number of your second coordinate?: "))
    coordinate_e = int(input("What is the second number of your coordinate?: "))
    coordinate_f = int(input("What is the third number of your coordinate?: "))
    coordinate1 = (coordinate_a, coordinate_b, coordinate_c)
    coordinate2 = (coordinate_d, coordinate_e, coordinate_f)
    final = distance (coordinate1, coordinate2)
    print(f"The distance is: {final:.2f}.")

# Function to find the actual distance between coordinates
def distance(input1, input2):
    x = ((input1[0]-input2[0])**2) + ((input1[1]-input2[1])**2) + ((input1[2]-input2[2])**2)
    total = math.sqrt(x)
    return total

# Call the main function.
if __name__ == '__main__':
    main()
