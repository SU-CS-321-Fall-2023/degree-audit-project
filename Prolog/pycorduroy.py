import os

# TODO: Call SWI-Prolog from this file.
# TODO: After opening program, consult "corduroy.pro"
# TODO: Run query to create "majors.txt"

# Replace the file paths with your own
majors = "D:/GitHub/Software Dev II/The-Auditors/degree-audit-project/Prolog/majors.txt"
majorsSorted = "D:/GitHub/Software Dev II/The-Auditors/degree-audit-project/Prolog/majorsSorted.txt"

contents = ''

if os.path.isfile(majors):
    print(f"'{majors}' is being read....")
    with open(majors, "r") as myFile:
        while 1:
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
        myFile.close()
print(contents)
contentsListed = contents.split(" ,",)
print(contentsListed)
print()

# This little snippet is from my Senior Project -- Alexander Garofalo
# BEGINNING OF SNIPPET
if os.path.isfile(majorsSorted):
    print(f"'{majorsSorted}' exists and has been marked for deletion...")
    os.remove(majorsSorted)
else:
    print(f"Error!! '{majorsSorted}' was not found.")
# END OF SNIPPET

for i in range(len(contentsListed)):
    with open(majorsSorted, "a") as myFile:
        myFile.write(f"{contentsListed[i]}\n")

myFile.close()
