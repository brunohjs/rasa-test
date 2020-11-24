from .__init__ import *

class ActionGreet(Action):
    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        utils.log(tracker.latest_message)
        dispatcher.utter_message(
            text=random.choice([
                "Olá!😃",
                "Oi!😃",
                "Eai!😃"
            ])
        )
        dispatcher.utter_message(
            text="Seja bem-vindo(a)! Sou seu assistente virtual e vou te ajudar a fazer cotação e conversões monetárias."
        )
        return []
