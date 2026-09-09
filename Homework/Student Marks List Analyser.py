import sys

def get_int_input(prompt, min_val=None, max_val=None):
    """Safely get an integer input with optional range validation."""
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Value must be at least {min_val}. Try again.")
                continue
            if max_val is not None and value > max_val:
                print(f"Value must be at most {max_val}. Try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    print("\n=== Student Marks Analyzer ===\n")
    num_students = get_int_input("Enter number of students: ", min_val=1)
    num_subjects = get_int_input("Enter number of subjects: ", min_val=1)
    subjects = []
    for i in range(num_subjects):
        subject_name = input(f"Enter name of subject {i+1}: ").strip()
        if not subject_name:
            subject_name = f"Subject{i+1}"
        subjects.append(subject_name)
    students = []
    for s in range(num_students):
        print(f"\n--- Enter details for Student {s+1} ---")
        name = input("Enter student name: ").strip()
        marks = []
        for subj in subjects:
            mark = get_int_input(f"Enter marks for {subj} (0-100): ", 0, 100)
            marks.append(mark)
        students.append({"name": name, "marks": marks})
    print("\n=== Student Marks Report ===")
    header = ["Name"] + subjects + ["Total", "Average", "Status"]
    print("-" * (len(header) * 12))
    print("{:<15}".format(header[0]), end="")
    for h in header[1:]:
        print("{:<12}".format(h), end="")
    print()
    
    print("-" * (len(header) * 12))

    for student in students:
        total = sum(student["marks"])
        avg = total / num_subjects
        status = "PASS" if all(m >= 40 for m in student["marks"]) else "FAIL"

        print("{:<15}".format(student["name"]), end="")
        for m in student["marks"]:
            print("{:<12}".format(m), end="")
        print("{:<12}".format(total), end="")
        print("{:<12.2f}".format(avg), end="")
        print("{:<12}".format(status))
    print("-" * (len(header) * 12))
    all_marks = [m for student in students for m in student["marks"]]
    print("\n=== Class Statistics ===")
    print(f"Highest Mark: {max(all_marks)}")
    print(f"Lowest Mark : {min(all_marks)}")
    print(f"Class Average: {sum(all_marks) / len(all_marks):.2f}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        sys.exit(0)
