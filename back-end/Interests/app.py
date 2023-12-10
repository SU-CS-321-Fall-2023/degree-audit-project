from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

default_interests = ["Computer Science", "Psychology", "Biology", "Mathematics", "Chemistry","Cybersecurity"]
selected_interests = []


@app.route('/')
def index():
    return render_template('interests-index.html', default_interests=default_interests)


def generate_course_recommendations(interests):
    course_data = {
        "Computer Science": ["CSCI141", "CSCI142", "CSCI201", "CSCI211", "CSCI221", "CSCI321", "CSCI301", "CSCI311",
                             "CSCI498", "CSCI499"],
        "Psychology": ["PSYC101S", "PSYC203", "PSYC306Q", "PYSC498", "PYSC499", "PYSC211", "PSYC313V", "PYSC414",
                       "PSYC221", "PSYC322", "PYSC231", "PYSCH332", "PSYC334", "PSYC435", "PSYC242", "PSYC241",
                       "PSYC343", "PSYC444", "PSYC445", "PSYC251V", "PSYC352V", "PSYC352V", "PSYC353", "PSYC451",
                       "PSYC452V", "PSYC180"],
        "Biology": ["BIOL100", "BIOL141P", "BIOL142P", "BIOL243Q", "BIOL244", "BIOL497", "BIOL498", "BIOL499"],
        "Mathematics": ["MATH142Q", "MATH243Q", "MATH211Q", "MATH312", "MATH401", "MATH431""MATH441", "MATH321",
                        "MATH341", "MATH351", "MATH361", "MATH498", "MATH499"],
        "Chemistry": ["CHEM141P", "CHEM142P", "CHEM201", "CHEM202", "CHEM203", "CHEM204", "CHEM205", "CHEM301",
                      "CHEM498", "CHEM499", "CHEM302", "CHEM303", "CHEM304", "CHEM305", "CHEM306", "CHEM307", "CHEM308",
                      "CHEM309"],
        "Cybersecurity": ["CSCI 141 - Introduction to Computer Science I",
                          "CSCI 142 - Introduction to Computer Science II", "CSCI 221 - Software Development I",
                          "CSCI 301 - Operating Systems", "CSCI 304 - Computer Networks", "CINF 201 - Database Systems",
                          "CINF 301 - Web Application Development", "CSEC 141 - Introduction to Cybersecurity",
                          "CSEC 302 - Secure Coding", "CSEC 331 - Computer and Network Security",
                          "CSEC 498 - Senior Proposal", "CSEC 499 - Senior Project"]
    }

    recommended_courses = []
    for interest in interests:
        if interest in course_data:
            recommended_courses.extend(course_data[interest])

    return recommended_courses


@app.route('/submit', methods=['POST'])
def submit():
    selected_interests.clear()
    selected_interests.extend(request.form.getlist('interests'))

    if 'OTHER' in selected_interests:
        custom_interest = request.form.get('custom_interest')
        if custom_interest:
            selected_interests.remove('OTHER')
            selected_interests.append(custom_interest)

    recommended_courses = generate_course_recommendations(selected_interests)

    return render_template('interests-courses.html', interests=selected_interests, courses=recommended_courses)


if __name__ == '__main__':
    app.run(debug=True)
