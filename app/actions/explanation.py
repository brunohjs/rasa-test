from .__init__ import *

class ActionExplanation(Action):
    def name(self) -> Text:
        return "action_explanation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        utils.log(tracker.latest_message)
        dispatcher.utter_message("Sou um assistente com o objetivo de fazer conversões e cotações monetárias.\n\nAinda estou em fase de testes, mas já consigo fazer algumas coisas.\n\nConsigo converter valores da nossa moeda (R$) para outras moedas, é só me dizer o valor. Além disso, eu posso te mostrar a cotação em tempo real da nossa moeda. Você também pode me pedir para listar as moedas que conheço. Para qualquer dúvida é só ir ao menu ou pedir ajuda.")
        return []
