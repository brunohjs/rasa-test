from .__init__ import *

class ActionFarewell(Action):
    def name(self) -> Text:
        return "action_farewell"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        utils.log(tracker.latest_message)
        dispatcher.utter_message(
            text="Estarei aqui a qualquer momento."
        )
        dispatcher.utter_message(
            text=random.choice([
                "Até mais!👋😄",
                "Tchau!👋😄"
            ])
        )
        return []
