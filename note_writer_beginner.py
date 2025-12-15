from datetime import datetime
import os

TODAY = datetime.now()
FILEPATH = "Notes"

# Create an empty list to store all notes
notes = []

# Start main loop
print("Enter your notes (type 'done' when finished):\n")
while True:
    note = input("Note: ")

    # Check if user wants to finish
    if note.lower() == "done":
        break

    # Add the note to list
    notes.append(note)

if len(notes) > 0:
    if not os.path.exists(FILEPATH):
        os.makedirs(FILEPATH)

    # Create filename with today's date
    filename = f"Notes/notes_{TODAY.year}-{TODAY.month:02d}-{TODAY.day:02d}.txt"


    print("\nWriting notes to file....")

    with open(filename, "w") as file:
        for note in notes:
            file.write(note + "\n")

    print(f"File Saved: {filename}\n")
    print("Notes saved successfully!")
    print(f"Total notes written: {len(notes)}")
else:
    print("\nNo notes to save. Exiting...")