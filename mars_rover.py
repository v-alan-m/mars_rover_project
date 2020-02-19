
import sys


input_instruc = sys.stdin.read().splitlines()                                   # Read each line in the instructions.txt file

compass_dir = ['N','E','S','W']                                                 # The compass directions to navigate through
compass_coor = {'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}                      # The coordinate displacement if the heading is in this chosen direction

number_of_rovers = 2                                                            # Define the number of rover units to run sequentially


def data_input(n):                                                                 

    start_point = ()                                                                     
    instructions = ''
                         
    start_read = tuple(input_instruc[1+(2*n)].split())                           # The current coordinates and heading             
    start_point = (int(start_read[0]),int(start_read[1]),start_read[2])          # Convert the numbers into integers for the move_rover()
    instructions = input_instruc[1+(2*n)+1]                                      # The move orders          

    return instructions, start_point                                             # Will be passed into the move_rover() in main() 


def move_rover(instructions, starting_point):

    final_coor = (starting_point[0],starting_point[1])                           # Initialise
    current_dir_index = compass_dir.index(starting_point[2])                     # The starting compass heading is converted into an index position       
    move_order = (0,0)
    new_dir_index = 0
    current_dir = ''

    for i in instructions:                                                       # Iterate through the move order 

        if i == 'L':
            if current_dir_index == 0:
                current_dir_index = len(compass_dir) - 1                         # Move to the end of the list, if at the first index position
            else:
                current_dir_index = current_dir_index - 1

        elif i == 'R':
            if current_dir_index == len(compass_dir) - 1:
                current_dir_index = 0                                            # Move to the front of the list, if at the last index position
            else:
                current_dir_index = current_dir_index + 1
        
        elif i == 'M':
            current_dir = compass_dir[current_dir_index]                                         
            move_order = compass_coor[current_dir]                                                 
            final_coor = (final_coor[0] + move_order[0],                         # The resultant coordinate of all the move orders added together
                final_coor[1] + move_order[1])

        else:
            print("Not a valid input (valid inputs: [L,R,M]")                    # Will be passed into the check_plat_size() in main() 

    return final_coor, current_dir, starting_point                              


def check_plat_size(final_coor, current_dir, starting_point):

    plat_dim = tuple(map(int,input_instruc[0].split()))                                           
    x_max = plat_dim[0]
    y_max = plat_dim[1]

    if (0 <= (final_coor[0]) <= x_max) and (0 <= (final_coor[1]) <= y_max):                                  # Only return a location coordinate if the destination is in bounds
        return print(f"{final_coor[0]} {final_coor[1]} {current_dir}")
    else:
        print("This move will take the rover outside of the plateau, please provide another move order")     # If not in bounds lets the user try again
        final_coor = starting_point[0],starting_point[1]                                                     # If move is out of bounds, rover back to the starting position

def main():
   
    for i in range (number_of_rovers):       # Run the rovers sequentially

        instructions, start_point = data_input(i)                                                            # Read the starting position and move orders for the rover               
        final_coor, current_dir, starting_point = move_rover(instructions,start_point)                       # Generate a destination coordinate and heading
        check_plat_size(final_coor, current_dir, starting_point)                                             # Act on whether the final destination is within the defined bounds


if __name__ == "__main__":
    main()