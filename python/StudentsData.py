'''
This program will let you create a record of different students and search through it.
Author: Lauren White
Assignement: Lab 8
Date: 11/21/24
'''
# Global list to use with multiple functions
records = list()

# Adds student record data to records list
def add_student_record(student_data):
    records.append(student_data.strip().split(';'))
    
# Prints all data from records list
def print_all():
    print("All student records:")
    for record in records:
        print (record)

# Lets the user find something within records list
def find(student_id):
    for record in records:
        if(student_id in record):
            return True
            
    return False

# Holds all other function calls and output
def main():
    while True:
        student_data = input("Enter a student's ID and info. Enter 'done' when finished. End separate pieces of data with ';': ")
        if student_data.lower() == "done":
            break
        add_student_record(student_data)
    student_id = input("Enter the student ID you're looking for: ")

    # Checks if student ID is in the system
    if(find(student_id)):
        print("Student record found")
    else:
        print("Student record not found.")

    # Prints all records
    print_all()
    
# Output
if __name__ == '__main__':
    main()