import toy

def main():
    while True:
        command = input("Enter command (forward, back, right, left, or exit to quit): ").strip().lower()

        if command == "exit":
            print("Exiting the robot control program.")
            break

        if command in ["forward", "back"]:
            while True:
                try:
                    steps = int(input(f"Enter steps to move {command}: "))
                    if steps > 0:
                        break 
                    else:
                        print("Please enter a positive number of steps.")
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
            
            toy.move_robot(command, steps)
        elif command in ["right", "left"]:
            
            toy.move_robot(command, 0)
        else:
            print("Please enter a valid command!")

if __name__ == "__main__":
    main()