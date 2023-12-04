import json

"""
    This Python file was created and used to reconstruct the 
    Stetson course catalog to fit the needs of the newer 
    Smart Degree Audit (SDA) Catalog.

    newCatalog.json is just a copy of 2024SpringCatalog.json

    sdaCatalog.json serves as our reconstructed course catalog. 
    This was then imported into the MySQL Database to form the 
    SDA Course Catalog database.
    """

null = None
lineCount = 0
newCatalog = list()
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
    # with open('front-end\src\db\sdaCatalog\sdaCatalog.json', 'r') as f:
    #     lineCount= sum(1 for _ in f)
    # print(f"Line Count: {lineCount}")

    with open('front-end\\src\\db\\sdaCatalog\\Other\\newCatalog.json', 'r') as ourFile:
        ourData = json.load(ourFile)
        for x in range(len(ourData["data"])):
            for i in range(len(subjects)):
                if (ourData["data"][x]["subject"] == subjects[i][0]):
                    newID = (subjects[i][1] + ourData["data"][x]["courseNumber"])
                    myIDs.append(newID)
                    break
            app_data = {
                "entry": x+1,
                "id": myIDs[x],
                "termEffective": ourData["data"][x]["termEffective"],
                "courseNumber": ourData["data"][x]["courseNumber"],
                "subject": ourData["data"][x]["subject"],
                "subjectCode": ourData["data"][x]["subjectCode"],
                "college": ourData["data"][x]["college"],
                "collegeCode": ourData["data"][x]["collegeCode"],
                "department": ourData["data"][x]["department"],
                "departmentCode": ourData["data"][x]["departmentCode"],
                "courseTitle": ourData["data"][x]["courseTitle"],
                # "durationUnit": ourData["data"][x]["durationUnit"],
                # "numberOfUnits": ourData["data"][x]["numberOfUnits"],
                "attributes": ourData["data"][x]["attributes"],
                # "gradeModes": ourData["data"][x]["gradeModes"],
                "ceu": ourData["data"][x]["ceu"],
                "courseScheduleTypes": ourData["data"][x]["courseScheduleTypes"],
                # "courseLevels": ourData["data"][x]["courseLevels"],
                "creditHourLow": ourData["data"][x]["creditHourLow"],
                "creditHourHigh": ourData["data"][x]["creditHourHigh"],
                "creditHourIndicator": ourData["data"][x]["creditHourIndicator"],
                "lectureHourLow": ourData["data"][x]["lectureHourLow"],
                "lectureHourHigh": ourData["data"][x]["lectureHourHigh"],
                "lectureHourIndicator": ourData["data"][x]["lectureHourIndicator"],
                "billHourLow": ourData["data"][x]["billHourLow"],
                "billHourHigh": ourData["data"][x]["billHourHigh"],
                "billHourIndicator": ourData["data"][x]["billHourIndicator"],
                "labHourLow": ourData["data"][x]["labHourLow"],
                "labHourHigh": ourData["data"][x]["labHourHigh"],
                "labHourIndicator": ourData["data"][x]["labHourIndicator"],
                "otherHourLow": ourData["data"][x]["otherHourLow"],
                "otherHourHigh": ourData["data"][x]["otherHourHigh"],
                "otherHourIndicator": ourData["data"][x]["otherHourIndicator"],
                "description": ourData["data"][x]["description"],
                "subjectDescription": ourData["data"][x]["subjectDescription"],
                "courseDescription": ourData["data"][x]["courseDescription"],
                # "division": ourData["data"][x]["division"],
                "termStart": ourData["data"][x]["termStart"],
                "termEnd": ourData["data"][x]["termEnd"],
                "preRequisiteCheckMethodCde": ourData["data"][x]["preRequisiteCheckMethodCde"],
                # "anySections": ourData["data"][x]["anySections"],
                "prerequisites": null
            }
            newCatalog.append(app_data)
        with open('front-end\\src\\db\\sdaCatalog\\Other\\sdaCatalog.json', 'w') as json_file:
            json.dump(newCatalog, json_file, indent=4)
        print("sdaCatalog.json has been created.")

except json.JSONDecodeError as e:
    print(f"JSON decoding error: {e}")
