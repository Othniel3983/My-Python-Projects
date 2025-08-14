import json
import os
from datetime import date


ATTENDANCE_FILE = "attendance.json"

def load_attendance():
    global present_students_today, absent_students_today, my_class_students
    if os.path.exists(ATTENDANCE_FILE):
        with open(ATTENDANCE_FILE, "r") as f:
            data = json.load(f)
            # Load existing students if they exist
            if "students" in data:
                my_class_students.extend(data["students"])
            return data
    return {}

def save_attendance(attendance_data):
    with open(ATTENDANCE_FILE, "w") as f:
        json.dump(attendance_data, f, indent=4)

my_class_students = []
present_students_today = []
absent_students_today = []

def add_name(attendance_data):
    while True:
        enter_name = input("\nDo you want to add a student's name? (Yes/No): ").strip().lower()
        if enter_name == 'yes':
            name = input("\nEnter student name: ")
            my_class_students.append(name)
            print(f"Added {name} to the class list.")
        elif enter_name == 'no':
            print("Thank You")
            break
        else:
            print("Invalid option! Please enter Yes or No")

    # Save the updated student list to attendance_data
    attendance_data["students"] = my_class_students
    save_attendance(attendance_data)
    print(f"\nCurrent students: {my_class_students}")


def mark_attendance(attendance_data):
    today = str(date.today())
    global present_students_today, absent_students_today
    present_students_today = []
    absent_students_today = []

    print(f"\nMarking attendance for {today}")
    for student in my_class_students:
        while True:
            status = input(f"{student}, (P/A): ").lower().strip()
            if status == 'p':
                present_students_today.append(student)
                break
            elif status == 'a':
                absent_students_today.append(student)
                break
            else:
                print("Invalid input. Please enter 'P' for present and 'A' for absent")
    
    attendance_data[today] = {
        "present": present_students_today,
        "absent": absent_students_today
    }
    
    save_attendance(attendance_data)
    print("\nAttendance marked successfully.\n")


def view_attendance(attendance_data):
    print("\n--Today's Attendance--")

    if not attendance_data:
        print("No attendance data found.")
        return
    
    print("\nDates with attendance records:")
    for day in attendance_data:
        print(f" - {day}")
    
    selected_day = input("\nEnter data to view (YYYY-MM-DD): ").strip()

    if selected_day in attendance_data:
        day_data = attendance_data[selected_day]
        
        print(f"\n--- Attendance for {selected_day} ---")
        
        print("\nPresent Students:")
        for student in day_data["present"]:
            print(student)
        
        print("\nAbsent Students:")
        for student in day_data["absent"]:
            print(student)
    
    else:
        print("No attendance found for that date. \n")

def run_attendance_app():
    attendance_data = load_attendance()
    print("Welcome to the attendance app!")

    while True:
        print("\nPlease choose an option")

        print("1. Add Name")
        print("2. Mark Attendance")
        print("3. View Attendance")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == '1':
            add_name(attendance_data)
        elif choice == '2':
            mark_attendance(attendance_data)
        elif choice == '3':
            view_attendance(attendance_data)
        elif choice == '4':
            print("\nGoodbye. Have a great day!")
            break
        else:
            print("Invalid choice. Please try again!")

run_attendance_app()

