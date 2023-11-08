import os
import subprocess

# // TODO: Call SWI-Prolog from this file.
# // TODO: After opening program, consult "corduroy.pro"
# // TODO: Run queries to create lists of majors
# TODO: Break code into functions.

subprocess.call(args="C:/Program Files/swipl/bin/swipl-win.exe")

# Replace the file paths with your own
degrees = [
    "D:/GitHub/Software Dev II/The-Auditors/degree-audit-project/Prolog/baMajors.txt",
    "D:/GitHub/Software Dev II/The-Auditors/degree-audit-project/Prolog/bsMajors.txt",
    "D:/GitHub/Software Dev II/The-Auditors/degree-audit-project/Prolog/bbaMajors.txt",
    "D:/GitHub/Software Dev II/The-Auditors/degree-audit-project/Prolog/bmMajors.txt",
    "D:/GitHub/Software Dev II/The-Auditors/degree-audit-project/Prolog/bmeMajors.txt"
]
baMajors  = degrees[0]
bsMajors  = degrees[1]
bbaMajors = degrees[2]
bmMajors  = degrees[3]
bmeMajors = degrees[4]

allMajors    = "D:/GitHub/Software Dev II/The-Auditors/degree-audit-project/Prolog/allMajors.txt"
majorsSorted = "D:/GitHub/Software Dev II/The-Auditors/degree-audit-project/Prolog/majorsSorted.txt"

contents = ''
for i in range(len(degrees)):
    if os.path.isfile(degrees[i]):
        print(f"'{degrees[i]}' is being read....")
        with open(degrees[i], "r") as myFile:
            while True:
                char = myFile.read(1)
                if not char:
                    break
                match char:
                    case '[':
                        contents += ""
                    case '(':
                        contents += "["
                    case ')':
                        contents += "] "
                    case ']':
                        contents += ""
                    case _:
                        contents += char
        contents += "\n"
        myFile.close() # Ensures that no streams are left open.
print(f"contents:\n{contents}")
contentsListed = contents.split(" ,")
print(f"contentsListed:\n{contentsListed}")

fullContents = ''
if os.path.isfile(allMajors):
    print(f"'{allMajors}' is being read....")
    with open(allMajors, "r") as myFile:
        while True:
            char = myFile.read(1)
            if not char:
                break
            match char:
                case '[':
                    fullContents += ""
                case '(':
                    fullContents += "["
                case ')':
                    fullContents += "] "
                case ']':
                    fullContents += ""
                case _:
                    fullContents += char
    fullContents += "\n"
    myFile.close() # Ensures that no streams are left open.
print()
print(f"fullContents:\n{fullContents}")
fullContentsListed = fullContents.split(" ,")
print(f"fullContentsListed:\n{fullContentsListed}")

print()

# This little snippet is from my Senior Project -- Alexander Garofalo
# BEGINNING OF SNIPPET
if os.path.isfile(majorsSorted):
    print(f"'{majorsSorted}' exists and has been marked for deletion...")
    os.remove(majorsSorted)
else:
    print(f"Error!! '{majorsSorted}' was not found.")
# END OF SNIPPET

for i in range(len(fullContentsListed)):
    with open(majorsSorted, "a") as myFile:
        myFile.write(f"{fullContentsListed[i]}\n")

myFile.close() # Ensures that no streams are left open.
