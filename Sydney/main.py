#import os
#import csv
#from flask import Flask, render_template, request

#app = Flask(__name__)

#UPLOAD_DIRECTORY = 'C:/Users/sydne/OneDrive - Stetson University, Inc/Desktop/Computer Science/degree-audit-project/back-end'
#app.config['UPLOAD_FOLDER'] = UPLOAD_DIRECTORY

#@app.route('/', methods=['GET', 'POST'])
#def index():
 #   data = []  # A list to hold our CSV data

  #  if request.method == 'POST':
   #     student_id = request.form.get('student_id')
    #    print(f"Received student ID: {student_id}")

        # Get the CSV path based on student ID
     #   csv_path = get_csv_path_for_student(student_id)
      #  print(f"Looking for CSV at path: {csv_path}")

       # if not os.path.exists(csv_path):
        #    print(f"CSV not found for student ID: {student_id}")
            # Handle the case where the CSV file doesn't exist for the given ID
         #   return "No data available for this student ID.", 400

        # Read the CSV file and store the data
        #with open(csv_path, 'r') as f:
         #   reader = csv.reader(f)
          #  data = [row for row in reader]

   # return render_template('index.html', data=data)

#def get_csv_path_for_student(student_id):
    # This will attempt to find a CSV with the name "studentID.csv" in your UPLOAD_DIRECTORY
    # Adjust this logic based on how your files are organized/named
 #   return os.path.join(app.config['UPLOAD_FOLDER'], f"{student_id}.csv")

#if __name__ == '__main__':
 #   app.run(host='192.168.1.216', port=5000, debug=True)


import os
import csv
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)

ALLOWED_EXTENSIONS = {'csv'}

UPLOAD_DIRECTORY = 'C:/Users/sydne/OneDrive - Stetson University, Inc/Desktop/Computer Science/degree-audit-project/back-end'
app.config['UPLOAD_FOLDER'] = UPLOAD_DIRECTORY

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    data = []  # A list to hold our CSV data

    if request.method == 'POST' and 'csv' in request.files:
        file = request.files['csv']
        if file.filename == '':
            # No selected file
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # Construct the path to save the file
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            print("Saving to:", save_path)
            file.save(save_path)

            # Read the saved CSV file and store the data
            with open(save_path, 'r') as f:
                reader = csv.reader(f)
                data = [row for row in reader]

            # After reading the CSV data, redirect isn't necessary.
            # The next line renders the index.html with CSV data

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host='192.168.1.216', port=5000, debug=True)
    #app.run(debug=True)












#import os
#from werkzeug.utils import secure_filename
#from flask import Flask, render_template, request, redirect, url_for

#app = Flask(__name__)

#ALLOWED_EXTENSIONS = {'csv'}

# This should be the directory where you want to save uploaded files, not the path of a specific file.
#UPLOAD_DIRECTORY = 'C:/Users/sydne/OneDrive - Stetson University, Inc/Desktop/Computer Science/degree-audit-project/back-end'
#app.config['UPLOAD_FOLDER'] = UPLOAD_DIRECTORY

#def allowed_file(filename):
 #   return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#@app.route('/', methods=['GET', 'POST'])
#def index():
 #   if request.method == 'POST' and 'csv' in request.files:
  #      file = request.files['csv']
   #     if file.filename == '':
            # No selected file
    #        return redirect(request.url)
     #   if file and allowed_file(file.filename):
      #      filename = secure_filename(file.filename)
            # Construct the path to save the file
       #     save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        #    print("Saving to:", save_path)  # Optional: to verify the save path
         #   file.save(save_path)
          #  return redirect(url_for('index'))
    #return render_template('index.html')

#if __name__ == '__main__':
 #   app.run(debug=True)










#import os
#from werkzeug.utils import secure_filename
#from flask import Flask, render_template, request, redirect, url_for

#app = Flask(__name__)

#UPLOAD_FOLDER = 'static/uploads'
#ALLOWED_EXTENSIONS = {'csv'}

#UPLOAD_DIRECTORY = 'C:/Users/sydne/OneDrive - Stetson University, Inc/Desktop/Computer Science/degree-audit-project/back-end/DegreeAudit.Database.csv'
#app.config['UPLOAD_FOLDER'] = UPLOAD_DIRECTORY

#def allowed_file(filename):
 #   return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#@app.route('/', methods=['GET', 'POST'])
#def index():
 #   if request.method == 'POST' and 'csv' in request.files:
  #      file = request.files['csv']
   #     if file.filename == '':
            # No selected file
    #        return redirect(request.url)
     #   if file and allowed_file(file.filename):
      #      filename = secure_filename(file.filename)
       #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #    return redirect(url_for('index'))
    #return render_template('index.html')

#if __name__ == '__main__':
#    app.run(debug=True)

