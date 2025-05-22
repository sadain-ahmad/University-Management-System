# 🎓 University Management System

A terminal-based University Management System built with **Python** and **MySQL** that helps manage students, teachers, courses, departments, and attendance, with **login-based access for students and teachers**.

## 🚀 Features

- 🔐 **Login system**
  - Students and teachers have their own accounts to securely access and manage their data
- Add, update, delete, and view:
  - Students
  - Teachers
  - Courses
  - Departments
- Assign courses to teachers
- Register students for courses
- View enrolled students in a course
- ✅ **Mark attendance** of a student in a specific subject
- 👁️ Students can:
  - View registered courses
  - Check their attendance
- 👨‍🏫 Teachers can:
  - View assigned courses
  - Mark student attendance

## 🛠️ Technologies Used

- **Python** – Core logic and CLI-based UI
- **MySQL** – Backend database for persistent storage
- **MySQL Connector for Python** – To interact with the database
- **Hashlib** – For password hashing (optional for login security)

## 📂 Project Structure

university management System/
│
├── main.py # Entry point and menu navigation
├── db_con.py # Database connection settings
├── account.py # Login and authentication logic
├── person.py # Person(Student and teacher)-specific operations
├── university.py # uni-specifin operation
├── course.py # Course-related operations
├── department.py # Department-related operations
├── attendance.py # Attendance marking/viewing
└── registration.py # registration of students


## 🧑‍💻 How to Run

1. **Clone the repository**
```bash
git clone https://github.com/sadain-ahmad/university-management-system.git
cd Uni Management System
```

2. Set up the MySQL database

- Open MySQL shell or GUI like phpMyAdmin

3. Configure the database

- Open `db_con.py`

- Set your database credentials

4. Install dependencies

```bash
pip install mysql-connector-python
```

5. Run the system

```bash
python main.py
```

## 🤝 Contributing
Feel free to fork the project and open pull requests. For major changes, please open an issue first to discuss what you want to change.