# vordle

Install Jinja2

`pip install Jinja2`

Run `wordle.py`

`python3 wordle.py`

This will write updated results to `index.html`

You can customize the game by editing the included text files and metadata.json

`answers.txt` is the list of answers. Order does matter here: the first answer will be used on the first day, the second on the second day, etc. You can control which day is the first day by editing `start_date` in `metadata.json`. Note that this does need to be in `yyyy-MM-dd` format, e.g. `2021-12-01`


`guesses.txt` is the list of accepted guesses. Order does not matter. The full list of accepted guesses is the combination of `guesses.txt` and `answers.txt`, so you don't need to list the answers in `guesses.txt` (but it's fine if you do)


`keyboard.txt` defines the keyboard layout. Letters represent themselves, obviously. `<` represents backspace and `>` represents enter


`letters.txt` defines the letters that can be input. If a letter is in `keyboard.txt` but not `letters.txt` there will be a keyboard key present, but it will be disabled


`metadata.json` defines the title of the variant, the number of rows and columns, and the start date
