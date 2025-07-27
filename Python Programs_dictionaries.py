# Write a program that creates a dictionary containing course numbers and the room numbers of the rooms where the courses meet.The program should let the user enter a course number and then it should display the course's room number, instructor, and meeting time.

# Dictionary Creation: Course as key, room number, instructor, and time as values pairs.
courses = {
    "CSC101": {"room": 3004, "instructor": "Haynes", "time": "8:00 a.m."},
    "CSC102": {"room": 4501, "instructor": "Alvarado", "time": "9:00 a.m."},
    "CSC103": {"room": 6755, "instructor": "Rich", "time": "10:00 a.m."},
    "NET110": {"room": 1244, "instructor": "Burke", "time": "11:00 a.m."},
    "COM241": {"room": 1411, "instructor": "Lee", "time": "1:00 p.m."}
}

query = input("Enter course number or instructor last name: ").strip().lower()

# Direct course search
if query in courses:
    details = courses[query]
    print(f"{query}: Room {details['room']}, {details['instructor']}, {details['time']}")
else:
    # Search by instructor
    found = False
    for course, details in courses.items():
        if details["instructor"].lower() == query.lower():
            print(f"{course}: Room {details['room']}, {details['instructor']}, {details['time']}")
            found = True
    if not found:
        print("No course or instructor found.")