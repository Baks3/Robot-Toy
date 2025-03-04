
position = 0  
direction = "forward"  


def move_robot(command, steps):
    global position, direction
    if command == "forward":
        position += steps
        direction = "forward"
        print(f"Robot moved {steps} steps forward. Current position: {position}")
    elif command == "back":
        position -= steps
        direction = "back"
        print(f"Robot moved {steps} steps backward. Current position: {position}")
    elif command == "right":
        direction = "right"
        print("Robot turned right.")
    elif command == "left":
        direction = "left"
        print("Robot turned left.")
    else:
        print("Please enter a valid command!")


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
        
        move_robot(command, steps)
    elif command in ["right", "left"]:
        move_robot(command, 0)  
    else:
        print("Please enter a valid command!")
