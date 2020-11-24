from .__init__ import *

class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        utils.log(tracker.latest_message)
        last_event = tracker.get_last_event_for('user', skip=1)
        last_confidence = last_event['parse_data']['intent']['confidence'] if last_event else None
        last_intent = last_event['parse_data']['intent']['name'] if last_event else None
        dispatcher.utter_message(
            text=random.choice([
                "Desculpe, mas não entendi sua frase.",
                "Desculpe, mas acho que não captei sua mensagem.",
                "Desculpe, mas não consegui entender."
            ])
        )
        if (last_confidence and last_confidence < 0.8) or last_intent == 'out_of_scope':
            dispatcher.utter_message(
                text="Aqui estão algumas sugestões:",
                buttons=[
                    {"title": "Cotação do Real", "payload": "/exchange_rate"},
                    {"title": "Converter R$ para outras moedas", "payload": "/conversion"},
                    {"title": "Lista de moedas", "payload": "/currency_list"},
                    {"title": "Sobre mim", "payload": "/explanation"},
                    {"title": "Sair", "payload": "/farewell"}
                ],
                button_type="reply"
            )
        else:
            dispatcher.utter_message(
                text="Poderia tentar novamente, por favor?"
            )
        return []
