from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():

    user_cultural_credits = 10
    credits_remaining = 24
    cultural_events = [
        {"name": "Pollination:The Art of Citizen Science", "date": "08-24-2023", "units": "1"},
        {"name": "The Bone Wars: Museums, Fossils and National Identity ", "date": "08-24-2023", "units": "1"},
        {"name": "International Trivia Games", "date": "11-29-2022", "units": "1"},
        {"name": "Taste of the World", "date": "11-03-2022", "units": "1"},
        {"name": "4th Annual Haunted History Tour", "date": "10-25-2022", "units": "1"},
        {"name": "Princess and the Frog: African Spirituality", "date": "10-11-2022", "units": "1"},
        {"name": "Murder at the Howard Johnson's Sam Brobick", "date": "09-29-2022", "units": "1"},
        {"name": "Black Health Matters", "date": "04-27-2022", "units": "1"},
        {"name": "Divine Nine History & Step Show", "date": "02-18-2022", "units": "1"},
        {"name": "BSA Ball:70's Boogies Night","date": "02-25-2022", "units": "1"}
    ]

    return render_template('culture-index.html', credits=user_cultural_credits, remaining=credits_remaining,
                           events=cultural_events)


if __name__ == '__main__':
    app.run(debug=True)
