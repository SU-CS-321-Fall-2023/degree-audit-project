import json, os

null = None
def readDatabase():
    """
    Use this file to read through the 'Database' for the
    the Smart Degree Audit (SDA) project.

    The 'Database' is the sdaCatalog.json file.
    """
    newCatalog = list()
    try:
        with open('front-end\\src\\db\\sdaCatalog\\sdaCatalog.json', 'r') as ourFile:
            # content = ourFile.read()
            # print(content)
            ourData = json.load(ourFile)
            # print(ourData)
            for x in range(len(ourData)):
                app_data = {
                    "entry": ourData[x]["entry"],
                    "id": ourData[x]["id"],
                    "termEffective": ourData[x]["termEffective"],
                    "courseNumber": ourData[x]["courseNumber"],
                    "subject": ourData[x]["subject"],
                    "subjectCode": ourData[x]["subjectCode"],
                    "college": ourData[x]["college"],
                    "collegeCode": ourData[x]["collegeCode"],
                    "department": ourData[x]["department"],
                    "departmentCode": ourData[x]["departmentCode"],
                    "courseTitle": ourData[x]["courseTitle"],
                    # "durationUnit": ourData["data"][x]["durationUnit"],
                    # "numberOfUnits": ourData["data"][x]["numberOfUnits"],
                    "attributes": ourData[x]["attributes"],
                    # "gradeModes": ourData["data"][x]["gradeModes"],
                    "ceu": ourData[x]["ceu"],
                    "courseScheduleTypes": ourData[x]["courseScheduleTypes"],
                    # "courseLevels": ourData["data"][x]["courseLevels"],
                    "creditHourLow": ourData[x]["creditHourLow"],
                    "creditHourHigh": ourData[x]["creditHourHigh"],
                    "creditHourIndicator": ourData[x]["creditHourIndicator"],
                    "lectureHourLow": ourData[x]["lectureHourLow"],
                    "lectureHourHigh": ourData[x]["lectureHourHigh"],
                    "lectureHourIndicator": ourData[x]["lectureHourIndicator"],
                    "billHourLow": ourData[x]["billHourLow"],
                    "billHourHigh": ourData[x]["billHourHigh"],
                    "billHourIndicator": ourData[x]["billHourIndicator"],
                    "labHourLow": ourData[x]["labHourLow"],
                    "labHourHigh": ourData[x]["labHourHigh"],
                    "labHourIndicator": ourData[x]["labHourIndicator"],
                    "otherHourLow": ourData[x]["otherHourLow"],
                    "otherHourHigh": ourData[x]["otherHourHigh"],
                    "otherHourIndicator": ourData[x]["otherHourIndicator"],
                    "description": ourData[x]["description"],
                    "subjectDescription": ourData[x]["subjectDescription"],
                    "courseDescription": ourData[x]["courseDescription"],
                    # "division": ourData["data"][x]["division"],
                    "termStart": ourData[x]["termStart"],
                    "termEnd": ourData[x]["termEnd"],
                    "preRequisiteCheckMethodCde": ourData[x]["preRequisiteCheckMethodCde"],
                    # "anySections": ourData["data"][x]["anySections"],
                    "prerequisites": ourData[x]["prerequisites"]
                }
                newCatalog.append(app_data)
            # # print("\n".join(map(str, newCatalog)))
            # with open('front-end\\src\\db\\sdaCatalog\\test.json', 'w') as json_file:
            #     json.dump(newCatalog, json_file, indent=4)
            # print("test.json has been created.")
            # # print(myIDs)

    except json.JSONDecodeError as e:
        print(f"JSON decoding error: {e}")
