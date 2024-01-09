from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///employees.db"
db = SQLAlchemy(app)


class Employee(db.Model):
    emp_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    design = db.Column(db.String(40), nullable=False)
    loc = db.Column(db.String(20), nullable=False)

    def __repr__(self) -> str:
        return f"{self.emp_id} - {self.name}"


# For generating "Employees.db"
with app.app_context():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def submit_employee():
    if request.method == 'POST':
        name = request.form['name']
        design = request.form['design']
        loc = request.form['loc']

        emp = Employee(name=name, design=design, loc=loc)

        db.session.add(emp)
        db.session.commit()

    all_emp = Employee.query.all()
    return render_template('index.html', all_emp=all_emp)


@app.route('/update/<int:emp_id>', methods=['GET', 'POST'])
def update_employee(emp_id):
    if request.method == 'POST':
        name = request.form['name']
        design = request.form['design']
        loc = request.form['loc']

        emp = Employee.query.filter_by(emp_id=emp_id).first()
        emp.name = name
        emp.design = design
        emp.loc = loc

        db.session.add(emp)
        db.session.commit()

        return redirect('/')

    emp = Employee.query.filter_by(emp_id=emp_id).first()
    return render_template('update.html', emp=emp)


@app.route('/delete/<int:emp_id>')
def delete_employee(emp_id):
    emp = Employee.query.filter_by(emp_id=emp_id).first()
    db.session.delete(emp)
    db.session.commit()

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, port=8000)
