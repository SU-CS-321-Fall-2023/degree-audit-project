# Course Search (from Course Catalog in Registration Dashboard)

Courtesy of Alexander Garofalo
9:00 PM 9/23/2023

## Link for Course Catalog

    The same type of page exists for the Course Search in the Registration Dashboard: 
    Base link: https://myapps.stetson.edu/StudentRegistrationSsb/ssb/term/termSelection?mode=search

    User-specific link (NOT VALID): https://myapps.stetson.edu/StudentRegistrationSsb/ssb/searchResults/searchResults?txt_term=202415&startDatepicker=&endDatepicker=&uniqueSessionId={userSessionId}&pageOffset=0&pageMaxSize=50&sortColumn=subjectDescription&sortDirection=asc

    **I just discovered that you don't have to be authenticated to search for courses in the Registration Dashboard. MORE TESTING NEEDED.

## Rundown

    "uniqueSessionId={userSessionId}"   --> Value of "xe.unique.session.storage.id" in Session Storage.
    "pageOffset={somePositiveInteger}"  --> Integer must be greater than or equal to zero.
    "pageMaxSize={somePositiveInteger}" --> Integer must be greater than zero.

### uniqueSessionId

We would have to replace the "uniqueSessionId={userSessionId}" . This can be done by grabbing the value of "xe.unique.session.storage.id", which is found in the Session Storage.

To view your own xe.unique.session.storage.id:

1. Right-click on the screen
2. Click INSPECT
3. Click on the APPLICATION tab
4. Scroll down to STORAGE
5. Expand the SESSION STORAGE label
6. Click on the session
7. Copy value of key "xe.unique.session.storage.id"

### pageOffset

The parameter of this property will range from 0 to one minus the total number of offered courses for that semester. For Fall 2023, there are 1160 different classes (includes multiple sessions). So, in this case, the parameter could range from 0 to 1159.

### pageMaxsize

The parameter of this property will determine the number of courses whose details will be returned on the page.
