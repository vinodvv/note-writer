"""
Command-line daily note taker with AI analysis.

This script lets user enter multiple notes in the terminal, saves them
to a dated text file in a "Notes" directory, and sends the notes to an
AI model for sentiment, themes, action items and motivation.
"""

import os
from datetime import datetime
from google import genai
from dotenv import load_dotenv


def load_credentials():
    """Load the Gemini API key from environment variables and return it, 
    raising an error if missing."""
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not set in the environment.")
    return api_key


def collect_notes():
    """Collect notes from user until they type 'done' is entered and
    return them as a list of strings."""
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
    """Build and return the full path for today's notes file,
    creating the 'Notes' directory if needed."""
    today = datetime.now()

    filename = today.strftime("notes_%Y-%m-%d.txt")

    # Output directory
    directory = "Notes"
    os.makedirs(directory, exist_ok=True)

    return os.path.join(directory, filename)


def save_notes(notes, filename):
    """Save all notes to the given file, add a dated header, one note per line, and
    print a short summary."""
    print("\nWriting notes to file....")

    with open(filename, "w", encoding="utf-8") as file:
        # Add a simple header, to make the file more readable.
        file.write(f"# Notes for {datetime.now().strftime('%Y-%m-%d')}\n\n")
        for note in notes:
            file.write(note + "\n")

    print(f"File Saved: {filename}\n")
    print("Notes saved successfully!")
    print(f"Total notes written: {len(notes)}")


def analyze_notes(client, notes):
    """Send notes to the AI client for analysis and print the model's feedback"""
    print("\nAI ANALYSIS OF YOUR NOTES")
    print("\nAnalyzing your notes...")
    notes_text = "\n".join(f"- {note}" for note in notes)

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
        """.strip()
    try:
        response = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt
        )
        print(f"\n{response.text}")
    except Exception as e:
        print(f"\nAI analysis failed: {e}")


def main():
    """Coordinate loading credentials, collecting notes, saving them and 
    running the AI analysis workflow."""
    api_key = load_credentials()
    client = genai.Client(api_key=api_key)
    notes = collect_notes()

    if len(notes) > 0:  # Very first input is not 'done'
        filepath = get_filename()
        save_notes(notes, filepath)
        analyze_notes(client, notes)
    else:
        print("\nNo notes to save. Exiting...")


# Run the program
if __name__ == "__main__":
    main()

