# --- 1. Dataset of Student Records ---
students_db = [
    {"id": "e20241154", "name": "Chhean Ravy", "score": 92.5},
    {"id": "e20241155", "name": "Sreyneath Kol", "score": 88.0},
    {"id": "e20241156", "name": "Heng Piseth", "score": 45.0},  # Failing score
    {"id": "e20241157", "name": "Vatey Chan", "score": 95.5}
]

# --- 2. Using a 'for' Loop & 'continue' to Calculate Average (Skipping Failures) ---
total_score = 0
valid_count = 0

print("--- Calculating Average Score (Passing Students Only) ---")
for student in students_db:
    if student["score"] < 50:
        print(f"Skipping {student['name']} (Score below passing threshold).")
        continue  # Skip current iteration if student failed
    
    total_score += student["score"]
    valid_count += 1

average_score = total_score / valid_count if valid_count > 0 else 0
print(f"Class Average (Passing): {average_score:.2f}\n")


# --- 3. Using a 'for' Loop & 'break' to Search for a Specific Student ---
target_id = "e20241155"
found_student = None

print(f"--- Searching Database for ID: {target_id} ---")
for student in students_db:
    if student["id"] == target_id:
        found_student = student
        break  # Terminate loop immediately once target is found

if found_student:
    print(f"Match Found! Name: {found_student['name']} | Score: {found_student['score']}\n")
else:
    print("Student ID not found in database.\n")


# --- 4. Replicating 'do-while' Behavior in Python using 'while True' ---
print("--- Interactive Retry Loop (Simulating do-while) ---")
attempt_count = 0

while True:
    attempt_count += 1
    print(f"Connection attempt #{attempt_count}...")
    
    # Simulate successful connection on attempt 2
    if attempt_count >= 2:
        print("Connection established successfully!")
        break  # Exit the infinite loop