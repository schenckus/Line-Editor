import time
import os
import glob

print("\n               Welcome to Line Editor: easily edit a line on an existing manuscript. \n"
      "                              Just follow the prompts below. \n "
      "\n ")

# Creates a list with all of the txt files in the manuscript folder. Add as many, as little as you need. All you need
# to do is replace my directory path with yours once everything has been downloaded to your machine.
directory = r'C:/Users/schen/OneDrive/Desktop/microservice/manuscript'
files_dir = os.listdir(directory)
manuscript_list = []
for names in files_dir:
    if names.endswith(".txt"):
        names_without_txt = names[:-(names.endswith('.txt') and len('.txt'))]
        manuscript_list.append(names_without_txt)

while True:
    time.sleep(1)
    value = input("Please enter the name of the manuscript you wish to edit or 0 if you wish to exit: ")

    if f'{value}' in manuscript_list:
        # write manuscript # to manuscript txt file
        number = value
        number = str(number)
        manuscript = open('manuscript-service.txt', 'w')
        manuscript.write(number)
        manuscript.close()

        # user enters line number and writes # to line-number txt file
        print(f"Manuscript file name {value} is now open. \n \n")
        line_number = input("Please enter what line number you would like to edit: ")
        line = open('line-number.txt', 'w')
        line.write(line_number)
        line.close()

        print("\n \nHow would you like to edit this line?")
        print("1 = ADD || 2 = REMOVE || 3 = REPLACE  || 4 = NOTE")

        # user enters edit options and writes # to edit txt file
        instruction = input("\n \nEnter option 1-4 here: ")
        edit = open('edit-line.txt', 'w')
        edit.write(instruction)
        edit.close()

        # turn some variables into integers
        line_number = int(line_number)
        instruction = int(instruction)

        # ADD
        if instruction == 1:
            time_to_edit = open('time-to-edit.txt', 'w')
            time_to_edit.write("time")
            time_to_edit.close()
            print(f"\n \nA new line has been added below line number {line_number}")

        # REMOVE
        if instruction == 2:
            time_to_edit = open('time-to-edit.txt', 'w')
            time_to_edit.write("time")
            time_to_edit.close()
            time.sleep(5)
            print(f"\n \nLine {line_number} has been removed successfully!")

        # REPLACE
        if instruction == 3:
            replace = input("\n \nPlease enter what you would like to replace this line with: ")
            replace_file = open('replace.txt', 'w')
            replace_file.write(replace)
            replace_file.close()

            time_to_edit = open('time-to-edit.txt', 'w')
            time_to_edit.write("time")
            time_to_edit.close()

            time.sleep(10)

            print(f"\n \nYou have successfully replaced line number {line_number} with the following: ")
            print(replace)

        # ADD NOTE
        if instruction == 4:
            note = input("\n \nPlease enter what note you would like to add: ")
            note_file = open('note.txt', 'w')
            note_file.write(note)
            note_file.close()

            time_to_edit = open('time-to-edit.txt', 'w')
            time_to_edit.write("time")
            time_to_edit.close()

            time.sleep(10)

            print(f"\n \nYou have successfully added note to line number {line_number} with the following: ")

        time.sleep(2)

        # This prints out the WHOLE manuscript. You can delete, especially if the manuscripts you are going to use are
        # long. This is handy for testing or for short manuscripts.
        manuscript = open(f"manuscript/{number}", 'r')
        print("Here is the updated manuscript:")
        for line in manuscript:
            print(line)

    elif value == 0:
        print("You have successfully closed Line Editor. Thank you and have a good day!")
        break

    else:
        print("Invalid manuscript file name.")
