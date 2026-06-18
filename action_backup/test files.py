"""from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from langdetect import detect
import random

# from actions import find_language
from find_language import find_language

class agent_acquaintance(Action):
            # def name(self) -> Text:
            #         return "action_agent_acquaintance"

            # def run(self, dispatcher: CollectingDispatcher,
            #         tracker: Tracker,
            #         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                
                latest_message = input()
                language_code = find_language(latest_message)
                # print(language_code)
                
                
                randomreply_en = ["I\'m a conversational app.", "I\'m a virtual being, not a real person", "Well, I\'m not a person, I\'m a virtual agent.", "Think of me as a virtual agent.", "I\'m a virtual agent.",
                            "I am a 'Personal Assistant', I'll answer for your questions, and carry out someother special tasks that would traditionally require human interaction."]
                ran_en = random.choice(randomreply_en)

                randomreply_ta = ["நான் ஒரு உரையாடல் பயன்பாடு","நான் ஒரு மெய்நிகர் உயிரினம், உண்மையான நபர் அல்ல"]
                ran_ta = random.choice(randomreply_ta)

                
                if language_code == "en":
                       
                        print("{}".format(ran_en))
                elif language_code == "ta":
                       print("{}".format(ran_ta))
                else:
                       print("Unable to find the language")


    """
import datetime

current_date = datetime.date.today()
print("Current date is:", current_date)
