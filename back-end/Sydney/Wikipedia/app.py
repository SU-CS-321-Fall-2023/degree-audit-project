#Test to upload
# import necessary libraries 
from flask import Flask, request, render_template 
import wikipedia
  
app = Flask(__name__) 
  
# create HOME View 
@app.route("/", methods=["POST", "GET"]) 
def home(): 
    if request.method == "GET": 
        return render_template("OLD-index.html") 
    else: 
        search = request.form["search"] 
  
        # Fetch data from wikipedia 
        result = wikipedia.summary(search, sentences=2) 
        title = search
        return render_template("OLD-results.html", title=title, summary=result)
        #return f"<h1>{result}</h1>"
  
if __name__ == '__main__': 
    app.run(debug=True) 
