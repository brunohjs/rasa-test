from .__init__ import *

class ActionCurrencyList(Action):
    def name(self) -> Text:
        return "action_currency_list"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        utils.log(tracker.latest_message)
        dispatcher.utter_message(text=utils.showCurrencyList())
        return []
