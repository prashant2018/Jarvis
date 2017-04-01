import random

def generateValue(l):
    a = random.choice(l)
    return a

def greet():
    values = ["Hi, Have a good day","Hi, hope you are having a lovely day"]
    return generateValue(values)


def regret():
    values = ["I am still learning. Thankyou","I am not as intelligent as Siri.","I am a beginner now"]
    return generateValue(values)

def jokes():
    values = ["Siri is my girlfriend", "Cortana is my sister", "I am better than Siri","Donald trump rocks"]
    return generateValue(values)





