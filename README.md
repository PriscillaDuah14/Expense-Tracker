# Expense-Tracker
![A picture of an Expense Tracker software](images.jpg)




## Project Overview

The Expense Tracker is a backend application developed using Flask and MySQL. This project is designed to help users efficiently manage their personal finances by providing CRUD operations for income and expenses, categorization of expenses, and generating reports to monitor financial health.

While the project is backend-focused but includes a little bit of frontend, it exposes APIs that can be integrated with any frontend framework or mobile application.




## Features

The application includes the following functionalities:

Core Features

Add, View, Update, and Delete Income and Expense Records
Manage financial transactions seamlessly using CRUD operations.

Expense Categorization
Categorize expenses into predefined groups such as food, rent, entertainment, etc.

Monthly Summaries
Generate summaries of income, expenses, and remaining savings for a given month.

Reports
Display detailed comparisons of income vs. expenses.


## Advanced Features

Data Visualization Ready
The API provides endpoints to integrate with third-party tools for data visualization.

Authentication (Optional)
A basic authentication system can be implemented to protect user data.





## Technologies Used

Backend Framework: Flask

Database: MySQL

ORM: SQLAlchemy

Language: Python,Html,Javascript

Environment: Flask Development Server





## Installation

Follow the steps below to set up and run the project:

Prerequisites

Python 3.9 or higher

MySQL installed and running

pip for Python package management


## Setup Instructions

1. Clone the Repository

git clone https://github.com/username/Expense-Tracker.git
cd Expense-Tracker

2. Set up a Virtual Environment

python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows


3. Install Dependencies

pip install -r requirements.txt


4. Configure MySQL Database

Create a MySQL database named Expense-Tracker_db (or your preferred name).

Update the SQLALCHEMY_DATABASE_URI in app.py with your MySQL credentials:

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/expensetracker_db'



5. Initialize the Database
Run the following script to create database tables:

python
from app import db
db.create_all()
exit()


6. Run the Application

python app.py


7. Access the Application
Open your browser and navigate to http://127.0.0.1:5000.






## API Endpoints

Income

GET /income
Retrieve all income records.

POST /income
Add a new income record.


Expenses

GET /expenses
Retrieve all expense records.

POST /expenses
Add a new expense record.


Reports

GET /reports/monthly?month=<month>&year=<year>
Retrieve a monthly summary of income and expenses.





## Project Structure

Expense-Tracker/
│
├── app.py               # Main Flask application
├── models.py            # Database models
├── expenses_crud.py     # API route definitions
├── index.html           # Html dependencies
├── README.md            # Project documentation





## Future Enhancements

Implement a frontend using React or Angular for better user interaction.

Add user authentication and authorization for secure access.

Integrate with data visualization libraries to display graphical summaries.

Expand the reporting feature to include year-to-date summaries and savings goals.





## Contributors
- Priscilla Duah
[LinkedIn](http://linkedin.com/in/priscilla-antwiwaa-duah-7485b532a)

- Dorgbetor Catherena Emefa
[Github](https://github.com/dorgbetorcatherena) 

Feel free to reach out for questions or contributions.
