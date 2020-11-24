from .__init__ import *

class ActionConversion(Action):
    def name(self) -> Text:
        return "action_conversion"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        utils.log(tracker.latest_message)
        dispatcher.utter_message(
            text="Qual o valor que você quer converter?"
        )
        return []
