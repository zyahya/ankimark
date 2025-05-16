# 📚 **AnkiMark: Markdown to Anki Card Generator**

Convert cleanly structured Markdown notes into fully formatted Anki cards — complete with questions, answers, and optional notes.

---

## 🚀 Overview

**AnkiMark** is a Python script that allows you to write Anki flashcards in a readable Markdown format and automatically converts them into an Anki-importable `.csv` file.

It supports:

- Markdown formatting for answers and notes
- Optional notes field for additional information
- Simple `---` separator for card definitions

---

## 📄 Input Format (`cards.md`)

Write your cards using this format:

```md
# What are the benefits of X?

- Improves focus
- Enhances memory
- Boosts productivity

::  
Can also be used in daily journaling.

---

# Define Y.

- A short explanation here.

::  
Useful for exams.
```

- `#` First line = Question
- Following lines = Answer (Markdown supported)
- `::` = Optional notes section
- `---` = Card separator

---

## 🛠️ How It Works

- Reads the `cards.md` file
- Parses the structure into three fields: **Question**, **Answer**, and **Notes**
- Converts Markdown to HTML (for rich formatting in Anki)
- Saves output as a tab-separated `anki_cards.csv` file ready for import

---

## 📥 How to Use

1. Write your cards in a `cards.md` file using the format above.
2. Run the script:

```bash
python generate_anki_cards.py
```

3. Import the generated `anki_cards.csv` file into Anki:

   - File > Import
   - Select `anki_cards.csv`
   - Set field mapping:

     - Field 1 → Front
     - Field 2 → Back
     - Field 3 → Notes (optional, configure in note type)

   - Choose tab as separator
   - Make sure HTML is enabled in your note type

---

## 📦 Requirements

- Python 3.x
- [`markdown`](https://pypi.org/project/Markdown/) module
