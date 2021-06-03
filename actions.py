# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import re
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

def validate_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex,email)):
        return True
    else:
        return False

class ActionSignUp(Action):

    def name(self) -> Text:
        return "action_sign_up"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot('name')
        email = tracker.get_slot('email')
        number = tracker.get_slot('number')
        password = tracker.get_slot('password')

        valid = validate_email(email)
        # customer_id = sign_up(name, email, password)
        if valid and name is not None and password is not None:
            dispatcher.utter_message(text="utter_authsignup_success")
        else: 
            dispatcher.utter_message(text="utter_authsignup_failed")

        return []

class ActionDomain(Action):

    def name(self) -> Text:
        return "action_domain"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        brand = tracker.get_slot('brand')
        site = tracker.get_slot('site')

        print(brand, site)

        if name is not None and password is not None:
            dispatcher.utter_message(text="utter_auth_success")
        else:
            dispatcher.utter_message(text="utter_auth_failed")

        return []


class ActionSignIn(Action):

    def name(self) -> Text:
        return "action_sign_in"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot('name')
        password = tracker.get_slot('password')

        # customer_id = sign_up(name, email, password)
        if name is not None and password is not None:
            dispatcher.utter_message(text="utter_authsignin_succed")
        else: 
            dispatcher.utter_message(text="utter_authsignin_fail")

        return []