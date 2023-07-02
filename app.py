from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
db = SQLAlchemy(app)

class Student(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False)
  college = db.Column(db.String(120), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    name = request.form['name']
    college = request.form['college']
    new_student = Student(name=name, college=college)

    try:
      db.session.add(new_student)
      db.session.commit()
      return jsonify({'result': 'success'})
    except:
      return jsonify({'result': 'error'})

  students = Student.query.order_by(Student.id).all()
  return render_template('index.html', students=students)

if __name__ == "__main__":
  app.run(debug=True)
