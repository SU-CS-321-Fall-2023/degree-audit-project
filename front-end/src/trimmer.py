import os, json
import jsonCreate

# ourFile = '\\student_data.json'
lineCount = 0
filteredData = []

try:
    with open('student_data.json', 'r') as f:
        lineCount= sum(1 for _ in f)
    print(f"Line Count: {lineCount}")

    with open('student_data.json', 'r') as ourFile:
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
            # }
            # filteredData.append(app_data)
            # app_data = {
                # "courseTitle": ourData["data"]["registrations"][1]["courseTitle"],
                # "courseReferenceNumber": ourData["data"]["registrations"][1]["courseReferenceNumber"],
                # "termDescription": ourData["data"]["registrations"][1]["termDescription"],
                
                # "courseTitle": ourData["data"]["registrations"][2]["courseTitle"],
                # "courseReferenceNumber": ourData["data"]["registrations"][2]["courseReferenceNumber"],
                # "termDescription": ourData["data"]["registrations"][2]["termDescription"],
                
                # "courseTitle": ourData["data"]["registrations"][3]["courseTitle"],
                # "courseReferenceNumber": ourData["data"]["registrations"][3]["courseReferenceNumber"],
                # "termDescription": ourData["data"]["registrations"][3]["termDescription"],
                # "courseReferenceNumber": ourData["courseReferenceNumber"],
                # "termDescription": ourData["termDescription"]
            }
            filteredData.append(app_data)
        print("\n".join(map(str, filteredData)))
        with open('Output Files/filtered.json', 'w') as json_file:
            json.dump(filteredData, json_file, indent=4)
        print("filtered.json has been created.")

        # courseTitle = ourData['courseTitle']
        # print(f"Course Title: {courseTitle}")

    # print(ourParse['courseTitle'])
    # for item in ourParse['items']:
    #     print(item['name'])
    # for cookie in cookies:
    #     match cookie.name:
    #         case 'JSESSIONID':
    #             session.cookies['JSESSIONID'] = cookie.value
    #             print(f"Cookie1 {cookie.value}")
    #         case 'INGRESSCOOKIE':
    #             session.cookies['INGRESSCOOKIE'] = cookie.value
    #             print(f"Cookie2 {cookie.value}")
    #         case _:
    #             print(f"Cookie Name: {cookie.name}, Cookie Value: {cookie.value}")
except json.JSONDecodeError as e:
    print(f"JSON decoding error: {e}")

# TIMING
# time1 = time.time_ns()
# time2 = time.time_ns()
# time3 = time2 - time1
# print(f"time3: {time3}")

# Read file line by line:
# with open('student_data.json', 'r') as ourFile:
#     for x in range(lineCount):
#         content = ourFile.readline()
#         print(content)

# Read file as whole
# with open('student_data.json', 'r') as ourFile:
#     content = ourFile.read()
#     print(content)
