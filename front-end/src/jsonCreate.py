import requests
import json

# jsonCreate.py --> trimmer.py --> test.py

session = requests.Session()

# Both of these cookies are necessary to access the URL.
# You will need to get your own personal cookies.
#! We don't condone cookie sharing here!!
# session.cookies['JSESSIONID'] = 'your JSESSIONID'
# session.cookies['INGRESSCOOKIE'] = 'your INGRESSCOOKIE'

# url = 'https://myapps.stetson.edu/StudentRegistrationSsb/ssb/registration'
data_url = 'https://myapps.stetson.edu/StudentRegistrationSsb/ssb/registrationHistory/reset?term=202315'

try:
    response = session.get(data_url)
    response.raise_for_status()

    if response.status_code == 200:
        print("Request was successful.")
        data = response.json()
        with open('Output Files/student_data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print("student_data.json has been created.")
        # print(response.text)  # Print the content of the page
    else:
        print("Request failed with status code:", response.status_code)

except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
except json.JSONDecodeError as e:
    print(f"JSON decoding error: {e}")










# import requests
# import json

# session = requests.Session()

# url = 'https://myapps.stetson.edu/StudentRegistrationSsb/ssb/registrationHistory/reset?term=202315'

# myCookies = {}

# try:
#     # cookies = session.cookies
#     # for cookie in cookies:
#     #     print(f"Cookie Name: {cookie.name}, Cookie Value: {cookie.value}")
#     response = session.get(url, cookies=session.cookies)
#     response.raise_for_status()
#     if response.status_code == 200:
#         print("Request was successful.")
#         cookies = session.cookies
#         for cookie in cookies:
#             if ((cookie.name == 'JSESSIONID') or (cookie.name == 'INGRESSCOOKIE')):
#                 print(f"Cookie Name: {cookie.name}, Cookie Value: {cookie.value}")
#                 myCookies[cookie.name] = cookie.value
#                 pass
#             else:
#                 session.cookies.pop(cookie.name)
#         print(myCookies)
#         response2 = session.get(url, cookies=myCookies)
#         data = response.json()
#         with open('test003.json', 'w') as json_file:
#             json.dump(data, json_file, indent=4)

#         # print(response.text)  # Print the content of the page
#     else:
#         print("Request failed with status code:", response.status_code)

#     # cookies = session.cookies
#     # for cookie in cookies:
#     #     match cookie.name:
#     #         case 'JSESSIONID':
#     #             session.cookies['JSESSIONID'] = cookie.value
#     #             print(f"Cookie1 {cookie.value}")
#     #         case 'INGRESSCOOKIE':
#     #             session.cookies['INGRESSCOOKIE'] = cookie.value
#     #             print(f"Cookie2 {cookie.value}")
#     #         case _:
#     #             print(f"Cookie Name: {cookie.name}, Cookie Value: {cookie.value}")
#     # print("\n\n")
#     # print(session.cookies)
#     # data = response.json()
#     # with open('test003.json', 'w') as json_file:
#     #     json.dump(data, json_file, indent=4)


# except requests.exceptions.RequestException as e:
#     print(f"Request error: {e}")
# except json.JSONDecodeError as e:
#     print(f"JSON decoding error: {e}")
