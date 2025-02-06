# test01_employee_api
 
This project is a sample **HR Employee Data REST API**, designed to mimic HR software

## Features
- Employee Data Registration and Updating

## Technologies Used
- Python, Flask (Backend)
- SQLite + SQLAlchemy (Database)
- Marshmallow (Data serialization)

## How to Run
1. Clone this repository: 
git clone https://github.com/USERNAME/test01_employee_api.git

2. Install dependencies: 
pip install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy

3. Start the API:
python app.py

4. Use **Postman** to test API requests.

## API Endpoints
- **GET** `/employees` – Retrieve employee list
- **POST** `/employees` – Add new employee
- **PUT** `/employees/ID` – Update an existing employee by ID
- **DELETE** `/employees/ID` – Deletes an employee by ID

## License
MIT License
