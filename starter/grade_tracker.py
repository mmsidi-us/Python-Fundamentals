import csv

def load_students(filepath):
    """
    Reads the CSV file and returns a list of dictionaries.
    Handles FileNotFoundError gracefully by returning an empty list.
    """
    students_list = []
    try:
        with open(filepath, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students_list.append(row)
        return students_list
    except FileNotFoundError:
        print(f"\n❌ Error: The file at '{filepath}' was not found.")
        return []

def calculate_average(grades):
    """
    Takes a list of grade values (as strings), filters out empty strings,
    and returns the rounded average float. Returns None if no valid grades exist.
    """
    valid_grades = []
    for g in grades:
        if g is not None and g.strip() != "":
            try:
                valid_grades.append(float(g))
            except ValueError:
                continue  # Skip any non-numeric strings safely
                
    if not valid_grades:
        return None
        
    return round(sum(valid_grades) / len(valid_grades), 1)

def get_letter_grade(average):
    """
    Converts a numeric average into a letter grade based on fixed boundaries.
    """
    if average is None:
        return "N/A"
    elif average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def generate_report(students):
    """
    Takes the full student list and returns a comprehensive summary dictionary,
    calculating class metrics, tracking grade distributions, and compiling student arrays.
    """
    total_students = len(students)
    student_results = []
    
    # Grade distribution template counter
    distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0, "N/A": 0}
    
    valid_averages = []
    
    for s in students:
        name = s.get("student_name")
        # Collect subject scores across columns
        subject_scores = [s.get("math"), s.get("science"), s.get("english"), s.get("history")]
        
        avg = calculate_average(subject_scores)
        letter = get_letter_grade(avg)
        
        # Increment distribution map
        distribution[letter] += 1
        
        if avg is not None:
            valid_averages.append(avg)
            
        student_results.append({
            "name": name,
            "average": avg,
            "letter_grade": letter
        })
        
    # Class stats calculation
    class_avg = round(sum(valid_averages) / len(valid_averages), 1) if valid_averages else 0.0
    highest_avg = max(valid_averages) if valid_averages else 0.0
    lowest_avg = min(valid_averages) if valid_averages else 0.0
    
    return {
        "total_students": total_students,
        "class_average": class_avg,
        "highest_average": highest_avg,
        "lowest_average": lowest_avg,
        "grade_distribution": distribution,
        "student_results": student_results
    }

def write_report(report, filepath):
    """
    Writes a polished, clean-text format report containing class metrics,
    grade distribution breakdowns, and individual lists to grade_report.txt.
    """
    with open(filepath, mode="w", encoding="utf-8") as file:
        file.write("==================================================\n")
        file.write("           CLASS ACADEMIC PERFORMANCE REPORT      \n")
        file.write("==================================================\n\n")
        
        file.write("--- Class Overview Statistics ---\n")
        file.write(f"Total Logged Students:  {report['total_students']}\n")
        file.write(f"Overall Class Average:  {report['class_average']:.1f}\n")
        file.write(f"Highest Student Score:  {report['highest_average']:.1f}\n")
        file.write(f"Lowest Student Score:   {report['lowest_average']:.1f}\n\n")
        
        file.write("--- Letter Grade Breakdown Distribution ---\n")
        for grade, count in report['grade_distribution'].items():
            file.write(f"  {grade}: {count}\n")
        file.write("\n")
        
        file.write("--- Individual Roster Student Performance Results ---\n")
        file.write("-" * 55 + "\n")
        file.write(f"{'Student Name':<25}{'Average':<15}{'Letter Grade':<15}\n")
        file.write("-" * 55 + "\n")
        
        for item in report['student_results']:
            avg_str = f"{item['average']:.1f}" if item['average'] is not None else "N/A"
            file.write(f"{item['name']:<25}{avg_str:<15}{item['letter_grade']:<15}\n")
        file.write("-" * 55 + "\n")

def main():
    """
    Main program flow logic execution engine.
    Controls reading pipeline, console routing layout, and text storage export calls.
    """
    input_file = "starter/data/students.csv"
    output_file = "starter/grade_report.txt"
    
    print("Loading student data...")
    students = load_students(input_file)
    if not students:
        print("Pipeline aborted: No data entries discovered.")
        return
        
    print(f"  Loaded {len(students)} students.\n")
    print("Generating report...\n")
    
    report = generate_report(students)
    
    # 1. Print terminal command summary dashboard
    print("--- Summary ---")
    print(f"Total students:   {report['total_students']}")
    print(f"Class average:    {report['class_average']:.1f}")
    print(f"Highest average:  {report['highest_average']:.1f}")
    print(f"Lowest average:   {report['lowest_average']:.1f}\n")
    
    print("Grade Distribution:")
    for letter, count in report['grade_distribution'].items():
        print(f"  {letter}: {count}")
    print()
    
    # Isolate valid numerical entities and sort them downwards to identify top 5 records
    valid_sorted = [s for s in report['student_results'] if s['average'] is not None]
    valid_sorted.sort(key=lambda x: x['average'], reverse=True)
    
    print("Top 5 students:")
    for item in valid_sorted[:5]:
        print(f"  {item['name']:<25}{item['average']:.1f}  ({item['letter_grade']})")
    print()
    
    # 2. Write file report down to target disk file path
    write_report(report, output_file)
    print(f"Report written to {output_file}")

if __name__ == "__main__":
    main()