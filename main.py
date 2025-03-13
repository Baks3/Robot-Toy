import toy

def get_steps():
    """Gets the number of steps from the user and validates input."""
    while True:
        try:
            steps = int(input("Enter number of steps: "))
            if steps > 0:
                return steps
            print("Please enter a positive number of steps.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def handle_movement(command):
    """Handles robot movement based on user input."""
    steps = get_steps() if command in ["forward", "back"] else 0
    toy.move_robot(command, steps)

def main():
    """Main loop for robot control."""
    while True:
        command = input("Enter command (forward, back, right, left, or exit to quit): ").strip().lower()

        if command == "exit":
            print("Exiting the robot control program.")
            break

        if command in ["forward", "back", "right", "left"]:
            handle_movement(command)
        else:
            print("Invalid command! Please enter 'forward', 'back', 'right', or 'left'.")

if __name__ == "__main__":
    main()
