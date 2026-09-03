# Student Data Management System Using Python Collections 
# Write a Python Program to create and storestudent information using Disctionary, Tuples and List. Perform the following operations on the Dictionary:
# 1. Add a new student record
# 2. Delete an existing student record
# 3. Update the details of a student
# 4. Display the final student records after performing the above operations. 
# Use suitable student attributes such as : Roll Number, Name, Branch, and Marks.

data_file = "student_records.txt"

# Default empty record
student_records = {"Roll Number": "", "Name": "", "Branch": "", "Marks": ""}

while True:
    # Read existing data from file into RAM
    # a+ append and read mode (and then saves it to students_records), creates the file if it doesn't exist 
    file = open(data_file, "a+")
    # Move the file pointer to the beginning of the file to read existing data
    file.seek(0)
    # Read all lines from the file saves from SSD to RAM
    lines = file.read().splitlines()
    # Close the file after reading required as python store the data in buffer and if we don't close it, it will not save the data to the file
    file.close()

    # If data exists in file, update dictionary
    if len(lines) >= 4:
        student_records["Roll Number"] = lines[0]
        student_records["Name"] = lines[1]
        student_records["Branch"] = lines[2]
        student_records["Marks"] = lines[3]

    print("\n--- STUDENT RECORD MANAGEMENT ---")
    command = input("Enter command (add, delete, update): ").strip().lower()

    if command == "add":
        student_records["Roll Number"] = input("Enter Roll Number: ")
        student_records["Name"] = input("Enter Name: ")
        student_records["Branch"] = input("Enter Branch: ")
        student_records["Marks"] = input("Enter Marks: ")

        # Save to file
        # w write mode (overwrites the file with new data)
        file = open(data_file, "w")
        file.write(student_records["Roll Number"] + "\n")
        file.write(student_records["Name"] + "\n")
        file.write(student_records["Branch"] + "\n")
        file.write(student_records["Marks"] + "\n")
        file.close()

        print("Record added successfully!")

    elif command == "delete":
        roll = input("Enter Roll Number to delete: ")
        if student_records["Roll Number"] == roll:
            student_records["Roll Number"] = ""
            student_records["Name"] = ""
            student_records["Branch"] = ""
            student_records["Marks"] = ""

            file = open(data_file, "w")
            file.write("\n\n\n\n")
            file.close()

            print("Record deleted successfully!")
        else:
            print("Roll number not found.")

    elif command == "update":
        roll = input("Enter Roll Number to update: ")
        if student_records["Roll Number"] == roll:
            student_records["Name"] = input("Enter new Name: ")
            student_records["Branch"] = input("Enter new Branch: ")
            student_records["Marks"] = input("Enter new Marks: ")

            file = open(data_file, "w")
            file.write(student_records["Roll Number"] + "\n")
            file.write(student_records["Name"] + "\n")
            file.write(student_records["Branch"] + "\n")
            file.write(student_records["Marks"] + "\n")
            file.close()

            print("Record updated successfully!")
        else:
            print("Roll number not found.")

    else:
        print("Invalid command!")

    # Display current record at the end of operation
    print("\nCurrent Record in Memory:")
    print(student_records)

    # Ask user to continue or exit
    choice = input("\nDo you want to continue? (yes/no): ").strip().lower()
    if choice != "yes":
        print("Exiting program.")
        break