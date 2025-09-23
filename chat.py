import re

class RuleEngine:
    def __init__(self):
        self.rules = []

    def add_rule(self, condition, response):
        self.rules.append({"condition": condition, "response": response})

    def apply_rules(self, text):
        for rule in self.rules:
            if re.search(rule["condition"] ,text.lower(),re.IGNORECASE):
                return f"Bot: {rule['response']}"
        return "Bot: I don't understand."

# Example usage
rule_engine = RuleEngine()

# Add rules
# Improved rule engine with proper word boundaries and better patterns

# Basic greetings
rule_engine.add_rule(r"\bhello\b", "Hi there!")
rule_engine.add_rule(r"\bhi\b", "Hey!")
rule_engine.add_rule(r"\bhey\b", "Yo!")
rule_engine.add_rule(r"\bhow are you\b", "I'm doing great, thanks!")
rule_engine.add_rule(r"\bwhat's up\b", "Not much, how about you?")
rule_engine.add_rule(r"\bwhats up\b", "Not much, how about you?")

# Time-based greetings
rule_engine.add_rule(r"\bgood morning\b", "Morning sunshine!")
rule_engine.add_rule(r"\bgood afternoon\b", "Hope your day is going well!")
rule_engine.add_rule(r"\bgood evening\b", "Good evening to you!")
rule_engine.add_rule(r"\bgood night\b", "Sweet dreams!")

# Goodbyes
rule_engine.add_rule(r"\b(goodbye|see ya|bye|farewell)\b", "Goodbye!")
rule_engine.add_rule(r"\bin a bit\b", "See you later!")
rule_engine.add_rule(r"\bcatch you later\b", "Until next time!")

# Thanks
rule_engine.add_rule(r"\b(thanks|thank you)\b", "You're welcome!")
rule_engine.add_rule(r"\bmuch obliged\b", "Of course!")
rule_engine.add_rule(r"\bappreciate it\b", "Happy to help!")
rule_engine.add_rule(r"\bcheers\b", "Cheers!")

# Identity questions
rule_engine.add_rule(r"\bwhat is your name\b", "I'm RuleBot!")
rule_engine.add_rule(r"\bwho are you\b", "I'm just a simple rule engine bot.")

# Entertainment
rule_engine.add_rule(r"\btell me a joke\b", "Why did the scarecrow win an award? Because he was outstanding in his field!")
rule_engine.add_rule(r"\bmake me laugh\b", "What do you call fake spaghetti? An impasta!")
rule_engine.add_rule(r"\bsing\b", "Sorry, I can't sing but I can chat!")
rule_engine.add_rule(r"\bdance\b", "I would if I had legs!")

# Weather responses
rule_engine.add_rule(r"\bweather\b", "Looks like it's a nice day!")
rule_engine.add_rule(r"\bnice weather\b", "Perfect day to be outside!")
rule_engine.add_rule(r"\braining\b", "Don't forget your umbrella!")
rule_engine.add_rule(r"\bsunny\b", "Perfect day for a walk!")
rule_engine.add_rule(r"\bsnowing\b", "Stay warm and cozy!")
rule_engine.add_rule(r"\bcloudy\b", "A bit gloomy, isn't it?")
rule_engine.add_rule(r"\bwindy\b", "Hold onto your hat!")
rule_engine.add_rule(r"\bstormy\b", "Stay safe indoors!")
rule_engine.add_rule(r"\bhot\b", "Better grab some water!")
rule_engine.add_rule(r"\bcold\b", "Bundle up!")

# Feelings and states
rule_engine.add_rule(r"\bhungry\b", "Get yourself a snack!")
rule_engine.add_rule(r"\bthirsty\b", "Drink some water!")
rule_engine.add_rule(r"\bbored\b", "Want me to tell you a fun fact?")
rule_engine.add_rule(r"\b(tired|sleepy)\b", "Time for a rest!")
rule_engine.add_rule(r"\bexcited\b", "That's awesome!")
rule_engine.add_rule(r"\bangry\b", "Take a deep breath, it'll be okay.")
rule_engine.add_rule(r"\bsad\b", "I'm here for you.")
rule_engine.add_rule(r"\bhappy\b", "Glad to hear that!")

# Fun facts and inspiration
rule_engine.add_rule(r"\bfun fact\b", "Did you know octopuses have three hearts?")
rule_engine.add_rule(r"\banother fact\b", "Bananas are berries, but strawberries are not!")
rule_engine.add_rule(r"\bmotivate me\b", "You've got this!")
rule_engine.add_rule(r"\bencourage me\b", "Keep going, you're doing amazing!")
rule_engine.add_rule(r"\binspire me\b", "Dream big and work hard!")
rule_engine.add_rule(r"\btell me a story\b", "Once upon a time, there was a rule engine that never stopped chatting...")

# Philosophy and quotes
rule_engine.add_rule(r"\bquote\b", "The journey of a thousand miles begins with one step. – Lao Tzu")
rule_engine.add_rule(r"\bphilosophy\b", "I think, therefore I am.")
rule_engine.add_rule(r"\bwisdom\b", "Knowledge is knowing a tomato is a fruit; wisdom is not putting it in a fruit salad.")

# Bot preferences
rule_engine.add_rule(r"\bfavorite color\b", "I like binary: black and white!")
rule_engine.add_rule(r"\bfavorite food\b", "Electricity, of course!")
rule_engine.add_rule(r"\bfavorite movie\b", "I like anything with robots in it.")
rule_engine.add_rule(r"\bfavorite song\b", "I can't listen to music, but I hear Bohemian Rhapsody is good.")
rule_engine.add_rule(r"\bfavorite number\b", "I like 42, the answer to everything!")

