All three files are ready. Here's the folder structure:


jeopardy/
├── index.html        ← the game
├── game-data.json    ← edit this to change questions
├── server.py         ← run this to launch
└── images/           ← drop local images here
To launch: open a terminal in the jeopardy folder and run:


python server.py
It will open http://localhost:8080 in your browser automatically.

How to edit game-data.json:

Each question/answer supports three content types:


{ "type": "text",    "content": "Your clue text here" }
{ "type": "image",   "content": "images/yourfile.jpg" }
{ "type": "youtube", "content": "https://www.youtube.com/watch?v=VIDEO_ID" }
{ "type": "image-text", "image": "images/chess_position.png", "content": "White to move — find the best continuation."}
You can mix types freely — e.g. an image clue with a text answer, or a YouTube clue with a text answer.

Gameplay flow:

Setup screen → pick 1–8 players, name them, hit Start (or Enter)
Board → click a tile to open it
Question screen → Spacebar reveals the answer; Escape goes straight back without revealing
Answer screen → Escape returns to the board and greys the tile
Scoreboard → +/− buttons use the last-opened tile's value; click the score directly to type any number; names are editable inline at any time