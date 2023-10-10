from flask import Flask
from flask import render_template
# from flask import url_for
import os

def ourPaths():
    """
    ourPaths() must be placed at the beginning of the file 
    in order for the site to build and run.
    
    ourPaths() must be called immediately after it ends.
    """
    global webletIndex
    webletIndex = 'index.html'
    
    global rootPath
    rootPath = os.path.abspath(os.getcwd()) + "/front-end/src"
ourPaths() # Must be placed at beginning of file.


app = Flask(
    __name__,
    root_path=(rootPath),
    # "D:/GitHub/Software Dev II/The-Auditors/degree-audit-project/front-end/src",
    template_folder="./templates",
    static_folder="./static")



@app.route("/index")
def index():
    return render_template(webletIndex)

@app.route('/data')
def database():
    return 'data'






if __name__ == '__main__':
    """
    Must be placed at the end of the file.
    """
    app.run(host = '127.0.0.1', port = 8000, debug = True)
