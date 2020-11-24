from .__init__ import *

class ActionShowConversion(Action):
    def name(self) -> Text:
        return "action_show_conversion"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        utils.log(tracker.latest_message)
        message = utils.showConversions(tracker.latest_message['entities'])
        dispatcher.utter_message(text=message)
        return []
