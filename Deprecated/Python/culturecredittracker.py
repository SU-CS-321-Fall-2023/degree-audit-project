from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Here, you would fetch data from Stetson's Engage platform and process it to show the user's cultural credits.
    user_cultural_credits = 24
    credits_remaining = 10  # Change this to the remaining credits.

    # Dummy data for cultural credit events.
    cultural_events = [
        {"name": "Pollination:The Art of Citizen Science", "date": "2023-24-08", "units": "1"},
        {"name": "The Bone Wars: Museums, Fossils and National Identity ", "date": "2023-24-08", "units": "1"},
        # Add more events here.
    ]

    return render_template('index.html', credits=user_cultural_credits, remaining=credits_remaining, events=cultural_events)

if __name__ == '__main__':
    app.run(debug=True)
