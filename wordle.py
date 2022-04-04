from datetime import datetime
import json

from jinja2 import Environment, FileSystemLoader, select_autoescape

def get_metadata(filename='metadata.json'):
    with open(filename, 'rt') as file:
        return json.load(file)

def get_word_list(filename):
    words = []
    with open(filename, 'rt') as file:
        for line in file:
            word = line.strip()
            if word and not word.startswith('#'):
                words.append(line.strip())
    return words


def get_valid_answers(answers='answers.txt'):
    return get_word_list(answers)


def get_valid_guesses(guesses='guesses.txt', answers='answers.txt'):
    answers = get_valid_answers(answers)
    guesses = get_word_list(guesses)
    return {word: True for word in answers + guesses}


def get_letters(filename='letters.txt'):
    with open(filename, 'rt') as file:
        return list(file.read().strip())


def get_keyboard(filename='keyboard.txt'):
    rows = []
    with open(filename, 'rt') as file:
        for line in file:
            rows.append(list(line.strip()))
    return rows


def to_milliseconds(date):
    return datetime.fromisoformat(date).timestamp() * 1000

def create():
    env = Environment(
        loader=FileSystemLoader('templates')
    )
    template = env.get_template('wordle.html')
    kwargs = {
        "valid_guesses": json.dumps(get_valid_guesses()),
        "valid_answers": json.dumps(get_valid_answers()),
        "letters": json.dumps(get_letters()),
        "keyboard": json.dumps(get_keyboard())
    }
    kwargs.update(get_metadata())
    kwargs["start_date"] = to_milliseconds(kwargs["start_date"])
    result = template.render(**kwargs)
    for name in ('result.html', 'index.html'):
        with open(name, 'wt', encoding='utf-8') as file:
            file.write(result)
    

if __name__ == '__main__':
    import time
    while True:
        create()
        time.sleep(1)
