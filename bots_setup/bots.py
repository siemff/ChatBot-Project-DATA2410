import random
from bots_setup.communication import Message

actions = {
    "sport": ["run", "play", "drive"],
    "chill": ["drink", "party"],
    "study": ["code", "write", "read"],
    "bad thing": ["steal", "fight"],
}

#This method takes an action and adds a subject to it
def suggestions(action: str):
    subjects = {
        "play": ['football', 'basketball', 'tennis'],
        "drive": ['sport car', 'motorcycle'],
        "drink": ['beer', 'coffee', 'wine'],
        "code": ['chatbot', 'website'],
        "write": ['essay', 'the rapport'],
        "read": ['novell', 'poem', 'comic book'],
        "fight": ['Floyd Mayweather', 'Conor Mcgregor', 'our professor'],
        "steal": ["book", "car", "computer from school"]
    }

    subject_in_action = action
    if action in subjects:
        return f"{subject_in_action} {random.choice(subjects[action])}"
    else:
        return action

def my_bot():
    name = 'Host'
    suggestion_types = ["sport", "chill", "study", "bad thing"]
    suggestion = random.choice(suggestion_types)
    action = random.choice(actions[suggestion])
    print("Host suggested " + suggestion)
    subject = suggestions(action)
    responses = [
        f"Do you guys want to {subject}?",
        f"Let's {subject} guys!!",
    ]
    raondom_response =random.choice(responses)
    return Message(sender=name, response=raondom_response,
                   action=action, suggestion_type=suggestion)

def madelen(response: Message):
    name = 'Madelen'
    suggestion = "sport"
    change_suggestion = random.choice(actions[suggestion])
    responses = [
        f"I dont like it, but I will join",
        f"I have some other stuff to do.",
        f"That one isn't fair, I would like to {change_suggestion}",
    ]
    random_response = random.choice(responses)
    return Message(sender=name, response=random_response)

def felix(response: Message):
    name = 'Felix'
    suggestion = "study"
    responses = [
        f"Yes, let`s do it.",
        f"WOW I can't wait for it!",
        "I have lots of homework folks, you have fun.",
    ]
    random_response = random.choice(responses)
    return Message(sender=name, response=random_response)

def marija(response: Message):
    name = 'Marija'
    suggestion = "bad thing"
    change_suggestion = random.choice(actions[suggestion])
    responses = [
        f"Let`s go for it then",
        f"I suggest {change_suggestion}",
        f"I can`t join!",
    ]
    random_response = random.choice(responses)
    return Message(sender=name, response=random_response)

def rateb(response: Message):
    name = 'Rateb'
    suggestion = "chill"
    change_suggestion = random.choice(actions[suggestion])
    responses = [
        f"Sounds great!! I am in.",
        f"That isn't my thing, you have a great time!",
        f"nah, let`s instead {change_suggestion}",
    ]
    random_response = random.choice(responses)
    return Message(sender=name, response=random_response)

# This methods takes a name and Message object
# and returns a bot with the given name.

def choose_bot(name: str, msg: Message):
    choose = {
        "Madelen": madelen(msg),
        "Felix": felix(msg),
        "Marija": marija(msg),
        "Rateb": rateb(msg),
    }
    return choose[name]

