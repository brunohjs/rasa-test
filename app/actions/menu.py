from .__init__ import *

class ActionMenu(Action):
    def name(self) -> Text:
        return "action_menu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        utils.log(tracker.latest_message)
        dispatcher.utter_message(
            text="Aqui está o menu. Escolha uma das opções a seguir:",
            buttons=[
                {"title": "Cotação do Real", "payload": "/exchange_rate"},
                {"title": "Converter R$ para outras moedas", "payload": "/conversion"},
                {"title": "Lista de moedas", "payload": "/currency_list"},
                {"title": "Sobre mim", "payload": "/explanation"},
                {"title": "Sair", "payload": "/farewell"}
            ],
            button_type="reply"
        )
        return []
