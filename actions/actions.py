# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
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



class QpmcTicketRaise(Action):

    def name(self) -> Text:
        return "Qpmc_ticket_raise_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        hardware_type = tracker.get_slot("hardware_type")

        ticket_type = tracker.get_slot("ticket_type")
        
        monitor_inches = tracker.get_slot("monitor_inches")

        dispatcher.utter_message(text=f"ticket raise action is working fine {hardware_type} {ticket_type} {monitor_inches}")

        return []
