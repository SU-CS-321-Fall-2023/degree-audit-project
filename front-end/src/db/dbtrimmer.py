import os, json
import dbjsonCreate

# jsonCreate.py --> trimmer.py --> test.py

# ourFile = '\\student_data.json'
lineCount = 0
filteredData = []

try:
    with open('Output Files/student_data.json', 'r') as f:
        lineCount= sum(1 for _ in f)
    print(f"Line Count: {lineCount}")

    with open('Output Files/student_data.json', 'r') as ourFile:
        # content = ourFile.read()
        # print(content)
        ourData = json.load(ourFile)
        # print(ourData)
        for x in range(len(ourData["data"]["registrations"])):
            # for app in ourData["data"]["registrations"]:
            app_data = {
                "courseTitle": ourData["data"]["registrations"][x]["courseTitle"],
                "courseReferenceNumber": ourData["data"]["registrations"][x]["courseReferenceNumber"],
                "termDescription": ourData["data"]["registrations"][x]["termDescription"],
            }
            filteredData.append(app_data)
        print("\n".join(map(str, filteredData)))
        with open('Output Files/filtered.json', 'w') as json_file:
            json.dump(filteredData, json_file, indent=4)
        print("filtered.json has been created.")

except json.JSONDecodeError as e:
    print(f"JSON decoding error: {e}")
