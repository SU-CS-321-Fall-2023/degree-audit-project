from flask import Blueprint, render_template

from weblet import rootPath, passwordTA, passwordTC, app

# app.register_blueprint(culturalCredits_bp, url_prefix='/cultural-credits')


culturalCredits_bp = Blueprint('culturalCredits', __name__,
                               root_path = rootPath,
                               template_folder= rootPath + "/front-end/src/Cultural-Credits/templates",
                               static_folder= rootPath + "/front-end/src/static")


@culturalCredits_bp.route('/culture')
def culture():
    # Here, you would fetch data from Stetson's Engage platform and process it to show the user's cultural credits.
    user_cultural_credits = 24
    credits_remaining = 10  # Change this to the remaining credits.

    # Dummy data for cultural credit events.
    cultural_events = [
        {"name": "Pollination:The Art of Citizen Science", "date": "2023-24-08", "units": "1"},
        {"name": "The Bone Wars: Museums, Fossils and National Identity ", "date": "2023-24-08", "units": "1"},
        # Add more events here.
    ]

    return render_template('culture.html', credits=user_cultural_credits, remaining=credits_remaining, events=cultural_events)
