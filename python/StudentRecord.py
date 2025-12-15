'''
This program will store students' ID and courses.
Author: Lauren White
Assignment: Lab 7
Date: 11/19/24
'''
# Asks user for student ID and courses
def student_record(all_students):
    # Gets the student's ID
    while (True):
        student_info = list()
        student_id = input("Enter a new student ID number: ")
        if (student_id.lower() == "done"):
            break
        elif (student_id.lower() == "new student"):
            continue
        student_info.append(int(student_id))
        # Lets users enter as many courses as they want
        while (True):
            courses = input("Enter course name: ")
            if (courses.lower() == "new student"):
                all_students.append(student_info)
                break
            elif (courses.lower() == "done"):
                all_students.append(student_info)
                break
            else:
                student_info.append(courses)
        if (courses.lower() == "done"):
            break

# Stores and prints student records
def main():
    student_data = list()
    print("Enter 'done' to exit. Enter 'new student' to start a new data list.")
    student_record(student_data)
    print("Student info:", student_data)
   
# Output 
if __name__ == '__main__':
    main()
