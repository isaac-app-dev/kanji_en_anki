I built this project to automatically generate Anki decks for studying Kanji. I am making this project available for anyone who would like to either:

1. download the repo and tune it to their own studying needs
2. download the .apkg directly and use in their anki platform to study the cards that I create.

I will be regularly updating this repo with new datasets as I continue my studying and growing my kanji learning list. Feel free to watch/follow this repo for those updates so that you can get the latest set.

If you just want the .apkg file to import into anki:

   Navigate to the kanji_en_anki/decks folder and download the file. You can import this into your anki user profile.

If you would like to build this project locally, a couple of key points:

1. This project was built from macOS. There are applescripts used to interact with the Numbers application for handling my CSV data. You can tune this to work for other apps (i.e. Excel on windows), but this project itself is built for macOS.

2. Script Dependencies: Python3, genanki library, hashlib library.

3. You must run the code from the project root folder due to how the FILEPATH locations are used. Again you can tune this yourself.

   3a. Run the following commands, in the following order:

   i. python3 scripts/export_numbers.py

   ii. python3 scripts/db_build.py

   iii. python3 scripts/build_deck.py
