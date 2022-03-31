import random
from bots_setup.communication import Message

actions = {
    "chill": ["drink", "party", "travel to"],
    "work": ["code", "write", "read"],
    "sport": ["play", "run", "drive"],
    "bad thing": ["steal", "fight"],
}

#This method takes an action from above and adds a subject to it
def suggestions(action: str):
    subjects = {
        "drink": ['beer', 'coffee', 'wine'],
        "travel to": ['Paris', 'New York', 'Oslo'],
        "code": ['chatbot', 'website'],
        "write": ['book', 'rapport'],
        "read": ['poem', 'the paper', 'python book'],
        "play": ['football', 'basketball', 'tennis'],
        "drive": ['sport car', 'motorcycle'],
        "fight": ['Floyd Mayweather', 'Conor Mcgregor', 'our professor'],
        "steal": ["book", "car", "computer from school"],
    }
    subject_in_action = action
    if action in subjects:
        return f"{subject_in_action} {random.choice(subjects[action])}"
    else:
        return action

def my_bot():
    name = 'Host'                                                 # username
    suggestion_types = ["sport", "chill", "work", "bad thing"]    # interests
    suggestion = random.choice(suggestion_types)                  # random choise of interests
    action = random.choice(actions[suggestion])                   # random choise action of chosen suggesion
    print("Host suggested " + suggestion)                         # print Host suggestion
    subject = suggestions(action)                                 # action choices
    responses = [                                                 # message from host
        f"Do you guys want to {subject}?",
        f"Let's {subject} guys!!",
    ]
    raondom_response =random.choice(responses)                    #Random choise of messages
    return Message(sender=name, response=raondom_response,        # Return usenname, message and
                   action=action, suggestion_type=suggestion)     #chosen action and suggestion

def madelen(response: Message):
    name = 'Madelen'                                                # username
    suggestion = "sport"                                            # interests
    change_suggestion = random.choice(actions[suggestion])          # random choise action of chosen suggesion
    responses = [                                                   # response from Madelen
        f"I dont like it, but I will join",
        f"I have some other stuff to do.",
        f"That one isn't fair, I would like to {change_suggestion}",
    ]
    random_response = random.choice(responses)                      #Random choise of messages
    return Message(sender=name, response=random_response)           # Return usenname and response

def felix(response: Message):
    name = 'Felix'
    suggestion = "work"
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

'''
 This function takes a name and Message object
 and returns a bot with the given name.
'''
def choose_bot(name: str, msg: Message):
    choose = {
        "Madelen": madelen(msg),
        "Felix": felix(msg),
        "Marija": marija(msg),
        "Rateb": rateb(msg),
    }
    return choose[name]

