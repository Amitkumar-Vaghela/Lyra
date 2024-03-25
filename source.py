from flask import Flask, render_template, request
import random

app = Flask(__name__)

characters = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Fiona", "George", "Hannah", "Ian", "Julia"]
settings = ["a mystical woodland glade", "the towering spires of an ancient citadel", "the neon-lit streets of a futuristic metropolis", "a hidden hamlet nestled amidst rolling hills", "an abandoned space station orbiting a distant planet", "a bustling market in a desert oasis", "a serene temple atop a mist-covered mountain", "a sun-drenched beach on a tropical island"]
problems = ["stumbled upon a forgotten portal to another realm", "came face to face with a legendary phoenix guarding its nest", "embarked on a quest to decipher cryptic clues left by a long-lost sorcerer", "sought the cure to a curse woven by a mischievous sprite", "discovered a map leading to a buried treasure", "encountered a time-traveling anomaly", "uncovered a conspiracy threatening the kingdom", "faced a moral dilemma with no easy solution"]
actions = ["summoned courage to confront", "unraveled the enigma confounding", "extended a helping hand to aid", "negotiated a pact with the wily guardian of", "bravely faced the challenges posed by", "delved deep into the mysteries of", "forged alliances with unlikely allies to overcome", "used wit and cunning to outsmart"]

def generate_story(character, setting, problem, action):
    story = f"In a land far, far away, {character} found themselves amidst {setting}. They {problem}, and with unwavering determination, they {action} the challenge."
    return story

@app.route('/')
def index():
    story = generate_story(random.choice(characters), random.choice(settings), random.choice(problems), random.choice(actions))
    return render_template('index.html', story=story)

@app.route('/generate', methods=['POST'])
def generate():
    character = request.form['character']
    setting = request.form['setting']
    problem = request.form['problem']
    action = request.form['action']
    story = generate_story(character, setting, problem, action)
    return render_template('index.html', story=story)

if __name__ == '__main__':
    app.run(debug=True)
