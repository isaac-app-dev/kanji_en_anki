import csv
import sqlite3
from pathlib import Path

# Set paths
csv_dir = Path("/Users/isaac/Desktop/dev/anki_decks/kanji_en/data")
output_db = Path("/Users/isaac/Desktop/dev/anki_decks/kanji_en/data/dictionary.db")

compound_csv = csv_dir / "compound_input.csv"
component_csv = csv_dir / "component_input.csv"

# Connect to the database (creates if doesn't exist)
conn = sqlite3.connect(output_db)
cursor = conn.cursor()

# Drop and recreate tables
cursor.execute("DROP TABLE IF EXISTS COMPOUND")
cursor.execute("DROP TABLE IF EXISTS COMPONENT")

cursor.execute("""
CREATE TABLE COMPOUND (
    compound_id INTEGER PRIMARY KEY,
    entry_char TEXT,
    entry_num INTEGER,
    top_1000 BOOLEAN,
    usage_type TEXT,
    word TEXT,
    num_slots INTEGER,
    jp TEXT,
    en TEXT,
    jlpt TEXT,
    word_type TEXT
)
""")

cursor.execute("""
CREATE TABLE COMPONENT (
    word TEXT,
    slot INTEGER,
    jp TEXT,
    en TEXT
)
""")

# Load compound_input.csv
with open(compound_csv, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("""
        INSERT INTO COMPOUND (
            compound_id, entry_char, entry_num, top_1000, usage_type, word,
            num_slots, jp, en, jlpt, word_type
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            int(row['compound_id']),
            row['entry_char'],
            int(row['entry_num']) if row['entry_num'] else None,
            int(row['top_1000']),
            row['usage_type'],
            row['word'],
            int(row['num_slots']),
            row['jp'],
            row['en'],
            row['jlpt'],
            row['word_type']
        ))

# Load component_input.csv
with open(component_csv, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("""
        INSERT INTO COMPONENT (
            word, slot, jp, en
        ) VALUES (?, ?, ?, ?)
        """, (
            row['word'],
            int(row['slot']),
            row['jp'],
            row['en']
        ))

conn.commit()
conn.close()

print(f"✅ Database loaded successfully into {output_db}")