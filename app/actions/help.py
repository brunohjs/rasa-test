from .__init__ import *

class ActionHelp(Action):
    def name(self) -> Text:
        return "action_help"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        utils.log(tracker.latest_message)
        dispatcher.utter_message(
            text=random.choice([
                "Você está perdido(a)?",
                "Algo está errado?",
                "Você precisa de ajuda?"
            ])
        )
        return []
