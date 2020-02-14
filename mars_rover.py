
import sys


input_instruc = sys.stdin.read().splitlines()                                               #Each line in the instructions.txt file will be an item in a list

compass_dir = ['N','E','S','W']
compass_coor = {'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}

number_of_rovers = 2


def data_input(n):

    start_point = ()                                                                     #Rover 1 starting coordinate
    instructions = ''
                         
    start_read = tuple(input_instruc[1+(2*n)].split())                                        #Convert the second input line into a tuple coordinate, and intial direction
    start_point = (int(start_read[0]),int(start_read[1]),start_read[2])      #Convert the coordinates from strings to integers 
    instructions = input_instruc[1+(2*n)+1]                                                         #Rover 1 directional input

    return instructions, start_point


def move_rover(instructions, starting_point):

    final_coor = (starting_point[0],starting_point[1])
    current_dir_index = compass_dir.index(starting_point[2])                             #The index position of the starting direction
    move_order = (0,0)
    new_dir_index = 0
    current_dir = ''

    for i in instructions:

        if i == 'L':
            if current_dir_index == 0:
                current_dir_index = len(compass_dir) - 1
            else:
                current_dir_index = current_dir_index - 1

        elif i == 'R':
            if current_dir_index == len(compass_dir) - 1:
                current_dir_index = 0           
            else:
                current_dir_index = current_dir_index + 1
        
        elif i == 'M':
            current_dir = compass_dir[current_dir_index]                                         #The new compass heading
            move_order = compass_coor[current_dir]                                               #Coordinate move order  
            final_coor = (final_coor[0] + move_order[0], final_coor[1] + move_order[1])

        else:
            print("Not a valid input (valid inputs: [L,R,M]") 

    return final_coor, current_dir, starting_point


def check_plat_size(final_coor, current_dir, starting_point):

    plat_dim = tuple(map(int,input_instruc[0].split()))                                           #Convert the first input line into a tuple coordinate
    x_max = plat_dim[0]
    y_max = plat_dim[1]

    if (0 <= (final_coor[0]) <= x_max) and (0 <= (final_coor[1]) <= y_max):
        return print(f"{final_coor[0]} {final_coor[1]} {current_dir}")
    else:
        print("This move will take the rover outside of the plateau, please provide another move order")
        final_coor = starting_point[0],starting_point[1]


def main():
   
    for i in range (number_of_rovers):       # Run the rovers sequentially

        instructions, start_point = data_input(i)
        final_coor, current_dir, starting_point = move_rover(instructions,start_point)
        check_plat_size(final_coor, current_dir, starting_point)


if __name__ == "__main__":
    main()