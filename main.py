import toy

def get_steps(command):
    while True:
        try:
            steps = int(input(f"Enter steps to move {command}: "))
            if steps > 0:
                return steps
            else:
                print("Please enter a positive number of steps.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def handle_movement(command):
    if command in ["forward", "back"]:
        steps = get_steps(command)
        toy.move_robot(command, steps)
    elif command in ["right", "left"]:
        toy.move_robot(command, 0)
    else:
        print("Please enter a valid command!")

def main():
    while True:
        command = input("Enter command (forward, back, right, left, or exit to quit): ").strip().lower()

        if command == "exit":
            print("Exiting the robot control program.")
            break

        handle_movement(command)

if __name__ == "__main__":
    main()
