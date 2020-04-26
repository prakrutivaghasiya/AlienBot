# importing regex and random libraries
import re
import random


class AlienBot:
  # potential negative responses
  negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
  # keywords for exiting the conversation
  exit_commands = ("quit", "pause", "exit", "goodbye",
                   "bye", "later", 'stop', 'bubye')
  # random starter questions
  random_questions = (
      "Why are you here? \n",
      "Are there many humans like you? \n",
      "What do you consume for sustenance? \n",
      "Is there intelligent life on this planet? \n",
      "Does Earth have a leader? \n",
      "What planets have you visited? \n",
      "What technology do you have on this planet? \n"
  )

  def __init__(self):
    self.alienbabble = {'describe_planet_intent': r'.*\s*your planet.*',
                        'answer_why_intent': r'why\s*.*',
                        'cubed_intent': r'.*cube.* (\d+)'
                        }

  # Define .greet() below:
  def greet(self):
    self.name = input('''Welcome to the AlienBot!
    Please enter your name. \n''')

    will_help = input(f'''Hi {self.name}, I'm Etcetera. I'm not from this planet. 
    Will you help me learn about your planet? \n''')

    if will_help.lower() in self.negative_responses:
      print("Ok, have a nice Earth Day!")
      return

    self.chat()

  # Define .make_exit() here:
  def make_exit(self, reply):
    for exit_command in self.exit_commands:
      if exit_command in reply.lower():
        print("Ok, have a nice day!")
        return True
    return False

  # Define .chat() next:
  def chat(self):
    reply = input(random.choice(self.random_questions)).lower()
    while not self.make_exit(reply):
      reply = input(self.match_reply(reply))

  # Define .match_reply() below:
  def match_reply(self, reply):
    for key, value in self.alienbabble.items():
      intent = key
      regex_pattern = value
      found_match = re.match(regex_pattern, reply)

      if found_match and intent == 'describe_planet_intent':
        return self.describe_planet_intent()
      elif found_match and intent == 'answer_why_intent':
        return self.answer_why_intent()
      elif found_match and intent == 'cubed_intent':
        print(found_match.groups()[0])
        return self.cubed_intent(found_match.groups()[0])

    return self.no_match_intent()

  # Define .describe_planet_intent():
  def describe_planet_intent(self):
    responses = ("My planet is a utopia of diverse organisms and species. \n",
                 "I am from Opidipus, the capital of the Wayward Galaxies. \n")
    return random.choice(responses)

  # Define .answer_why_intent():
  def answer_why_intent(self):
    responses = ("I come in peace. \n", "I am here to collect data on your planet and its inhabitants. \n",
                 "I heard the coffee is good. \n")
    return random.choice(responses)

  # Define .cubed_intent():
  def cubed_intent(self, number):
    cubed_number = int(number) ** 3
    return f"The cube of {number} is {cubed_number}. Isn't that cool? \n"

  # Define .no_match_intent():
  def no_match_intent(self):
    responses = ('Please tell me more. \n',
                 'Tell me more! \n',
                 'Why do you say that? \n',
                 'I see. Can you elaborate? \n',
                 'Interesting. Can you tell me more? \n',
                 'I see. How do you think? \n',
                 'Why? \n',
                 'How do you think I feel when you say that? \n')
    return random.choice(responses)


# Create an instance of AlienBot below:
AlienBot_instance = AlienBot()
AlienBot_instance.greet()
