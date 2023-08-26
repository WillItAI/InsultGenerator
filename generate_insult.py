import json
import random
import os

def generate_insult():
    # Load data from JSON files
    with open(os.path.join("static", "data", "relations.json"), "r") as file:
        relations = json.load(file)["relations"]

    with open(os.path.join("static", "data", "bodypart.json"), "r") as file:
        bodyparts = json.load(file)["body_parts"]

    with open(os.path.join("static", "data", "size.json"), "r") as file:
        sizes = json.load(file)["sizes"]

    with open(os.path.join("static", "data", "sillyword.json"), "r") as file:
        silly_words = json.load(file)["silly_features_plural"]

    # Randomly select words from each list
    random_relation = random.choice(relations)
    random_bodypart = random.choice(bodyparts)
    random_size = random.choice(sizes)
    random_silly_word = random.choice(silly_words)

    # Compile the insult
    insult = f"Your {random_relation} has {random_size} {random_bodypart} {random_silly_word}"

    return insult
