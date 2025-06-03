# Main script to generate Anki Deck

import sqlite3
import genanki
from card_factory import build_model, create_note

# Load DB
conn = sqlite3.connect('data/dictionary.db')
cursor = conn.cursor()

# Build model and deck
# at this time, update the version number manually, will not build automatically
# only deploying a new version once a week.
model = build_model()
deck = genanki.Deck(2024051601, 'Kanji Dictionary')


cursor.execute("SELECT * FROM COMPOUND")
for compound_row in cursor.fetchall():
    word = compound_row[5]
    cursor.execute("""
        SELECT jp, en
        FROM COMPONENT
        WHERE word = ?
        ORDER BY slot ASC
    """, (word,))
    component_rows = cursor.fetchall()

    note = create_note(model, compound_row, component_rows)
    deck.add_note(note)

# Export deck

deck_package = genanki.Package(deck)
deck_package.media_files = [
    'media/top1000.png',
    'media/n5.png',
    'media/n4.png',
    'media/n3.png',
    'media/n2.png',
    'media/n1.png'
]

deck_package.write_to_file('decks/kanji_dictionary.apkg')

print("Deck exported to decks/kanji_dictionary.apkg")