from flask import Flask, render_template, request, jsonify
from flask import request 

app = Flask(__name__)

# This will act as a simple database in memory
reviews = []
last_review_id = 1000

@app.route('/')
def index():
    # Display the home page and form to submit reviews
    return render_template('index.html')

@app.route('/submit_review', methods=['POST'])
def submit_review():
    global last_review_id
    data = request.get_json()  # Get data sent as JSON
    
    # Extract 'course_code' and 'review_text' from the JSON object
    course_code = data.get('course_code')
    review_text = data.get('review_text')

    if not course_code or not review_text:
        # Return an error response
        return jsonify({'error': 'Missing course code or review text'}), 400

    # Increment the last review ID for a new review
    last_review_id += 1

    # Create a new review dictionary
    new_review = {
        'id': last_review_id,
        'course_code': course_code,
        'review_text': review_text
    }

    # Add the new review to the list of reviews
    reviews.append(new_review)

    # Return a JSON response with the new review ID
    return jsonify({'review_id': last_review_id}), 201


@app.route('/reviews/<course_code>')
def view_reviews(course_code):
    # Fetching reviews for course code
    course_reviews = [review for review in reviews if review['course_code'].lower() == course_code.lower()]
    
    # Display the reviews for the specific course
    return render_template('reviews.html', course_code=course_code.upper(), reviews=course_reviews)


if __name__ == '__main__':
    app.run(debug=True)
