import time

while True:
    time.sleep(1)
    time_to_edit = open('time-to-edit.txt', 'r')
    is_it_time = time_to_edit.read()
    is_it_time = str(is_it_time)
    time_to_edit.close()

    if is_it_time == "time":
        # import manuscript number
        manuscript = open('manuscript-service.txt', 'r')
        manuscript_file_name = manuscript.readline()
        manuscript.close()

        # import line number
        line = open('line-number.txt', 'r')
        line_number = line.readline()
        line_number = int(line_number)
        line.close()

        # import edit option
        edit = open('edit-line.txt', 'r')
        edit_option = edit.readline()
        edit.close()

        manuscript_file = f"manuscript/{manuscript_file_name}"

        with open(manuscript_file, 'r') as manuscript:
            manuscript_lines = manuscript.readlines()
            line_index = 0
            line_number -= 1

            manuscript.close()

            with open(manuscript_file, 'w') as manuscript:
                edit_integer = edit_option
                edit_integer = int(edit_integer)
                for line in manuscript_lines:
                    # ADD
                    if edit_integer == 1:
                        if line_number == line_index:
                            manuscript_lines.insert(line_number + 1, ' \n')
                        line_index += 1

                    # REMOVE
                    if edit_integer == 2:
                        if line_number != line_index:
                            manuscript.write(line)
                            line_index += 1
                        else:
                            line_index += 1

                    # REPLACE
                    if edit_integer == 3:
                        replace_file = open("replace.txt", "r")
                        replace = replace_file.read()
                        replace_file.close()
                        if line_number == line_index:
                            manuscript_lines[line_number] = (replace + '\n')
                        line_index += 1

                    # NOTE
                    if edit_integer == 4:
                        note_file = open("note.txt", "r")
                        note = note_file.read()
                        note_file.close()
                        if line_number == line_index:
                            new_line = line.translate({ ord("\n"): None})
                            manuscript_lines[line_number] = f"{new_line} [{note}] \n"
                        line_index += 1

                manuscript.close()

        if edit_integer != 2:
            with open(manuscript_file, 'w') as manuscript:
                for x in manuscript_lines:
                    manuscript.write(x)

        time_to_edit = open('time-to-edit.txt', 'w')
        time_to_edit.truncate()
        time_to_edit.seek(0)
        time_to_edit.close()
