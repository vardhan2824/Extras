def main():
    semesters = 8
    completed_data = []  # Stores (credits, sgpa) for completed semesters
    remaining_credits = []  # Credits for upcoming semesters

    # Input completed semesters
    print("=== Enter COMPLETED Semesters (Credits and SGPA) ===")
    for sem in range(1, semesters + 1):
        choice = input(f"\nAdd Semester {sem} data? (y/n): ").lower()
        if choice != 'y':
            break
        credits = float(input(f"  - Credits for Semester {sem}: "))
        sgpa = float(input(f"  - SGPA for Semester {sem}: "))
        completed_data.append((credits, sgpa))

    # Calculate current CGPA
    total_credits = sum(credits for credits, _ in completed_data)
    total_grade_points = sum(credits * sgpa for credits, sgpa in completed_data)
    current_cgpa = total_grade_points / total_credits if total_credits > 0 else 0
    print(f"\nCurrent CGPA after {len(completed_data)} semesters: {current_cgpa:.2f}")

    # Input remaining semesters' credits and target CGPA
    remaining_sems = semesters - len(completed_data)
    if remaining_sems > 0:
        print("\n=== Enter UPCOMING Semesters' Credits ===")
        for sem in range(len(completed_data) + 1, semesters + 1):
            credits = float(input(f"  - Credits for Semester {sem}: "))
            remaining_credits.append(credits)

        target_cgpa = float(input("\nEnter TARGET CGPA: "))

        # Calculate required future SGPA
        total_future_credits = sum(remaining_credits)
        required_grade_points = (target_cgpa * (total_credits + total_future_credits)) - total_grade_points
        required_sgpa = required_grade_points / total_future_credits

        print(f"\nTo achieve a CGPA of {target_cgpa:.2f}:")
        print(f"  - You need an average SGPA of **{required_sgpa:.2f}** in the next {remaining_sems} semesters.")
    else:
        print("\nAll 8 semesters completed! Final CGPA:", current_cgpa)

if __name__ == "__main__":
    main()
