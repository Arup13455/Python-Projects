'''#attendence sheet maker
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class AttendanceSheet:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance Sheet Maker")

        # Title label
        tk.Label(root, text="Attendance Sheet", font=("Arial", 18)).grid(row=0, column=0, columnspan=3, pady=10)

        # Date input
        tk.Label(root, text="Date (DD-MM-YYYY):").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.date_entry = tk.Entry(root)
        self.date_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        # Students' names
        self.students = ["Alice", "Bob", "Charlie", "David", "Eve"]

        # Create labels and dropdowns for each student
        self.attendance = {}
        for i, student in enumerate(self.students):
            tk.Label(root, text=student).grid(row=i+2, column=0, padx=10, pady=5, sticky=tk.W)
            self.attendance[student] = tk.StringVar()
            self.attendance[student].set("No")  # Default value is "No"
            ttk.Combobox(root, textvariable=self.attendance[student], values=["Yes", "No"], state="readonly").grid(row=i+2, column=1, padx=10, pady=5)

        # Submit button
        tk.Button(root, text="Submit", command=self.submit).grid(row=len(self.students)+2, column=0, columnspan=3, pady=10)

    def submit(self):
        date = self.date_entry.get()
        if not date:
            messagebox.showwarning("Input Error", "Please enter a date.")
            return

        attendance_results = f"Attendance for {date}:\n"
        for student, status in self.attendance.items():
            attendance_results += f"{student}: {status.get()}\n"
        attendance_results += "\n"  # Add a newline after each record

        # Save attendance to a file
        with open("attendance_records.txt", "a") as file:
            file.write(attendance_results)

        messagebox.showinfo("Attendance Submitted", "Attendance has been recorded successfully!")
        self.clear_form()

    def clear_form(self):
        self.date_entry.delete(0, tk.END)
        for student in self.students:
            self.attendance[student].set("No")  # Reset all dropdowns to "No"

if __name__ == "__main__":
    root = tk.Tk()
    app = AttendanceSheet(root)
    root.mainloop()'''
from datetime import datetime

class Attendance:
    def __init__(self):
        self.records = {}  # Initialize the records dictionary

    def add_attendance(self, name, present):
        if name not in self.records:
            self.records[name] = {'present': 0, 'total': 0}

        if present.lower() == 'y':
            self.records[name]['present'] += 1
        self.records[name]['total'] += 1

    def save_attendance_to_file(self, date):
        print("\nSaving attendance data to file...")
        with open("attendance.txt", "a") as f:
            f.write(f"\nDate: {date}\n")
            for name, data in self.records.items():
                total_present = data['present']
                total_days = data['total']
                percentage = (total_present / total_days) * 100 if total_days > 0 else 0
                eligible = "Eligible" if percentage >= 75 else "Not Eligible"
                result = f"Student: {name}, Attendance: {percentage:.2f}%, Status: {eligible}"
                print(result)
                f.write(result + "\n")

    def check_student_attendance(self, name):
        if name in self.records:
            total_present = self.records[name]['present']
            total_days = self.records[name]['total']
            percentage = (total_present / total_days) * 100 if total_days > 0 else 0
            eligible = "Eligible" if percentage >= 75 else "Not Eligible"
            print(f"Student: {name}, Attendance: {percentage:.2f}%, Status: {eligible}")
        else:
            print(f"No record found for student: {name}")

# Main function to handle the attendance taking process
def main():
    attendance = Attendance()
    
    # Input the date for attendance
    date = input("Enter the date for attendance (YYYY-MM-DD): ")
    try:
        datetime.strptime(date, "%Y-%m-%d")  # Validate date format
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    
    print("\nEnter all student names (type 'done' when finished):")
    
    # Input all student names at the beginning
    while True:
        name = input("Enter student name: ")
        if name.lower() == 'done':
            break
        attendance.records[name] = {'present': 0, 'total': 0}

    print("\n--- Start taking attendance ---")
    for name in attendance.records.keys():
        present = input(f"Is {name} present? (Y/N): ")
        attendance.add_attendance(name, present)
    
    # Save attendance data to file
    attendance.save_attendance_to_file(date)
    print("\nAttendance report saved in 'attendance.txt'")
    
    # Check a student's overall attendance by name
    while True:
        check_name = input("\nEnter a student's name to check overall attendance (or type 'exit' to stop): ")
        if check_name.lower() == 'exit':
            break
        attendance.check_student_attendance(check_name)

if __name__ == "__main__":
   main()