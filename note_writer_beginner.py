from datetime import datetime
import os

# Constants
TODAY = datetime.now()
FILEPATH = "Notes"


def collect_notes():
    """Collect notes from user until they type 'done'"""
    # Create an empty list to store all notes
    notes = []

    # Start main loop
    print("\nEnter your notes (type 'done' when finished):")

    while True:
        note = input("\nNote: ")

        # Check if user wants to finish
        if note.lower() == "done":
            break

        # Add the note to list
        notes.append(note)

    return notes


def get_filename():
    """Generate filename based on today's date"""
    # Check Notes folder exists
    if not os.path.exists(FILEPATH):
        os.makedirs(FILEPATH)

    # Create filename with today's date
    filename = f"Notes/notes_{TODAY.year}-{TODAY.month:02d}-{TODAY.day:02d}.txt"

    return filename


def save_notes(notes, filename):
    """Save notes to a file"""
    print("\nWriting notes to file....")

    with open(filename, "w") as file:
        for note in notes:
            file.write(note + "\n")

    print(f"File Saved: {filename}\n")
    print("Notes saved successfully!")
    print(f"Total notes written: {len(notes)}")


def main():
    """Main function"""
    notes = collect_notes()

    if len(notes) > 0:  # Very first input is not 'done'
        filename = get_filename()
        save_notes(notes, filename)
    else:
        print("\nNo notes to save. Exiting...")


# Run the program
if __name__ == "__main__":
    main()
