
position_x = 0  
position_y = 0 
direction = "forward"  


MAX_X = 500
MAX_Y = 700
MIN_X = 0
MIN_Y = 0


def move_robot(command, steps):
    global position_x, position_y, direction

    if command == "forward":
        if position_y + steps <= MAX_Y:
            position_y += steps
            direction = "forward"
            print(f"Robot moved {steps} steps forward. Current position: ({position_x}, {position_y})")
        else:
            print(f"Cannot move forward. Y position exceeds the limit of {MAX_Y}.")
    elif command == "back":
        if position_y - steps >= MIN_Y:
            position_y -= steps
            direction = "back"
            print(f"Robot moved {steps} steps backward. Current position: ({position_x}, {position_y})")
        else:
            print(f"Cannot move backward. Y position is at the minimum limit of {MIN_Y}.")
    elif command == "right":
        if position_x + steps <= MAX_X:
            position_x += steps
            direction = "right"
            print(f"Robot moved {steps} steps right. Current position: ({position_x}, {position_y})")
        else:
            print(f"Cannot move right. X position exceeds the limit of {MAX_X}.")
    elif command == "left":
        if position_x - steps >= MIN_X:
            position_x -= steps
            direction = "left"
            print(f"Robot moved {steps} steps left. Current position: ({position_x}, {position_y})")
        else:
            print(f"Cannot move left. X position is at the minimum limit of {MIN_X}.")
    else:
        print("Please enter a valid command!")

