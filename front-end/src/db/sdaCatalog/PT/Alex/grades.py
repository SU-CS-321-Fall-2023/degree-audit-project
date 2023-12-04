import json

courses = list()
myIDs = list()
subjects = [
    ["ACCT", "01"],
    ["AERS", "02"],
    ["AFST", "03"],
    ["AMST", "04"],
    ["ANTH", "05"],
    ["LARB", "06"],
    ["ARTS", "07"],
    ["ARTH", "08"],
    ["ASIA", "09"],
    ["ASTR", "10"],
    ["BIOL", "11"],
    ["SOBA", "12"],
    ["BLAW", "13"],
    ["BSAN", "14"],
    ["CHEM", "15"],
    ["CHIN", "16"],
    ["COMM", "17"],
    ["CINF", "18"],
    ["CSCI", "19"],
    ["COUN", "20"],
    ["CREA", "21"],
    ["CSEC", "22"],
    ["DIGA", "23"],
    ["ECON", "24"],
    ["EDUC", "25"],
    ["EL", "26"],
    ["ENGL", "27"],
    ["ENCW", "28"],
    ["ENTP", "29"],
    ["ENSS", "30"],
    ["FENT", "31"],
    ["FINA", "32"],
    ["FSEM", "33"],
    ["FREN", "34"],
    ["GEND", "35"],
    ["GERM", "36"],
    ["HLSC", "37"],
    ["HIST", "38"],
    ["HONR", "39"],
    ["HRMT", "40"],
    ["INTL", "41"],
    ["INSU", "42"],
    ["ITAL", "43"],
    ["JWST", "44"],
    ["JOUR", "45"],
    ["LANG", "46"],
    ["LALS", "47"],
    ["LING", "48"],
    ["MGMT", "49"],
    ["MKTG", "50"],
    ["MATH", "51"],
    ["MILS", "52"],
    ["MUSC", "53"],
    ["MUSA", "54"],
    ["MUED", "55"],
    ["MUSE", "56"],
    ["MUSX", "57"],
    ["PHIL", "58"],
    ["PHYS", "59"],
    ["POLI", "60"],
    ["PORT", "61"],
    ["PRHP", "62"],
    ["PSYC", "63"],
    ["PUBH", "64"],
    ["RELS", "65"],
    ["REES", "66"],
    ["RUSS", "67"],
    ["SALS", "68"],
    ["SSCI", "69"],
    ["SOCI", "70"],
    ["SPAN", "71"],
    ["SPTB", "72"],
    ["STAT", "73"],
    ["SA", "74"],
    ["FOOD", "75"],
    ["THEA", "76"],
    ["TRF", "77"],
    ["WLGC", "78"],
    ["LAW", "100"]
]


try:
    with open("front-end\\src\\db\\sdaCatalog\\PT\\Alex\\grades.json", "r") as myFile:
        ourData = json.load(myFile)
        for x in range(len(ourData["data"])):
            for i in range(len(subjects)):
                if (ourData["data"][x]["subjectCode"] == subjects[i][0]):
                    newID = (subjects[i][1] + ourData["data"][x]["courseNumber"])
                    myIDs.append(newID)
                    break
            app_data = {
                "id": myIDs[x],
                "courseNumber": ourData["data"][x]["courseNumber"],
                "subject": ourData["data"][x]["subjectCode"],
                "courseReferenceNumber": ourData["data"][x]["courseReferenceNumber"],
                "section": ourData["data"][x]["section"],
                "courseTitle": ourData["data"][x]["courseTitle"],

                "levelCode": ourData["data"][x]["levelCode"],
                "levelDescription": ourData["data"][x]["levelDescription"],
                "campusCode": ourData["data"][x]["campusCode"],
                "termDescription": ourData["data"][x]["termDescription"],

                "gpaHours": ourData["data"][x]["gpaHours"],
                "hoursAttempted": ourData["data"][x]["hoursAttempted"],
                "hoursEarned": ourData["data"][x]["hoursEarned"],
                "midtermGrade": ourData["data"][x]["midtermGrade"],
                "finalGrade": ourData["data"][x]["finalGrade"],
                "calculatedFinalGrade": ourData["data"][x]["calculatedFinalGrade"],
                "historyFinalGrade": ourData["data"][x]["historyFinalGrade"],
                "qualityPoints": ourData["data"][x]["qualityPoints"]
            }
            courses.append(app_data)
        with open('front-end\\src\\db\\sdaCatalog\\PT\\Alex\\gradesTrimmed.json', 'w') as json_file:
            json.dump(courses, json_file, indent=4)
        print("gradesTrimmed.json has been created.")

except json.JSONDecodeError as e:
    print(f"JSON decoding error: {e}")
