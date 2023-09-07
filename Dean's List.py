""" Brent Lewis
    Dean's List or Honor Roll app
    Enter student's name and GPA to determine if they made the Dean's List, Honor Roll, or neither. """
def main()
    while True:
        last_name = input("Enter student's last name (or 'ZZZ' to quit):")
        if last_name == 'ZZZ':
            break

        first_name = input("Enter student's first name: ")
        gpa = float(input("Enter student's GPA: "))

        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List.")
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll.")
        else:
            print(f"{first_name} {last_name} does not qualify for Dean's List or Honor Roll.")

# Test the app with 5 students
for _ in range(5):
    main()
https://github.com/blewis238/M02-Lab/upload