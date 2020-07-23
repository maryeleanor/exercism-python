def latest(scores):
    last = len(scores)
    latest = scores[last-1]
    return latest

def personal_best(scores):
    counter = 0
    for i in range(len(scores)):
        if scores[i] >= counter: 
            counter = scores[i]
    return counter

def personal_top_three(scores):
    top_three = []
    scores.sort(reverse=True)
    if len(scores) < 3:
        return scores
    for i in range(3):
        top_three.append(scores[i])
    return top_three
