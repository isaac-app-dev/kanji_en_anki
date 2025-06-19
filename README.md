# Kanji Anki Deck Generator

This project automatically generates **Anki decks** to support studying Japanese Kanji. It's designed for learners who want to:

* Customize and generate their own Anki decks based on their study preferences.
* Download prebuilt `.apkg` decks and start studying immediately in Anki.

## 📦 Getting Started

You can either **download the prebuilt decks** or **build your own deck** using the provided scripts.

---

### ✅ Use Prebuilt Anki Decks

If you just want the ready-made Anki deck:

1. Navigate to the [`decks/`](./decks) folder.
2. Download the latest `.apkg` file.
3. Import it into your Anki profile and start studying.

---

### 🛠️ Build the Project Locally

This project was developed on **macOS** and uses **AppleScript** to interact with **Apple Numbers** for CSV data export.

> ⚠️ You may need to adapt parts of the workflow if you're using Windows or Linux (e.g., switch from Apple Numbers to Excel).

#### Dependencies

* Python 3
* [`genanki`](https://github.com/kerrickstaley/genanki)
* `hashlib` (standard Python library)

Install required Python packages:

```bash
pip install genanki
```

#### Directory Assumptions

Run all scripts from the **project root directory**, due to hardcoded file paths.

#### 📋 Step-by-Step Build Instructions

1. Export your data from Apple Numbers:

```bash
python3 scripts/export_numbers.py
```

2. Build the internal kanji database:

```bash
python3 scripts/db_build.py
```

3. Generate the Anki deck:

```bash
python3 scripts/build_deck.py
```

---

## 🔄 Updates

I update this repository regularly with new Kanji datasets as I continue studying. **Watch or follow** the repo to stay up to date with the latest decks.

---

## 📁 Project Structure

```bash
kanji-anki-deck-generator/
├── decks/               # Prebuilt .apkg decks for Anki
├── scripts/             # Scripts for data export and deck generation
├── data/                # CSV or intermediate data files
├── README.md            # Project documentation
```

---

## 🙌 Contributing & Feedback

Feedback and contributions are welcome! Feel free to open issues or submit pull requests.

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

Happy studying! 頑張って！📚🇯🇵
