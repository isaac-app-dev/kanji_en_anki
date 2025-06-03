# Handles Dynamic Card Creation

import genanki
import hashlib

# Fixed ID for our Model
MODEL_ID = 1607392319

# Load card templates
def load_templates():
    with open('templates/card_front.html', 'r', encoding='utf-8') as f:
        front = f.read()
    with open('templates/card_back.html', 'r', encoding='utf-8') as f:
        back = f.read()
    with open('templates/card_style.css', 'r', encoding='utf-8') as f:
        css = f.read()
    return front, back, css

# Define the Anki card model
def build_model():
    front, back, css = load_templates()

    return genanki.Model(
        MODEL_ID,
        'KanjiCardModel',
        fields=[
            {'name': 'usage_type'},     # center top (with entry_char)
            {'name': 'entry_char'},     # center top (with usage_type)
            {'name': 'jlpt'},           # top-right of card
            {'name': 'word'},           # center of card
            {'name': 'word_type'},      # under the word (if applicable)
            {'name': 'components'},     # hint content on front + breakdown on back
            {'name': 'jp'},             # back of card: reading
            {'name': 'en'},             # back of card: English meaning
            {'name': 'top_1000'},       # bottom-left of card (front and back)
            {'name': 'num_slots'},      # functional (optional for scripting/layout)
            {'name': 'entry_num'},       # optional reference for Kodansha (internal or footer)
            {'name': 'top1000_badge'},
            {'name': 'jlpt_badge'},
            {'name': 'compound_id'}
        ],
        templates=[
            {
                'name': 'Kanji-English Template',
                'qfmt': front,
                'afmt': back,
            },
        ],
        css=css
    )

# Convert data from DB into a genanki.Note
def create_note(model, compound_row, component_rows):
    compound_id, entry_char, entry_num, top_1000, usage_type, word, num_slots, jp, en, jlpt, word_type  = compound_row


    #build unique guid for each compound_id in table
    guid = hashlib.md5(str(compound_id).encode('utf-8')).hexdigest()

    # Build tag list based on fields
    tags = []

    # JLPT level tag: n5, n4, etc.
    if jlpt:
        tags.append(jlpt.lower())

    # Top 1000 kanji tag
    if top_1000:
        tags.append("top1000")

    # Format components list
    components_html = ""
    for char_jp, char_en in component_rows:
        components_html += f"{char_jp} = {char_en}<br>"

    top1000_badge = '<img src="top1000.png" width="70">' if top_1000 else ""

    jlpt_badge_map = {
    "N5": '<img src="n5.png" alt="JLPT N5" width="60">',
    "N4": '<img src="n4.png" alt="JLPT N4" width="60">',
    "N3": '<img src="n3.png" alt="JLPT N3" width="60">',
    "N2": '<img src="n2.png" alt="JLPT N2" width="60">',
    "N1": '<img src="n1.png" alt="JLPT N1" width="60">',
    
    }
    jlpt_badge = jlpt_badge_map.get(jlpt, "")

    return genanki.Note(
        model=model,
        fields=[
            usage_type or "",
            entry_char or "",
            jlpt,
            word,
            word_type or "",
            components_html,
            jp,
            en,
            "1" if top_1000 else "0",
            str(num_slots),
            str(entry_num) if entry_num else "",
            top1000_badge,
            jlpt_badge,
            str(compound_id)
        ],
        tags=tags, #set genanki tags field to tags array we created
        guid=guid #include created guid in guid field
    )