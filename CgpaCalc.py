def calculate_sgpa():
    print("\n--- SGPA Calculator ---")
    num_subjects = int(input("Enter number of subjects: "))
    total_credits = 0
    total_grade_points = 0

    for i in range(num_subjects):
        credit = float(input(f"Enter credits for subject {i+1}: "))
        grade = float(input(f"Enter grade (out of 10) for subject {i+1}: "))
        total_credits += credit
        total_grade_points += credit * grade

    sgpa = total_grade_points / total_credits
    print(f"\nSGPA = {sgpa:.2f}")
    return sgpa, total_credits

def calculate_cgpa(semester_data):
    total_credits = sum(credits for _, credits in semester_data)
    total_grade_points = sum(sgpa * credits for sgpa, credits in semester_data)
    cgpa = total_grade_points / total_credits
    return cgpa

def predict_future_grades(semester_data, target_cgpa, remaining_credits):
    total_credits = sum(credits for _, credits in semester_data)
    total_grade_points = sum(sgpa * credits for sgpa, credits in semester_data)
    required_grade_points = (target_cgpa * (total_credits + remaining_credits)) - total_grade_points
    required_avg = required_grade_points / remaining_credits
    return required_avg

def main():
    semester_data = []
    total_semesters = 8

    for sem in range(1, total_semesters + 1):
        print(f"\n--- Semester {sem} ---")
        choice = input("Calculate SGPA for this semester? (y/n): ").lower()
        if choice == 'y':
            sgpa, credits = calculate_sgpa()
            semester_data.append((sgpa, credits))
            cgpa = calculate_cgpa(semester_data)
            print(f"Current CGPA after Semester {sem}: {cgpa:.2f}")
        else:
            remaining_semesters = total_semesters - sem + 1
            remaining_credits = sum(float(input(f"Enter credits for Semester {sem + i}: ")) for i in range(remaining_semesters))
            target_cgpa = float(input("\nEnter Target CGPA: "))
            required_avg = predict_future_grades(semester_data, target_cgpa, remaining_credits)
            print(f"\nYou need an average of **{required_avg:.2f}** in the next {remaining_semesters} semesters to achieve a CGPA of {target_cgpa:.2f}.")
            break

if __name__ == "__main__":
    main()
