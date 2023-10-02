# Course Retrieval (from Academic Transcripts)

Courtesy of Alexander Garofalo
9:00 PM 9/23/2023

## Link for Academic Transcripts

    You may have to log into your myStetson first: 
    https://myapps.stetson.edu/StudentRegistrationSsb/ssb/registrationHistory/reset?term=202415

## Rundown

    "term=######"
The value for "term" parameter will be a 6-digit number. The first four numbers represent the Academic Year and the last two numbers are coded to represent the Semester.

### Possible values

#### First Four Numbers

    - 2021 = 2020-2021 Academic Year
    - 2022 = 2021-2022 Academic Year
    - 2023 = 2022-2023 Academic Year
    - 2024 = 2023-2024 Academic Year (this year)
    etc.

#### Last Two Numbers

Only three options exist for these:

    - 15 = Fall Semester
    - 25 = Spring Semester
    - 35 = Summer Semester

#### Putting them together

    - 202115 = Fall 2020 Semester
    - 202125 = Spring 2021 Semester
    - 202135 = Summer 2021 Semester
    - 202215 = Fall 2021 Semester
    and so on and so forth.

### Significance

Why is this significant?? Rather than trying to battle with a Web Scraper that has to parse HTML tags and the Inner Text and Text Content, this link will take you to a page that is set up as a .JSON file. I have been going through the HTML source code of the Registration Dashboard and the Student Dashboard, trying to figure out which one would better serve as the source for a given student's course history. During this, I began having doubts on whether it would even end up working. Regardless, I have realized a major flaw in this approach: if it (somehow) does not prove to be overly complicated, the code built upon this approach will surely break if any of the HTML source code is ever changed (i.e. there is a change in 3rd Party service providers, Ellucian, or if the structure of the page is changed).

With that being said, we can alter our approach and use the links as the "source". This way, if Stetson ever does change the 3rd Party service provider or the link changes, all they have to do is update the link in our program's source code to reflect the new one. I can explain this more during our meeting tomorrow.
