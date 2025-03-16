🤖 Robot Movement Simulator
A simple text-based Robot Movement Simulator that allows users to control a robot within defined boundaries using intuitive commands.

🚀 Features
Move the robot forward, back, left, and right.

Prevents the robot from moving outside the defined boundary:

X-axis: 0 to 500

Y-axis: 0 to 700

Validates input to ensure positive step values only.

Handles invalid inputs gracefully with helpful messages.

📦 Installation & Setup
Clone the Repository
git clone git@github.com:Baks3/Robot-Toy.git
cd Robot-Toy

Run the Program
python main.py

🕹 How to Use
Available Commands
Command	Description
forward	Move the robot up along the Y-axis
back	Move the robot down along the Y-axis
right	Move the robot right along the X-axis
left	Move the robot left along the X-axis
exit	Quit the program

Example Session
Enter command (forward, back, right, left, or exit to quit): forward
Enter number of steps: 50
Robot moved 50 steps forward. Current position: (0, 50)

Enter command (forward, back, right, left, or exit to quit): right
Enter number of steps: 100
Robot moved 100 steps right. Current position: (100, 50)

Enter command: exit
Exiting the robot control program.
🗂 Code Structure
Robot-Toy/
│── main.py         # Handles user input and command processing
│── toy.py          # Contains movement logic and boundary checks
│── README.md       # Project documentation
🧠 Code Overview
main.py
Prompts the user for commands and step input.

Validates inputs and calls movement functions.

Handles program exit cleanly.

toy.py
Defines boundaries: 0 ≤ X ≤ 500, 0 ≤ Y ≤ 700.

Contains the logic to move the robot while ensuring it stays within bounds.

Uses a direction mapping for clean movement calculations.

🔮 Future Enhancements
🛠 Undo Functionality – Revert the last move.

💾 Save & Load Position – Persist robot's position between sessions.

🖥 Graphical Interface (GUI) – Interactive interface for robot control.

🤝 Contributing
Contributions are welcome! Feel free to fork the repo, create a feature branch, and submit a pull request with your improvements. 🚀