from .__init__ import *

class ActionExchangeRate(Action):
    def name(self) -> Text:
        return "action_exchange_rate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        utils.log(tracker.latest_message)
        dispatcher.utter_message(
            text=utils.showCurrencyPrice()
        )
        return []
