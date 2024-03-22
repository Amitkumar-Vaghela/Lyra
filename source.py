import random

# Lists of elements to compose the story
characters = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
settings = ["a magical forest", "an enchanted castle", "a bustling city", "a remote village"]
problems = ["lost their way home", "encountered a dragon", "searched for a hidden treasure", "needed to break a curse"]
actions = ["bravely fought", "cleverly outsmarted", "kindly helped", "wisely negotiated with"]

# Function to generate a story
def generate_story():
    # Randomly select elements for the story
    character = random.choice(characters)
    setting = random.choice(settings)
    problem = random.choice(problems)
    action = random.choice(actions)
    
    # Construct the story
    story = f"{character} found themselves in {setting}. They {problem} and had to {action} to solve it."
    return story

# Generate and print the story
print("Once upon a time...")
print(generate_story())

