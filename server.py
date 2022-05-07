from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('/home.html')

@app.route('/attendance/attendance.py')
def my_link():
  print ('Attendance Taken')

  from attendance import attendance
  return ('Done')
  
  # cwd=os.getcwd()
  # path=os.path.join(cwd,'attendance','attendance.py')
  # file = open(path, 'r').read()
  # return exec(file)

if __name__ == '__main__':
  app.run(debug=True)