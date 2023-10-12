# import jsonCreate # importing script, creates student_data.json
import trimmer

# desired_parameters = ['courseTitle', 'courseReferenceNumber', 'termDescription', 'courseNumber']
# filtered_data  = {}

# def myCreator():
#     return jsonCreate
def myTrimmer():
    return trimmer

myTrimmer()
# try:
    # myCreator()
    # response = session.get(url)
    # response.raise_for_status()
    # data = response.json()
    # with open('test003.json', 'w') as json_file:
    #     json.dump(data, json_file, indent=4)
    # match id.lower:
    #     case _:
    #         folderPath = "./Documentation/Test/Output Files/" + id
    #         status = os.path.isdir(folderPath)
    #         match status:
    #             case True:
    #                 print(f"Copying {currentFile} to {folderPath}...")
    #                 shutil.copy2(currentFile, folderPath)
    #             case False:
    #                 print(f"\nCreating {folderPath}...")
    #                 os.mkdir(folderPath)
    #                 print(f"Copying {currentFile} to {folderPath}...")
    #                 shutil.copy2(currentFile, folderPath)
    #             case _:
    #                 print("OHH! Great heavens! That was a BOOOOOOOL?!?!")

    # data_dict = {
    #     'courseTitle': print(f"{data}\n")
    # }
    # with open('test002.json', 'w') as json_file:
    #     json.dump(data, json_file, indent=4)
    
    
    # for param in desired_parameters:
    #     if param in data:
    #         filtered_data[param] = data[param]
    # print(filtered_data)
    # courseTitle = data['courseTitle']
    # print(courseTitle)
    # print(data)
    
    # if response.status_code == 200:
    #     print("Request was successful.")
    #     # print(response.text)  # Print the content of the page
    # else:
    #     print("Request failed with status code:", response.status_code)

# except requests.exceptions.RequestException as e:
#     print(f"Request error: {e}")
# except json.JSONDecodeError as e:
#     print(f"JSON decoding error: {e}")
