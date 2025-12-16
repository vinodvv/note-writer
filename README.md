# Note Writer

A command-line daily note-taking tool with optional AI-powered analysis. Write your thoughts, ideas, and tasks directly from your terminal and get intelligent insights about your day.

## Features

### Basic Version (`note_writer_beginner.py`)
- 📝 Simple interactive note collection
- 💾 Automatic file organization with date-based naming
- 📁 Creates and manages a `Notes` directory
- ⏰ Timestamps each session automatically

### Advanced Version (`note_writer_advanced.py`)
- ✨ All basic features plus:
- 🤖 AI-powered note analysis using Google's Gemini
- 📊 Sentiment analysis and productivity scoring
- 🎯 Automatic action item extraction
- 💡 Theme identification
- 🌟 Personalized motivational messages

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Basic Version
No additional dependencies required! Just Python's standard library.

### Advanced Version
Install required packages:

```bash
pip install google-genai python-dotenv
```

## Setup

1. **Clone the repository:**
```bash
git clone https://github.com/vinodvv/note-writer.git
cd note-writer
```

2. **For Advanced Version - Set up Gemini API:**
   - Get a free API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a `.env` file in the project root:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

### Basic Version
```bash
python note_writer_beginner.py
```

### Advanced Version
```bash
python note_writer_advanced.py
```

### Example Session
```
Enter your notes (type 'done' when finished):

Note: Completed the project documentation
Note: Had a productive team meeting
Note: Need to follow up on client emails
Note: done

Writing notes to file....
File Saved: Notes/notes_2024-12-16.txt

Notes saved successfully!
Total notes written: 3

AI ANALYSIS OF YOUR NOTES
Analyzing your notes...
[AI-generated insights appear here]
```

## File Structure

```
note-writer/
├── note_writer_beginner.py    # Simple note-taking script
├── note_writer_advanced.py    # AI-enhanced version
├── .env                        # API key (not tracked in git)
├── .gitignore                  # Excludes .env and Notes/
├── Notes/                      # Auto-created directory
│   ├── notes_2024-12-16.txt
│   └── notes_2024-12-17.txt
└── README.md
```

## AI Analysis Features

The advanced version provides:

1. **Overall Sentiment** - Understands the emotional tone of your day
2. **Main Themes** - Identifies key topics and focus areas
3. **Action Items** - Extracts tasks that need attention
4. **Motivational Message** - Personalized encouragement
5. **Productivity Score** - Rates your accomplishments (1-10)

## Notes Format

Notes are saved as plain text files with the format `notes_YYYY-MM-DD.txt` in the `Notes` directory. Each file contains all notes from that day, making it easy to review and search your history.

## Privacy & Security

- All notes are stored **locally** on your machine
- The advanced version sends notes to Google's Gemini API for analysis
- Never commit your `.env` file or API keys to version control
- The `.gitignore` file is configured to protect sensitive data

## Tips

- Use descriptive notes for better AI insights
- Type `done` on a new line to finish your session
- Review previous days by opening files in the `Notes` folder
- Run the script daily to build a comprehensive journal

## Troubleshooting

**"GEMINI_API_KEY is not set" error:**
- Ensure your `.env` file exists and contains the API key
- Check that the `.env` file is in the same directory as the script

**Import errors:**
- Run `pip install google-genai python-dotenv` for the advanced version

**Permission errors:**
- Ensure you have write permissions in the script directory

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Google Gemini AI](https://deepmind.google/technologies/gemini/)
- Inspired by the need for simple, effective daily journaling

## Author

Created by [vinodvv](https://github.com/vinodvv)

---

**Happy note-taking! 📝✨**