import csv
import markdown
import re

with open("cards.md", "r", encoding="utf-8") as f:
    content = f.read()

cards = content.split('---')
rows = []

for card in cards:
    lines = card.strip().splitlines()
    if not lines:
        continue
    
    question = lines[0].replace('#', '').strip()
    
    answer_lines = []
    notes_lines = []
    notes_started = False

    for line in lines[1:]:
        if re.match(r'::', line, re.I):
            notes_started = True
            continue
        if not notes_started:
            answer_lines.append(line)
        else:
            notes_lines.append(line)

    answer_md = "\n".join(answer_lines).strip()
    notes_md = "\n".join(notes_lines).strip()

    answer_html = markdown.markdown(answer_md) if answer_md else ""
    notes_html = markdown.markdown(notes_md) if notes_md else ""

    rows.append([question, answer_html, notes_html])

with open("anki_cards.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile, delimiter='\t')
    writer.writerows(rows)
