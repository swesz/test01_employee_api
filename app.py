# web API for HTTP requests
from flask import Flask, request, jsonify
# SQL database functionality inside Python
from flask_sqlalchemy import SQLAlchemy
# JSON formatting for API responses
from flask_marshmallow import Marshmallow

# Initialize Flask app
app = Flask(__name__)

# Database configuration (store records in employees.db)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Database & Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Employee Model (table)
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    job_title = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Float, nullable=False)
    department = db.Column(db.String(100), nullable=False)

    def __init__(self, name, job_title, salary, department):
        self.name = name
        self.job_title = job_title
        self.salary = salary
        self.department = department

# Employee Schema (convert employee objects into JSON format)
class EmployeeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Employee

employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)

# Create database tables
with app.app_context():
    db.create_all()

# API Routes

# Get all employees
@app.route('/employees', methods=['GET'])
def get_employees():
    all_employees = Employee.query.all()
    return jsonify(employees_schema.dump(all_employees))

# Get single employee by ID
@app.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    employee = Employee.query.get(id)
    if employee:
        return jsonify(employee_schema.dump(employee))
    return jsonify({"error": "Employee not found"}), 404

# Add new employee
@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.json
    new_employee = Employee(
        name=data['name'],
        job_title=data['job_title'],
        salary=data['salary'],
        department=data['department']
    )
    db.session.add(new_employee)
    db.session.commit()
    return jsonify(employee_schema.dump(new_employee)), 201

# Update employee
@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    employee = Employee.query.get(id)
    if not employee:
        return jsonify({"error": "Employee not found"}), 404

    data = request.json
    employee.name = data.get('name', employee.name)
    employee.job_title = data.get('job_title', employee.job_title)
    employee.salary = data.get('salary', employee.salary)
    employee.department = data.get('department', employee.department)

    db.session.commit()
    return jsonify(employee_schema.dump(employee))

# Delete employee
@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    employee = Employee.query.get(id)
    if not employee:
        return jsonify({"error": "Employee not found"}), 404

    db.session.delete(employee)
    db.session.commit()
    return jsonify({"message": "Employee deleted successfully"})

# Run the app (start Flask server)
if __name__ == '__main__':
    app.run(debug=True)
