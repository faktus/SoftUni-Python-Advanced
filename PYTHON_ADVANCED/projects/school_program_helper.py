# Define the school week schedule (Monday to Friday, 8:00 AM to 2:00 PM)
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
start_time = 800  # 8:00 AM represented as an integer (800)
end_time = 1400  # 2:00 PM represented as an integer (1400)
class_duration = 40  # Duration of each class in minutes

# Initialize the schedule dictionary
schedule = {day: {} for day in days_of_week}

# Predefined list of subjects with some subjects appearing twice
subjects = [
    "Math", "English", "Science", "History", "Art",
    "Music", "Physical Education", "Geography", "Computer Science", "Spanish",
    "French", "Biology", "Chemistry", "Physics", "Literature",
    "Social Studies", "Economics", "Psychology", "Sociology", "Government",
    "Physical Education", "Computer Science", "Art", "Social Studies", "Spanish"
]

# Initialize a teacher-subject assignment list
teacher_subject_assignments = []

# Input teacher-subject assignments
for i in range(len(subjects)):
    teacher = input(f"Enter the teacher's name for {subjects[i]}: ")
    teacher_subject_assignments.append({"Teacher": teacher, "Subject": subjects[i]})

# Shuffle the teacher-subject assignments to randomize
import random
random.shuffle(teacher_subject_assignments)

# Generate the schedule based on teacher-subject assignments
current_time = start_time

for day in days_of_week:
    current_time = start_time  # Reset time for each day
    for _ in range(len(teacher_subject_assignments)):
        if current_time >= end_time:
            break

        assignment = teacher_subject_assignments.pop(0)
        teacher = assignment["Teacher"]
        subject = assignment["Subject"]

        if day not in schedule:
            schedule[day] = {}

        # Calculate hours and minutes for the time slot
        hours = current_time // 100
        minutes = current_time % 100
        end_time_minutes = minutes + class_duration

        # Adjust the end time if it goes beyond 60 minutes
        if end_time_minutes >= 60:
            hours += 1
            end_time_minutes -= 60

        end_hours = hours
        end_minutes = end_time_minutes

        time_slot = f"{hours:02d}:{minutes:02d} - {end_hours:02d}:{end_minutes:02d}"
        if time_slot not in schedule[day]:
            schedule[day][time_slot] = []

        schedule[day][time_slot].append({"Teacher": teacher, "Subject": subject})
        current_time = end_hours * 100 + end_minutes

# Print the final program
for day, slots in schedule.items():
    print(f"\n{day}:")
    for time, assignments in slots.items():
        assignments_info = [f"{assignment['Subject']} ({assignment['Teacher']})" for assignment in assignments]
        print(f"{time}: {', '.join(assignments_info)}")
