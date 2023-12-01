import os, json


lineCount = 0
filteredData = []

try:
    with open('Output Files/db/subjects.json', 'r') as f:
        lineCount= sum(1 for _ in f)
    print(f"Line Count: {lineCount}")

    with open('Output Files/db/subjects.json', 'r') as ourFile:
        # content = ourFile.read()
        # print(content)
        ourData = json.load(ourFile)
        # print(ourData)
        for x in range(len(ourData)):
            # for app in ourData["data"]["registrations"]:
            app_data = {
                "subject": ourData[x]["code"]
            }
            filteredData.append(app_data)
        print("\n".join(map(str, filteredData)))
        with open('Output Files/db/subfilter.json', 'w') as json_file:
            json.dump(filteredData, json_file, indent=4)
        print("subfilter.json has been created.")

except json.JSONDecodeError as e:
    print(f"JSON decoding error: {e}")
