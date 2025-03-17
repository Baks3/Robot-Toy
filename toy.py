# toy.py

position_x = 0
position_y = 0
UNDO_LIMIT = 5  # Limit the number of undos
position_history = []  # Stack for tracking move history (limited to UNDO_LIMIT) # Stack for tracking move history

MAX_X = 500
MAX_Y = 700
MIN_X = 0
MIN_Y = 0

DIRECTION_MAP = {
    "forward": (0, 1),
    "back": (0, -1),
    "right": (1, 0),
    "left": (-1, 0)
}

def is_within_bounds(new_x, new_y):
    """Checks if the new position is within the allowed boundaries."""
    return MIN_X <= new_x <= MAX_X and MIN_Y <= new_y <= MAX_Y

def move_robot(command, steps=0):
    """Moves the robot based on the command and ensures it stays within bounds."""
    global position_x, position_y

    if command in DIRECTION_MAP:
        dx, dy = DIRECTION_MAP[command]
        new_x = position_x + dx * steps
        new_y = position_y + dy * steps

        if is_within_bounds(new_x, new_y):
            position_history.append((position_x, position_y))
            # Enforce UNDO_LIMIT
            if len(position_history) > UNDO_LIMIT:
                position_history.pop(0)  # Remove the oldest entry

            position_x, position_y = new_x, new_y
            print(f"Robot moved {steps} steps {command}. Current position: ({position_x}, {position_y})")
        else:
            print(f"Cannot move {command}. Movement would exceed boundaries: X({MIN_X}-{MAX_X}), Y({MIN_Y}-{MAX_Y}).")
    else:
        print("Invalid command! Please enter 'forward', 'back', 'right', or 'left'.")

def undo_move():
    """Reverts the robot's last move."""
    global position_x, position_y

    if position_history:
        position_x, position_y = position_history.pop()
        print(f"Undo successful. Current position: ({position_x}, {position_y})")
    else:
        print("No moves to undo.")
