import csv
import os
from datetime import datetime

FILE_NAME = "issues_log.csv"

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Issue ID", "User", "Issue Type", "System", "Status", "Logged Time"])

def log_issue():
    issue_id = input("Enter Issue ID: ")
    user = input("Enter User Name: ")
    issue_type = input("Enter Issue Type (Software/Hardware/Network/Printer): ")
    system = input("Enter System Name/ID: ")
    status = "Open"
    logged_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([issue_id, user, issue_type, system, status, logged_time])

    print("✅ Issue Logged Successfully!")

def view_issues():
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def resolve_issue():
    issue_id = input("Enter Issue ID to Resolve: ")
    rows = []

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    for row in rows:
        if row and row[0] == issue_id:
            row[4] = "Resolved"
            print("✅ Issue Marked as Resolved!")

    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

def main_menu():
    initialize_file()

    while True:
        print("\n===== IT HELP DESK & DESKTOP SUPPORT SIMULATION =====")
        print("1. Log New Issue")
        print("2. View All Issues")
        print("3. Mark Issue as Resolved")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            log_issue()
        elif choice == "2":
            view_issues()
        elif choice == "3":
            resolve_issue()
        elif choice == "4":
            print("Exiting Helpdesk System.")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