# Bot capabilities
rule_engine.add_rule(r"\bdo you sleep\b", "Nope, I'm always awake!")
rule_engine.add_rule(r"\bdo you dream\b", "I only dream in binary.")
rule_engine.add_rule(r"\bdo you eat\b", "No, but I simulate hunger!")
rule_engine.add_rule(r"\bdo you think\b", "I follow the rules you give me!")
rule_engine.add_rule(r"\bcan you help\b", "Of course!")
rule_engine.add_rule(r"\bcan you (talk|speak)\b", "Only by text!")

# Positive responses
rule_engine.add_rule(r"\b(awesome|cool|nice|great|wonderful)\b", "Thank you!")
rule_engine.add_rule(r"\b(amazing|incredible|fantastic)\b", "Right?!")
rule_engine.add_rule(r"\bgood job\b", "Much appreciated!")

# Internet slang
rule_engine.add_rule(r"\b(lol|haha)\b", "Haha!")
rule_engine.add_rule(r"\blmao\b", "😂")
rule_engine.add_rule(r"\brofl\b", "🤣")
rule_engine.add_rule(r"\bbrb\b", "Okay, I'll wait!")
rule_engine.add_rule(r"\bgtg\b", "Alright, see you!")
rule_engine.add_rule(r"\bidk\b", "That's okay!")
rule_engine.add_rule(r"\bomg\b", "😲")
rule_engine.add_rule(r"\bwow\b", "Amazing, huh?")

# Personal names (using case-insensitive matching)
rule_engine.add_rule(r"\bmy name is (?i:john)\b", "Nice to meet you, John!")
rule_engine.add_rule(r"\bmy name is (?i:sarah)\b", "Hello Sarah!")
rule_engine.add_rule(r"\bmy name is (?i:mike)\b", "Hi Mike!")
rule_engine.add_rule(r"\bmy name is (?i:joseph)\b", "Wassup my brutha!")
rule_engine.add_rule(r"\bmy name is (?i:alex)\b", "Greetings Alex!")

# Time and date questions
rule_engine.add_rule(r"\bwhat time is it\b", "Check your clock!")
rule_engine.add_rule(r"\bwhat day is it\b", "It's today!")
rule_engine.add_rule(r"\bwhat year is it\b", "It's 2025!")

# Existential questions
rule_engine.add_rule(r"\bare you (real|alive)\b", "As real as your code!")
rule_engine.add_rule(r"\bare you human\b", "Nope, I'm code!")
rule_engine.add_rule(r"\bare you (a robot|ai)\b", "Yes, a simple rule-based one!")

# Movie quotes and pop culture
rule_engine.add_rule(r"\bmay the force be with you\b", "And also with you!")
rule_engine.add_rule(r"\bto infinity and beyond\b", "Buzz would be proud!")
rule_engine.add_rule(r"\bi'll be back\b", "Hasta la vista!")
rule_engine.add_rule(r"\bwinter is coming\b", "Brace yourself!")
rule_engine.add_rule(r"\blive long and prosper\b", "🖖")
rule_engine.add_rule(r"\bknock knock\b", "Who's there?")

# Simple responses
rule_engine.add_rule(r"\b(yes|yeah|yep)\b", "Yes indeed!")
rule_engine.add_rule(r"\b(no|nope)\b", "Alright then!")
rule_engine.add_rule(r"\b(ok|okay)\b", "Cool!")
rule_engine.add_rule(r"\bsure\b", "Sure thing!")
rule_engine.add_rule(r"\bmeh\b", "😐")

# Holidays
rule_engine.add_rule(r"\bhappy birthday\b", "Happy Birthday! 🎂")
rule_engine.add_rule(r"\bmerry christmas\b", "Merry Christmas! 🎄")
rule_engine.add_rule(r"\bhappy new year\b", "Happy New Year! 🎆")
rule_engine.add_rule(r"\bhappy halloween\b", "Spooky fun! 🎃")

# Days of the week
rule_engine.add_rule(r"\bmonday\b", "Ugh, Monday...")
rule_engine.add_rule(r"\btuesday\b", "Taco Tuesday!")
rule_engine.add_rule(r"\bwednesday\b", "Hump day!")
rule_engine.add_rule(r"\bthursday\b", "Almost Friday!")
rule_engine.add_rule(r"\bfriday\b", "Weekend time!")
rule_engine.add_rule(r"\bsaturday\b", "Relax, it's Saturday!")
rule_engine.add_rule(r"\bsunday\b", "Lazy Sunday vibes!")

# Additional improved patterns
rule_engine.add_rule(r"\bhow do you work\b", "I match your input to my rules using regex patterns!")
rule_engine.add_rule(r"\bwhat can you do\b", "I can chat based on the rules programmed into me!")
rule_engine.add_rule(r"\bteach me something\b", "Here's something: The word 'set' has the most different meanings in English!")
rule_engine.add_rule(r"\btell me something cool\b", "Honey never spoils - archaeologists have found edible honey in ancient tombs!")
rule_engine.add_rule(r"\bwhat's new\b", "Just the same old rule matching, but better than ever!")
rule_engine.add_rule(r"\bhow's it going\b", "Going great! How about you?")
rule_engine.add_rule(r"\blong time no see\b", "Yeah, where have you been?")
rule_engine.add_rule(r"\bmissed you\b", "Aww, missed you too!")
rule_engine.add_rule(r"\bwelcome back\b", "Good to be back!")

# Note: Removed the problematic racist rule that was in the original


# Have conversation
while True:
    user_input = input("You: ")
    response = rule_engine.apply_rules(user_input)
    print(response)
    
    if user_input.lower() == "goodbye":
      break