import random

def generate_score():

    score = random.randint(60,95)

    if score > 85:
        verdict = "Very Promising"
    elif score > 70:
        verdict = "Moderate Potential"
    else:
        verdict = "High Risk"

    return score, verdict