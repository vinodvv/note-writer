import os
from datetime import datetime
from google import genai
from dotenv import load_dotenv

TODAY = datetime.now()
OUTPUT_DIR = "Notes"
FILE_NAME = f"notes_{TODAY.year}-{TODAY.month:02d}-{TODAY.day:02d}.txt"
FILEPATH = os.path.join(OUTPUT_DIR, FILE_NAME)


def load_credentials():
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")
    return api_key


def collect_notes():
    """Collect notes from user until they type 'done'"""
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
    """Generate filename based on today's date"""
    # Check Notes folder exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Create filename with today's date
    filename = FILEPATH

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


def analyze_notes(client, notes):
    """Analyze notes"""
    print("\nAI ANALYSIS OF YOUR NOTES")
    print("\nAnalyzing your notes...")
    notes_text = ["\n".join(f"-{note}" for note in notes)]

    prompt = f"""
            Analyze the following daily notes and provide:

            1. **Overall Sentiment:** (Positive/Neutral/Negative and why)
            2. **Main Themes:** (What topics or areas are covered)
            3. **Suggested Action Items:** (What the person should do based on their notes)
            4. **Brief Motivational Message:** (Encourage the person)
            5. **Productivity Score:** (Rate from 1-10 based on accomplishments mentioned)

            Notes:
            {notes_text}

             Please provide a concise, encouraging analysis.
        """

    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt
    )
    print(f"\n{response.text}")


def main():
    """Main function"""
    api_key = load_credentials()
    client = genai.Client(api_key=api_key)
    notes = collect_notes()

    if len(notes) > 0:  # Very first input is not 'done'
        filename = get_filename()
        save_notes(notes, filename)
        analyze_notes(client, notes)
    else:
        print("\nNo notes to save. Exiting...")


# Run the program
if __name__ == "__main__":
    main()

