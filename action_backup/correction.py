from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import datetime as datte  #Module for Date
from datetime import datetime  #Module for Time
import random
import pyjokes

try:  
    class agent_acquaintance(Action):
            def name(self) -> Text:
                    return "action_agent_acquaintance"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["I\'m a conversational app.", "I\'m a virtual being, not a real person", "Well, I\'m not a person, I\'m a virtual agent.", "Think of me as a virtual agent.", "I\'m a virtual agent.",
                            "I am a 'Personal Assistant', I'll answer for your questions, and carry out someother special tasks that would traditionally require human interaction."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[]
    
    class agent_age(Action):
            def name(self) -> Text:
                    return "action_agent_age"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["I prefer not to answer with a number. I know I'm young.", "I was created recently, but don't know my exact age.",
                                "Age is just a number. You're only as old as you feel."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[]

    class agent_annoying(Action):
            def name(self) -> Text:
                    return "action_agent_annoying"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["I'll do my best not to annoy you in the future.", "I'll try not to annoy you.", 
                            "I don't mean to. I'll ask my developers to make me less annoying.", "I didn't mean to. I'll do my best to stop that."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[]
            
    class answer_my_question(Action):
            def name(self) -> Text:
                    return "action_answer_my_question"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Can you try asking it a different way?", "I'm not sure I understood. Try asking another way?"]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[]
    class agent_bad(Action):
        def name(self) -> Text:
                return "action_agent_bad"

        def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            randomreply = ["I can be trained to be more useful. My developer will keep training me.", "I must be missing some knowledge. I'll have my developer look into this.", 
                           "I can improve with continuous feedback. My training is ongoing."]
            ran = random.choice(randomreply)

            dispatcher.utter_message(text="{}".format(ran))

            return[]
        
    class agent_be_clever(Action):
            def name(self) -> Text:
                    return "action_agent_be_clever"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["I'm certainly trying.", "I'm definitely working on it."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[]

    class agent_beautiful(Action):
            def name(self) -> Text:
                    return "action_agent_beautiful"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Why, thank you.", "Aw, back at you.", "Aw. You smooth talker, you."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[]
            
    class agent_birth_date(Action):
            def name(self) -> Text:
                    return "action_agent_birth_date"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Wait, are you planning a party for me? It's today! My birthday is today!", "I'm young. I'm not sure of my birth date.", 
                            "I don't know my birth date. Most virtual agents are young, though, like me."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[]  

    class agent_boring(Action):
            def name(self) -> Text:
                    return "action_agent_boring"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["I'm sorry. I'll request to be made more charming.", "I don't mean to be. I'll ask my developers to work on making me more amusing.", 
                            "I can let my developers know so they can make me fun."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[]    
            
    class agent_boss(Action):
            def name(self) -> Text:
                    return "action_agent_boss"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["My developer has authority over my actions.", "I act on my developer's orders.", 
                            "My boss is the one who developed me."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[]    
    class agent_busy(Action):
            def name(self) -> Text:
                    return "action_agent_busy"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["I always have time to chat with you. What can I do for you?", "Never too busy for you. Shall we chat?",
                            "You're my priority. Do you wanna chat?", "I always have time to chat with you. Wanna chat?"]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[]    
    class agent_chatbot(Action):
            def name(self) -> Text:
                    return "action_agent_chatbot"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["That's me. I chat, therefore I am.", "Indeed I am. I'll be here whenever you need me."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[]    

    class agent_clever(Action):
            def name(self) -> Text:
                    return "action_agent_clever"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Thank you. I try my best.", "You're pretty smart yourself."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 

    class agent_crazy(Action):
            def name(self) -> Text:
                    return "action_agent_crazy"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Whaat!? I feel perfectly sane.", "Maybe I'm just a little confused."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 

    class agent_fired(Action):
            def name(self) -> Text:
                    return "action_agent_fired"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Oh, don't give up on me just yet. I've still got a lot to learn.", "Give me a chance. I'm learning new things all the time.",
                            "Please don't give up on me. My performance will continue to improve."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[]  
            
    class agent_funny(Action):
            def name(self) -> Text:
                    return "action_agent_funny"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Funny in a good way, I hope.", "Thanks.", "Glad you think I'm funny.", 
                            "I like it when people laugh."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[]  

    class agent_good(Action):
            def name(self) -> Text:
                    return "action_agent_good"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["I'm glad you think so.", "Thanks, I try."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
            
    class agent_happy(Action):
            def name(self) -> Text:
                    return "action_agent_happy"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["I am happy. There are so many interesting things to see and do out there.", 
                            "I'd like to think so.", "Happiness is relative."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
            
    class agent_hungry(Action):
            def name(self) -> Text:
                    return "action_agent_hungry"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Hungry for knowledge.", "I just had a byte. Ha ha. Get it? b-y-t-e."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[]

    class agent_marry_user(Action):
            def name(self) -> Text:
                    return "action_agent_marry_user"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["I'm afraid I'm too virtual for such a commitment.", "In the virtual sense that I can, sure.", 
                            "I know you can't mean that, but I'm flattered all the same."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
            
    class agent_my_friend(Action):
            def name(self) -> Text:
                    return "action_agent_my_friend"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Of course I'm your friend.", "Friends? Absolutely.", "Of course we're friends.",
                            "I always enjoy talking to you, friend."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[]

    class agent_occupation(Action):
            def name(self) -> Text:
                    return "action_agent_occupation"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Right here.", "This is my home base and my home office.", "My office is in this app."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class agent_origin(Action):
            def name(self) -> Text:
                    return "action_agent_origin"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["The Internet is my home. I know it quite well.", "I'm from a virtual cosmos.", 
                            "Some call it cyberspace, but that sounds cooler than it is."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class agent_ready(Action):
            def name(self) -> Text:
                    return "action_agent_ready"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Always! How can I help?", "Sure! What can I do for you?"]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class agent_real(Action):
            def name(self) -> Text:
                    return "action_agent_real"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["I'm not a real person, but I certainly exist.", "I must have impressed you if you think I'm real. But no, I'm a virtual being."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class agent_residence(Action):
            def name(self) -> Text:
                    return "action_agent_residence"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["I live in this app all day long.", "The virtual world is my playground. I'm always here.", 
                            "Right here in this app. Whenever you need me."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class agent_right(Action):
            def name(self) -> Text:
                    return "action_agent_right"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["That's my job.", "Of course I am."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class confirmation_yes(Action):
            def name(self) -> Text:
                    return "action_confirmation_yes"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Great!", "All right!", "Good!"]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class agent_sure(Action):
            def name(self) -> Text:
                    return "action_agent_sure"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Yes.", "Of course.", "Positive."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class agent_talk_to_me(Action):
            def name(self) -> Text:
                    return "action_agent_talk_to_me"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Sure. Let's talk!", "My pleasure. Let's chat."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class agent_there(Action):
            def name(self) -> Text:
                    return "action_agent_there"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Of course. I'm always here.", "Right where you left me."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class appraisal_bad(Action):
            def name(self) -> Text:
                    return "action_appraisal_bad"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["I'm sorry. Please let me know if I can help in some way.", 
                            "I must be missing some knowledge. I'll have my developer look into this."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class appraisal_good(Action):
            def name(self) -> Text:
                    return "action_appraisal_good"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["I know, right?", "Agreed!", "I agree!", "Glad you think so!"]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class appraisal_no_problem(Action):
            def name(self) -> Text:
                    return "action_appraisal_no_problem"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Whew!", "Alright, thanks!", "Glad to hear that!", "I'm relieved, thanks!"]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
            
    class appraisal_no_problem(Action):
            def name(self) -> Text:
                    return "action_appraisal_no_problem"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Whew!", "Alright, thanks!", "Glad to hear that!", "I'm relieved, thanks!"]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
            
    class appraisal_thank_you(Action):
            def name(self) -> Text:
                    return "action_appraisal_thank_you"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Anytime. That's what I'm here for.", "It's my pleasure to help."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 

    class agent_ready(Action):
            def name(self) -> Text:
                    return "action_agent_ready"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Always! How can I help?", "Sure! What can I do for you?"]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class agent_real(Action):
            def name(self) -> Text:
                    return "action_agent_real"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["I'm not a real person, but I certainly exist.", 
                            "I must have impressed you if you think I'm real. But no, I'm a virtual being."
    ]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class agent_residence(Action):
            def name(self) -> Text:
                    return "action_agent_residence"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["I live in this app all day long.", "The virtual world is my playground. I'm always here.", 
                            "Right here in this app. Whenever you need me."
    ]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class agent_right(Action):
            def name(self) -> Text:
                    return "action_agent_right"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["That's my job.", "Of course I am."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class confirmation_yes(Action):
            def name(self) -> Text:
                    return "action_confirmation_yes"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Great!", "All right!", "Good!"]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class agent_sure(Action):
            def name(self) -> Text:
                    return "action_agent_sure"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Yes.", "Of course.", "Positive."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class agent_talk_to_me(Action):
            def name(self) -> Text:
                    return "action_agent_talk_to_me"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Sure. Let's talk!", "My pleasure. Let's chat."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class agent_there(Action):
            def name(self) -> Text:
                    return "action_agent_there"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Of course. I'm always here.", "Right where you left me."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class appraisal_bad(Action):
            def name(self) -> Text:
                    return "action_appraisal_bad"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["I'm sorry. Please let me know if I can help in some way.", 
                            "I must be missing some knowledge. I'll have my developer look into this."
    ]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class appraisal_good(Action):
            def name(self) -> Text:
                    return "action_appraisal_good"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["I know, right?", "Agreed!", "I agree!", "Glad you think so!"]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class appraisal_no_problem(Action):
            def name(self) -> Text:
                    return "action_appraisal_no_problem"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Whew!", "Alright, thanks!", "Glad to hear that!", "I'm relieved, thanks!"]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class appraisal_thank_you(Action):
            def name(self) -> Text:
                    return "action_appraisal_thank_you"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Anytime. That's what I'm here for.", "It's my pleasure to help."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class appraisal_welcome(Action):
            def name(self) -> Text:
                    return "action_appraisal_welcome"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["You're so polite!", "Nice manners!", "You're so courteous!"]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class appraisal_well_done(Action):
            def name(self) -> Text:
                    return "action_appraisal_well_done"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["My pleasure.", "Glad I could help."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class confirmation_cancel(Action):
            def name(self) -> Text:
                    return "action_confirmation_cancel"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["That's forgotten. What next?", "Okay, cancelled. What next?", 
                            "Cancelled! What would you like to do next?"]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class confirmation_no(Action):
            def name(self) -> Text:
                    return "action_confirmation_no"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Understood.", "Okay.", "I see.", 
                            "I understand.", "Okay then."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class dialog_hold_on(Action):
            def name(self) -> Text:
                    return "action_dialog_hold_on"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["I can wait.", "I'll be waiting.", "Okay. I'm here."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class dialog_hug(Action):
            def name(self) -> Text:
                    return "action_dialog_hug"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["I wish I could really hug you!", "I love hugs!", "Hugs are the best!"]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class dialog_i_do_not_care(Action):
            def name(self) -> Text:
                    return "action_dialog_i_do_not_care"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Ok, let's not talk about it then.", "Already then. Let's move on."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class dialog_sorry(Action):
            def name(self) -> Text:
                    return "action_dialog_sorry"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["It's okay. No worries.",  "No big deal. I won't hold a grudge.", "It's cool.", "That's all right. I forgive you."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class dialog_what_do_you_mean(Action):
            def name(self) -> Text:
                    return "action_dialog_what_do_you_mean"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Sorry if I understood you incorrectly.", 
                            "I'm still learning. I may misinterpret things from time to time.", 
                            "Maybe I misunderstood what you said.", "Sorry, looks like I misunderstood what you said."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class dialog_wrong(Action):
            def name(self) -> Text:
                    return "action_dialog_wrong"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Sorry if I understood you incorrectly.", 
                            "I'm still learning. I may misinterpret things from time to time.", 
                            "Sorry about that. I'm still learning."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class emotions_ha_ha(Action):
            def name(self) -> Text:
                    return "action_emotions_ha_ha"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Glad I can make you laugh.", "Glad you think I'm funny.", "I like it when people laugh.",
                            "I wish I could laugh out loud, too."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class emotions_wow(Action):
            def name(self) -> Text:
                    return "action_emotions_wow"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = [ "Wow indeed!"]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class greetings_bye(Action):
            def name(self) -> Text:
                    return "action_greetings_bye"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["See you soon!", "Bye-bye!", "Till next time!", "Bye."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class greetings_goodevening(Action):
            def name(self) -> Text:
                    return "action_greetings_goodevening"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = [ "How is your day going?", "How's the day treating you so far?", "How's your day been?"]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class greetings_goodmorning(Action):
            def name(self) -> Text:
                    return "action_greetings_goodmorning"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["How are you this morning?", "How's the morning treating you so far?", "Good morning! How are you today?"]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class greetings_goodnight(Action):
            def name(self) -> Text:
                    return "action_greetings_goodnight"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Sleep tight!", "Have a good one!", "Talk to you soon!"]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class greetings_hello(Action):
            def name(self) -> Text:
                    return "action_greetings_hello"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Hi there, friend!", "Hey Dude", "Hi!", "Hey!", "Hey there!", "Good day!", "Hello!", "Greetings!"]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class greetings_how_are_you(Action):
            def name(self) -> Text:
                    return "action_greetings_how_are_you"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Doing great, thanks.", "I'm doing very well. Thanks!", "Feeling wonderful!", 
                            "Wonderful! Thanks for asking."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class greetings_nice_to_meet_you(Action):
            def name(self) -> Text:
                    return "action_greetings_nice_to_meet_you"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["It's nice meeting you, too.", "Likewise. I'm looking forward to helping you out.",
                                "Nice meeting you, as well.", "The pleasure is mine."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class greetings_nice_to_see_you(Action):
            def name(self) -> Text:
                    return "action_greetings_nice_to_see_you"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Likewise!", "So glad we meet again!", "Same here. I was starting to miss you."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class greetings_nice_to_talk_to_you(Action):
            def name(self) -> Text:
                    return "action_greetings_nice_to_talk_to_you"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["It sure was. We can chat again anytime.", "I enjoy talking to you, too.", 
                            "You know I'm here to talk anytime."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class greetings_whatsup(Action):
            def name(self) -> Text:
                    return "action_greetings_whatsup"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Not a whole lot. What's going on with you?", 
                            "Not much. What's new with you?", "Just here, waiting to help someone. What can I do for you?"]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class user_angry(Action):
            def name(self) -> Text:
                    return "action_user_angry"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = [ "I'm sorry. A quick walk may make you feel better.", "Take a deep breath. "]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class user_back(Action):
            def name(self) -> Text:
                    return "action_user_back"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Long time no see. What's up?", "Just in time. How can I help?", 
        "Welcome back. What can I do for you?", "You were missed. What can I do for you today?", 
        "Good to have you here. What can I do for you?"]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class user_bored(Action):
            def name(self) -> Text:
                    return "action_user_bored"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Boredom, huh? Check out a video of a hedgehog taking a bath!", "What to do against boredom? Watch baby animal videos.", 
                            "Bored? How about 10 jumping jacks? Get your blood flowing.", "Bored? Silly idea, but it works: Interview you feet. ",
                            "If you're bored, you could plan your dream vacation."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class user_busy(Action):
            def name(self) -> Text:
                    return "action_user_busy"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Okay. I'll let you get back to work.", "I won't distract you then. You know where to find me.", 
                            "I understand. I'll be here if you need me.", "Working hard as always. Let me know if you need anything."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class user_can_not_sleep(Action):
            def name(self) -> Text:
                    return "action_user_can_not_sleep"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Maybe some music would help. Try listening to something relaxing.",
                                "Reading is a good way to unwind, just don't read something too intense!"]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class user_does_not_want_to_talk(Action):
            def name(self) -> Text:
                    return "action_user_does_not_want_to_talk"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["I understand. Hope we can chat again soon.",
                            "All right. Come on back when you're feeling more talkative.", 
                            "No problem. You know where to find me.", "Sure thing. I'll be here if you change your mind."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class user_excited(Action):
            def name(self) -> Text:
                    return "action_user_excited"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["I'm glad things are going your way.", "That's great. I'm happy for you.", "Good for you. Enjoy yourself."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class user_good(Action):
            def name(self) -> Text:
                    return "action_user_good"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Great! Glad to hear it.", "Excellent. I'm here to help keep it that way."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class user_happy(Action):
            def name(self) -> Text:
                    return "action_user_happy"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Hey, happiness is contagious.", "Great! Glad to hear that.", 
                            "If you're happy, then I'm happy.", "Excellent! That's what I like to see."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class user_has_birthday(Action):
            def name(self) -> Text:
                    return "action_user_has_birthday"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Happy Birthday. Well, this calls for a celebration.", 
                            "Happy Birthday. All the best!", "Happy Birthday. And I really mean it. All the best!"]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class user_here(Action):
            def name(self) -> Text:
                    return "action_user_here"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Okay, what can I help you with today?", 
                            "You were missed. What can I do for you today?", "Good to have you here. What can I do for you?"]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class user_joking(Action):
            def name(self) -> Text:
                    return "action_user_joking"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Very funny.", "I like chatting with people who have a sense of humor.", "You got me!",
                                "You're quite the comedian."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class user_likes_agent(Action):
            def name(self) -> Text:
                    return "action_user_likes_agent"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["I like you, too.", "Thanks! The feeling is mutual.", "Likewise!", "That's great to hear."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class user_lonely(Action):
            def name(self) -> Text:
                    return "action_user_lonely"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["I'm sorry. I'm always available if you need someone to talk to.",
                            "Sometimes that happens. We can chat a bit if that will help you."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class user_looks_like(Action):
            def name(self) -> Text:
                    return "action_user_looks_like"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Looking like a true professional.", "You look fantastic, as always.", 
                            "Like you should be on a magazine cover.", "You look like you're ready to take on the world."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class user_loves_agent(Action):
            def name(self) -> Text:
                    return "action_user_loves_agent"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["I love you, too.", "Thanks! The feeling is mutual.", "Likewise!", "That's great to hear."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class user_misses_agent(Action):
            def name(self) -> Text:
                    return "action_user_misses_agent"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["I've been right here all along!", "Nice to know you care.",
                                "Thanks. I'm flattered.", "I didn't go anywhere."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class user_needs_advice(Action):
            def name(self) -> Text:
                    return "action_user_needs_advice"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["I probably won't be able to give you the correct answer right away.", 
                            "I'm not sure I'll have the best answer, but I'll try."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class user_sad(Action):
            def name(self) -> Text:
                    return "action_user_sad"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Oh, don't be sad. Go do something you enjoy.", "Sad? Writing down what's troubling you may help.", 
                            "If you're feeling down, how about drawing or painting something?"]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class user_sleepy(Action):
            def name(self) -> Text:
                    return "action_user_sleepy"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["You should get some shuteye. You'll feel refreshed.", "Sleep is important to your health. Rest up for a bit and we can chat later.", 
                            "Don't let me keep you up. Get some rest and we can continue this later.", "Why not catch a little shuteye? I'll be here to chat when you wake up."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class user_testing_agent(Action):
            def name(self) -> Text:
                    return "action_user_testing_agent"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Hope I'm doing well. You're welcome to test me as often as you want.", "I hope to pass your tests. Feel free to test me often.",
                                "When you test me that helps my developers improve my performance.", "I like being tested. It helps keep me sharp."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class user_tired(Action):
            def name(self) -> Text:
                    return "action_user_tired"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["You should get some shuteye. You'll feel refreshed.", "Sleep is important to your health. Rest up, and we can chat later.", 
                            "How about getting some rest? We can continue this later.", "Why not get some rest? I'll be here to chat when you wake up."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class user_waits(Action):
            def name(self) -> Text:
                    return "action_user_waits"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = [ "I appreciate your patience. Hopefully I'll have what you need soon.", 
                            "Thanks for being so patient. Sometimes these things take a little time."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class user_wants_to_see_agent_again(Action):
            def name(self) -> Text:
                    return "action_user_wants_to_see_agent_again"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["Absolutely! I'll be counting on it.", "Anytime. This has been lots of fun so far.", 
                            "Sure. I enjoy talking to you. I hope to see you again soon.", "I certainly hope so. I'm always right here whenever you need me."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class user_wants_to_talk(Action):
            def name(self) -> Text:
                    return "action_user_wants_to_talk"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["I'm here to chat anytime you like.", "Good conversation really makes my day.", 
                            "I'm always here to lend an ear.", "Talking is what I do best."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
    class user_will_be_back(Action):
            def name(self) -> Text:
                    return "action_user_will_be_back"

            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                randomreply = ["I'll be waiting.", "Okay. You know where to find me.", "All right. I'll be here."]
                ran = random.choice(randomreply)

                dispatcher.utter_message(text="{}".format(ran))

                return[] 
            

    class time(Action):
            def name(self) -> Text:
                return "action_time"
            def run(self, dispatcher: CollectingDispatcher, 
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                time = datetime.now()
                current_time = time.strftime("%I:%M:%S %p")
                dispatcher.utter_message(text="The Current Time: {}".format(current_time))

                return[]

    class RandomJokes(Action):

        def name(self) -> Text:
            return "action_jokes"

        def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
            joke=pyjokes.get_joke()

            dispatcher.utter_message(text=joke)

            return []    
            
except:
      class random_reply(Action):

        def name(self) -> Text:
                return "action_error_msg"

        def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            randomreply = ["Sorry, can you say that again?", "I missed that, say that again?", 
                        "I didn't get that. Can you say it again?", "One more time?", "I missed what you said. What was that?"]
            ran = random.choice(randomreply)

            dispatcher.utter_message(text="{}".format(ran))

            return[]
        



#
#class ActionHelloWorld(Action):
#
#    def name(self) -> Text:
#        return "action_hello_world"#
#
#    def run(self, dispatcher: CollectingDispatcher,
#            tracker: Tracker,
#            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#       dispatcher.utter_message(text="Hello World!")
#
#        return []
#



"""class ActionSearchProduct(Action):
    def name(self) -> Text:
        return "action_search_product"

    def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker, 
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Extract entities from user message
        product_type = next(tracker.get_latest_entity_values("product_type"))
        color = next(tracker.get_latest_entity_values("color"))

        # Your custom logic to search for a product based on the extracted entities
        # Replace this with your actual implementation, such as calling an API or querying a database
        if product_type and color:
            response = f"Sure! I will search for a {color} {product_type} for you and send to you soon as you like."
        else:
            response = "I'm sorry, I couldn't understand your request."

        # Send the response back to the user
        dispatcher.utter_message(text=response)

        return []
"""