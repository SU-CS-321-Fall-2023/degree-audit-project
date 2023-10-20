from werkzeug.utils import secure_filename
from flask import Flask, jsonify, request, redirect, url_for
from flask import render_template, send_from_directory
from flask_cors import CORS
import csv
import os

def ourPaths():
    """
    ourPaths() must be placed at the beginning of the file 
    in order for the site to build and run.
    
    ourPaths() must be called immediately after it ends.
    
    Purpose: Initializes necessary variable for web app.
    """
    global rootPath
    # rootPath = os.path.abspath(os.getcwd()) + "\\front-end\\src"
    rootPath = os.path.abspath(os.getcwd())
    print(f"rootPath: {rootPath}")
    
    global webletIndex
    webletIndex =  "index.html"
ourPaths() # Must be placed at beginning of file.

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


app = Flask(
    __name__,
    root_path=(rootPath),
    # "D:/GitHub/Software Dev II/The-Auditors/degree-audit-project/front-end/src",
    # template_folder= rootPath + "/frontend/src/templates",
    # static_folder= rootPath + "/frontend/src")
    template_folder= rootPath + "/frontend/src/templates",
    static_folder= rootPath + "/frontend/src/components")
# cors = CORS(app)
# Configure the value of the "origins" key to be the actual URL of the React Frontend.
# Make sure to NOT have a / at the end of the "origins" URL.
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:*"}})

ALLOWED_EXTENSIONS = {'csv'}
# class Index(Resource):
    # def get(self):
    #     data = []
    #     # render_template(webletIndex, data=data)
    #     return jsonify(render_template(webletIndex, data=data))

    # def post(self):
    #     data = request.get_json()
    #     return jsonify({'data': data}), 201



# @app.route("/index")
# def index():
#     return render_template(webletIndex)

# @app.route('/data')
# def database():
#     return 'data'



@app.route('/', methods=['GET', 'POST'])
def index():
    data = []  # A list to hold our CSV data

    # Use raw string notation for the path or double up the backslashes
<<<<<<< HEAD:back-end/src/weblet.py
    userCSV_path = rootPath + '\\user.csv'
=======
    userCSV_path = rootPath + '\\front-end\\src\\user.csv'
>>>>>>> 261dcfff76bf80a916565283d7d9c178763f332c:back-end/weblet.py
    reqsCSV_path = rootPath + r'\\reqs.csv'
    testCSV_path = rootPath + r'\\test.csv'

    if request.method == 'POST':
        email = request.form.get('student_email', None)  # Fetch the major entered by the user

        # Read the predefined CSV file and store the data
        #with open(userCSV_path, 'r') as f:
         #   reader = csv.reader(f)
          #  data = [row for row in reader]

        # Filter the data based on the major if one is entered
        #if email:
            # Assuming the major is in the 2nd column (index 1). Adjust the index if needed.
         #   data = [data[0]] + [row for row in data[1:] if email.lower() in row[1].lower()]
    else:
        print("else Statement has been reached for /api/index.")
        # print("GET method has been used for /api/index .")

    return render_template("index.html", data=data)

# @app.route('/api/static/', methods=['GET', 'POST'])

# @app.route('/api/data')
# def get_data():
#     data = {'message': 'Hello from the Flask API!'}
#     return jsonify(data)



# Sydney's log
    # csv_path = rootPath + r'\\Academic Programs - Stetson University.csv'
    #r'C:\Users\sydne\OneDrive - Stetson University, Inc\Desktop\Computer Science\Python\DegreeAudit.Databasefinal.csv'
    #r'C:\Users\sydne\OneDrive - Stetson University, Inc\Desktop\Computer Science\Python\DegreeAudit.Database.csv'
    #r'C:\Users\sydne\OneDrive - Stetson University, Inc\Desktop\Computer Science\Python\Academic_Programs_-_Stetson_University.csv'

    # if request.method == 'POST':
    #     major = request.form.get('major', None)  # Fetch the major entered by the user

    #     # Read the predefined CSV file and store the data
    #     with open(csv_path, 'r') as f:
    #         reader = csv.reader(f)
    #         data = [row for row in reader]

    #     # Filter the data based on the major if one is entered
    #     if major:
    #         # Assuming the major is in the 2nd column (index 1). Adjust the index if needed.
    #         data = [data[0]] + [row for row in data[1:] if major.lower() in row[1].lower()]

    # return render_template(webletIndex, data=data)



if __name__ == '__main__':
    """
    Must be placed at the end of the file.
    """
    # app.run(host = '192.168.1.46', port = 3000, debug = True)
    app.run(host = '127.0.0.1', port = 3000, debug = True)
