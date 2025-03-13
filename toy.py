position_x = 0  
position_y = 0 
direction = "forward"  

MAX_X = 500
MAX_Y = 700
MIN_X = 0
MIN_Y = 0

def is_within_bounds(new_x, new_y):
    """Checks if the new position is within allowed boundaries."""
    return MIN_X <= new_x <= MAX_X and MIN_Y <= new_y <= MAX_Y

def move_robot(command, steps):
    """Moves the robot in the given direction while enforcing boundary constraints."""
    global position_x, position_y, direction
    
    movement = {
        "forward": (0, steps),
        "back": (0, -steps),
        "right": (steps, 0),
        "left": (-steps, 0),
    }

    if command in movement:
        new_x = position_x + movement[command][0]
        new_y = position_y + movement[command][1]

        if is_within_bounds(new_x, new_y):
            position_x, position_y = new_x, new_y
            direction = command
            print(f"Robot moved {steps} steps {command}. Current position: ({position_x}, {position_y})")
        else:
            print(f"Cannot move {command}. Movement would exceed boundaries: X({MIN_X}-{MAX_X}), Y({MIN_Y}-{MAX_Y}).")
    else:
        print("Invalid command! Please enter 'forward', 'back', 'right', or 'left'.")
