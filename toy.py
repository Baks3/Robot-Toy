while True:
    command = input("Enter command (forward, back, right, left): ").strip().lower()

    if command == "forward":
        steps = int(input("Enter steps to move forward: "))
        print(f"Robot moved {steps} steps forward")
    elif command == "back":
        steps = int(input("Enter steps to move backward: "))
        print(f"Robot moved {steps} steps backward")
    elif command == "right" or command == "left":
        print(f"Robot turned {command}")
    else:
        print("Please a valid command!")
    
