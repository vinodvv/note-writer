"""
Simple command-line note-writing tool.

This script lets the user type multiple notes interactively in the terminal
and saves them to a dated text file inside a "Notes" folder.
Each run creates (or reuses) a file named like "note_YYYY-mm-dd.txt".
"""

from datetime import datetime
import os


def collect_notes():
    """
    Collect notes from user until they type 'done' is entered and
    return them as a list of strings.
    '"""
    # Create an empty list to store all notes
    notes = []

    # Start main loop
    print("\nEnter your notes (type 'done' when finished):\n")

    while True:
        note = input("Note: ")

        # Check if user wants to finish
        if note.lower() == "done":
            break

        # Add the note to list
        notes.append(note)

    return notes


def get_filename():
    """Return the full path for today's notes file,
    creating the 'Notes' directory if needed"""
    today = datetime.now()

    # Create filename with today's date
    filename = today.strftime("notes_%Y-%m-%d.txt")

    # Output directory
    directory = "Notes"
    os.makedirs(directory, exist_ok=True)

    return os.path.join(directory, filename)


def save_notes(notes, filename):
    """Write all notes to the given file path, one note per line, and
    print a short summary."""
    print("\nWriting notes to file....")

    with open(filename, "w", encoding="utf-8") as file:
        for note in notes:
            file.write(note + "\n")

    print(f"File Saved: {filename}\n")
    print("Notes saved successfully!")
    print(f"Total notes written: {len(notes)}")


def main():
    """Run the interactive not-taking workflow: collect notes,
    save them, or exit if none are provided."""
    notes = collect_notes()

    if len(notes) > 0:  # Very first input is not 'done'
        filepath = get_filename()
        save_notes(notes, filepath)
    else:
        print("\nNo notes to save. Exiting...")


# Run the program
if __name__ == "__main__":
    main()
