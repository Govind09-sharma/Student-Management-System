Student Management System

1. Project Overview

The Student Management System is a web-based application developed to manage student records efficiently. It provides a simple and user-friendly interface for adding, viewing, searching, updating, and deleting student information.

2. Objectives

- To maintain student records digitally.
- To reduce manual record-keeping.
- To make student information easy to search and update.
- To provide a simple dashboard for managing student data.

3. Technologies Used

- Frontend: HTML, CSS
- Backend: Python, Flask
- Database: SQLite
- Development Environment: Visual Studio Code

4. Main Features

1. Dashboard displaying student statistics.
2. Add new student records.
3. View all registered students.
4. Search students by name or roll number.
5. Edit existing student information.
6. Delete student records with confirmation.
7. Store student information in an SQLite database.

5. Project Structure

student management system/
├── templates/
│   ├── index.html
│   ├── add_student.html
│   ├── edit_student.html
│   └── students.html
├── app.py
├── students.db
└── README.md

6. Database Information

The application uses SQLite to store student records. The database contains student information such as ID, name, roll number, email, and course.

7. How to Run the Project

1. Install Python on your computer.

2. Open the project folder in Visual Studio Code.

3. Activate the project's virtual environment if required.

4. Install Flask if it is not already installed:
   
   "python -m pip install flask"

5. Run the application:
   
   "python app.py"

6. Open your browser and visit:
   
   "http://127.0.0.1:5000/"

8. Conclusion

The Student Management System demonstrates how Python, Flask, HTML, CSS, and SQLite can be combined to develop a basic web application for managing student records. It provides essential student management operations through a simple interface.

9. Future Scope

- User authentication and administrator login.
- Export student records to Excel or PDF.
- Course-wise student reports.
- Improved data validation and security.