🏦 Banking Management System (Python)
A modular Banking Management System built using Python, following clean architecture principles (separation of concerns), Object-Oriented Programming (OOP), file handling, and basic data analytics.
________________________________________
🚀 Features
•	Create a new bank account
•	Deposit & withdraw money
•	View account details
•	Delete account
•	Secure login using Account Number & PIN
•	Persistent data storage using JSON
•	CLI-based interactive menu system
•	Basic data analytics:
o	Total users
o	Total balance
o	Average balance
o	Highest & lowest balance
________________________________________
🧠 Architecture
main.py           → CLI (User Interface)
services/         → Business Logic
models/           → Data Structure (Account)
utils/            → Helper Functions
data/             → JSON Database
________________________________________
📂 Project Structure
banking-system/
│
├── data/
│   └── database.json
│
├── models/
│   └── account.py
│
├── services/
│   └── bank_service.py
│
├── utils/
│   └── helpers.py
│
├── main.py
└── README.md
________________________________________
⚙️ Setup & Installation
1. Clone Repository https://github.com/ghanshyamverma4654/Banking-Management-System
git clone 
2. Ensure JSON File Exists
Create file:
data/database.json
Add this inside:
[]
________________________________________
3. Run the Project
python main.py
________________________________________
🖥️ Usage (CLI Menu)
===== Banking System =====
1. Create Account
2. Deposit
3. Withdraw
4. View Account
5. Delete Account
6. Show Statistics
7. Exit	
________________________________________
📊 Example Output
Account created successfully!
Account No: AbC12345

Deposit successful!
Updated Balance: 5000

Statistics:
Total Users: 1
Average Balance: 5000
________________________________________
🛠️ Tech Stack
•	Python
•	JSON (File Handling)
•	OOP (Object-Oriented Programming)
•	CLI (Command Line Interface)
________________________________________
🔐 Key Concepts Implemented
•	Object-Oriented Design
•	File Handling (JSON persistence)
•	Modular Programming
•	Input Validation & Error Handling
•	Data Processing & Basic Analytics
________________________________________
📈 Future Improvements
•	Web version using Flask / Django
•	Database integration (MySQL / PostgreSQL)
•	Transaction history tracking
•	User authentication (hashed PINs)
•	GUI interface (Tkinter / React frontend)
________________________________________
👨‍💻 Author
Ghanshyam Verma
Aspiring Data Scientist | Python | Data Analysis | Machine Learning
________________________________________
⭐ If you like this project
Give it a ⭐ on GitHub and share feedback!



